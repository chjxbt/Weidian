# -*- coding:utf8 -*-
import json
import sys
import os
import uuid
import random
from datetime import datetime

from weixin import WeixinPay
from flask import request

from WeiDian import logger
from WeiDian.common.loggers import generic_log
from WeiDian.common.params_require import parameter_required
from WeiDian.config.enums import ORDER_STATUS, order_product_info_status, ORDER_STATUS_, OrderResend, OrderResendType
from WeiDian.config.kd import kd_list
from WeiDian.config.setting import QRCODEHOSTNAME, APP_ID, MCH_ID, MCH_KEY, notify_url
from WeiDian.common.TransformToList import dict_add_models, list_add_models
from WeiDian.common.timeformat import format_for_db, get_web_time_str
from WeiDian.common.token_required import verify_token_decorator, is_partner, is_admin
from WeiDian.common.import_status import import_status
from WeiDian.models.model import OrderProductInfo, OrderInfo, OrderProductResend
from WeiDian.service.SOrder import SOrder
from WeiDian.service.SProductImage import SProductImage
from WeiDian.service.SProductSkuKey import SProductSkuKey
from WeiDian.service.SProduct import SProduct
from WeiDian.service.SComplain import SComplain
from WeiDian.service.SUser import SUser
from WeiDian.config.response import PARAMS_MISS, SYSTEM_ERROR, AUTHORITY_ERROR, TOKEN_ERROR, NOT_FOUND, DumpliError
from WeiDian.common.token_required import is_tourist
from WeiDian.service.SRaward import SRaward
sys.path.append(os.path.dirname(os.getcwd()))


class COrder():
    def __init__(self):
        self.sorder = SOrder()
        self.sproductskukey = SProductSkuKey()
        self.sproduct = SProduct()
        self.sproductimage = SProductImage()
        self.suser = SUser()
        self.scomplain = SComplain()
        self.update_order_params = ['orid', 'oipaystatus']
        self.pay = WeixinPay(APP_ID, MCH_ID, MCH_KEY, notify_url)
        self.sraward = SRaward()

    @verify_token_decorator
    def add_one(self):
        if is_tourist():
            return TOKEN_ERROR
        data = request.json
        if not data:
            return PARAMS_MISS
        required = ['oiaddress', 'oirecvname', 'oirecvphone', 'sku']
        missed = filter(lambda x: x not in data, required)
        usid = request.user.id
        if missed:
            return PARAMS_MISS('必要参数缺失: ' + '/'.join(missed))
        with self.sorder.auto_commit() as session:
            pass
        # 建立订单
        order_dict = dict(
            oiid=str(uuid.uuid4()),
            usid=request.user.id,
            oisn=self._geceric_sn(),
            oileavetext=data.get('oileavetext') or '',
            oiaddress=data.get('oiaddress'),
            oirecvname=data.get('oirecvname'),
            oirecvphone=data.get('oirecvphone'),
            Sellerid=request.user.UPPerd
        )
        # 建立订单详情
        sku = data.get('sku')
        orderproductinfo_dict_list = self.fix_orderproduct_info(sku, order_dict['oiid'])
        list_add_models('OrderProductInfo', orderproductinfo_dict_list)
        order_dict['oimount'] = sum([x['SmallTotal'] for x in orderproductinfo_dict_list]) # 总价
        # 判断优惠券是否符合条件
        raid = data.get('raid')
        if raid:
            # 判断优惠券
            raward = self.sraward.get_raward_by_id(raid)
            if not raward:
                raise NOT_FOUND(u'不正确的优惠券')
            user_raward = self.get_reward_by_raid_usid(raid, usid)
            if not user_raward:
                raise NOT_FOUND(u'不正确的优惠券')
            # todo 可使用的转赠优惠券

            if raward.RAtype == 0:
                order_dict['oimount'] -= raward.RAamount
            order_dict['RAid'] = raid
        dict_add_models('OrderInfo', order_dict)
        data = import_status('add_order_success', 'OK')
        data['data'] = {
            'oiid': order_dict['oiid']
        }
        return data

    @verify_token_decorator
    def get_order_list_by_status(self):
        """根据订单状态获取"""
        if is_tourist():
            return AUTHORITY_ERROR(u"未登录")
        args = request.args.to_dict()
        logger.info("get order list args is %s", args)
        sell = args.get('sell', 'false')
        parameter_required("paystatus", "page_size", "page_num")
        status = args.get('paystatus')
        status = ['1', '4', '5', '6', '11'] if status == '0' else status
        status = ['2', '4', '5', '7', '9', '10', '11'] if status == '20' else status
        print status
        try:
            if sell == 'true':
                order_list = self.sorder.get_sell_order_by_status(request.user.id, status, int(args["page_num"]), int(args["page_size"]))
                # order_list_count = self.sorder.get_sell_ordercount_by_status(request.user.id, status)
            else:
                order_list = self.sorder.get_user_order_by_status(request.user.id, status, int(args["page_num"]), int(args["page_size"]))
                # order_list_count = self.sorder.get_user_ordercount_by_status(request.user.id, status)
            for order in order_list:
                # order.fields = ['OIid', 'OIsn', 'OIpaystatus', 'OIcreatetime']
                order.fill(ORDER_STATUS.get(str(order.OIpaystatus)), 'oipaystatusmsg')
                # map(self.fill_oistatusmessage, order_list)
                self.fill_productinfo(order)
                self.fill_complainstatus(order)
                order.fill(ORDER_STATUS_.get(str(order.OIpaystatus)), 'order_status')
                order.OIpaytime = get_web_time_str(order.OIpaytime)
                order.OIcreatetime = get_web_time_str(order.OIcreatetime)

            # map(self.fill_oistatusmessage, order_list)
            data = import_status('get_order_list_success', 'OK')
            data['totalcount'] = request.all_count
            data['data'] = order_list
            return data
        except Exception as e:
            logger.exception("get order list by status error")
            return SYSTEM_ERROR

    @verify_token_decorator
    def get_order_count(self):
        """获取订单预览数"""
        if is_tourist():
            return AUTHORITY_ERROR(u"未登录")
        print '已登录'
        args = request.args.to_dict()
        logger.info("get order count args is %s", args)
        sell = args.get('sell')
        print (request.user.id)
        all_status = ['1', '4', '5', '6', '11']
        if sell == 'true':
            json_data = [
                {
                    'status': u'全部',
                    'statusnum': u'0',
                    'count': self.sorder.get_sell_ordercount_by_status(request.user.id, all_status)
                },
                {
                    'status': u'待付款',
                    'statusnum': u'1',
                    'count': self.sorder.get_sell_ordercount_by_item_status(request.user.id, '1')
                },
                {
                    'status': u'待发货',
                    'statusnum': u'4',
                    'count': self.sorder.get_sell_ordercount_by_item_status(request.user.id, '4')
                },
                {
                    'status': u'待收货',
                    'statusnum': u'5',
                    'count': self.sorder.get_sell_ordercount_by_item_status(request.user.id, '5')
                },
                {
                    'status': u'已完成',
                    'statusnum': u'6',
                    'count': self.sorder.get_sell_ordercount_by_status(request.user.id, '6')
                },
                {
                    'status': u'退换货',
                    'statusnum': u'11',
                    'count': self.sorder.get_sell_ordercount_by_item_status(request.user.id, '11')
                }
            ]
        else:
            json_data = [
                {
                    'status': u'全部',
                    'statusnum': u'0',
                    'count': self.sorder.get_user_ordercount_by_status(request.user.id, all_status)
                },
                {
                    'status': u'待付款',
                    'statusnum': u'1',
                    'count': self.sorder.get_user_ordercount_by_item_status(request.user.id, '1')
                },
                {
                    'status': u'待发货',
                    'statusnum': u'4',
                    'count': self.sorder.get_user_ordercount_by_item_status(request.user.id, '4')
                },
                {
                    'status': u'待收货',
                    'statusnum': u'5',
                    'count': self.sorder.get_user_ordercount_by_item_status(request.user.id, '5')
                },
                {
                    'status': u'已完成',
                    'statusnum': u'6',
                    'count': self.sorder.get_user_ordercount_by_status(request.user.id, '7')
                },
                # {
                #     'status': u'已取消',
                #     'statusnum': u'7',
                #     'count': self.sorder.get_user_ordercount_by_status(request.user.id, '7')
                # },
                # {
                #     'status': u'待评价',
                #     'statusnum': u'10',
                #     'count': self.sorder.get_user_ordercount_by_status(request.user.id, '10')
                # },
                {
                    'status': u'退换货',
                    'statusnum': u'11',
                    'count': self.sorder.get_user_ordercount_by_item_status(request.user.id, '11')
                }
            ]

        data = import_status('get_order_count_success', 'OK')
        data['data'] = json_data
        return data

    @verify_token_decorator
    def get_order_info(self):
        if is_tourist():
            raise TOKEN_ERROR(u'请登录')
        data = request.args.to_dict()
        oiid = data.get('oiid')
        if not oiid:
            raise PARAMS_MISS(u'参数oiid缺失')
        order = self.sorder.get_order_by_oiid(oiid)
        usid = request.user.id
        if not order:
            raise NOT_FOUND(u'不存在的订单')
        if order.USid != usid and not is_admin():
            raise NOT_FOUND(u'他人订单')
        try:
            order.fill(ORDER_STATUS.get(str(order.OIpaystatus)), 'oipaystatusmsg')
            # map(self.fill_oistatusmessage, order_list)
            self.fill_productinfo(order)
            self.fill_complainstatus(order)
            order.fill(ORDER_STATUS_.get(str(order.OIpaystatus)), 'order_status')
            self.fill_productinfo(order)
            if is_admin():
                # 买家
                usid = order.USid
                user = self.suser.get_user_by_user_id(usid)
                if user.USlevel == 0:
                    user.level = 'ordinary'
                if user.USlevel > 0:
                    user.level = 'partner'
                user.add('level')
                order.fill(user, 'user')
                # 卖家
                upperusid = order.Sellerid
                upuser = self.suser.get_user_by_user_id(upperusid)
                if user.USlevel == 0:
                    user.level = 'ordinary'
                if user.USlevel > 0:
                    user.level = 'partner'
                user.add('level')
                order.fill(upuser, 'upper')
            # 填充退款信息
            order.OIpaytime = get_web_time_str(order.OIpaytime)
            order.OIcreatetime = get_web_time_str(order.OIcreatetime)
            response = import_status('get_order_list_success', 'OK')
            response['data'] = order
            return response
        except Exception as e:
            generic_log(e)
            raise e

    @verify_token_decorator
    def admin_get_order_count(self):
        if not is_admin():
            raise TOKEN_ERROR(u'请使用管理员登录')
        data = request.args.to_dict()
        usid = data.get('usid', '').strip() or None
        all_status = ['1', '4', '5', '6', '11']
        json_data = [
            {
                'status': u'全部',
                'statusnum': u'0',
                'count': self.sorder.get_sell_ordercount_by_status(usid, all_status)
            },
            {
                'status': u'待付款',
                'statusnum': u'1',
                'count': self.sorder.get_sell_ordercount_by_item_status(usid, '1')
            },
            {
                'status': u'待付款',
                'statusnum': u'5',
                'count': self.sorder.get_sell_ordercount_by_item_status(usid, '5')
            },
            {
                'status': u'待发货',
                'statusnum': u'4',
                'count': self.sorder.get_sell_ordercount_by_item_status(usid, '4')
            },
            {
                'status': u'已完成',
                'statusnum': u'6',
                'count': self.sorder.get_sell_ordercount_by_status(usid, '6')
            },
            {
                'status': u'退换货',
                'statusnum': u'11',
                'count': self.sorder.get_sell_ordercount_by_item_status(usid, '11')
            }
        ]
        data = import_status('get_order_count_success', 'OK')
        data['data'] = json_data
        return data

    @verify_token_decorator
    def admin_get_order_list(self):
        if not is_admin():
            raise TOKEN_ERROR(u'请使用管理员登录')
        parameter_required("paystatus")
        data = request.args.to_dict()
        usid = data.get('usid', '').strip() or None
        phone = data.get('phone', '').strip() or None
        page = data.get('page', '').strip() or 1
        count = data.get('count', '').strip() or 15
        status = data.get('paystatus')
        status = ['1', '4', '5', '6', '11'] if str(status) == '0' else status
        status = ['2', '4', '5', '7', '9', '10', '11'] if str(status) == '20' else status
        order_list = self.sorder.get_sell_order_by_status2(status, page, count, usid, phone)
        for order in order_list:
            order.fill(ORDER_STATUS.get(str(order.OIpaystatus)), 'oipaystatusmsg')
            # map(self.fill_oistatusmessage, order_list)
            self.fill_productinfo(order)
            self.fill_complainstatus(order)
            order.fill(ORDER_STATUS_.get(str(order.OIpaystatus)), 'order_status')
            order.OIpaytime = get_web_time_str(order.OIpaytime)
            order.OIcreatetime = get_web_time_str(order.OIcreatetime)
            # 买家
            usid = order.USid
            user = self.suser.get_user_by_user_id(usid)
            if user:
                if user.USlevel == 0:
                    user.level = 'ordinary'
                if user.USlevel > 0:
                    user.level = 'partner'
                user.add('level')
                order.fill(user, 'user')
            # 卖家
            upperusid = order.Sellerid
            upuser = self.suser.get_user_by_user_id(upperusid)
            if upuser:
                if upuser.USlevel == 0:
                    upuser.level = 'ordinary'
                if upuser.USlevel > 0:
                    upuser.level = 'partner'
                upuser.add('level')
                order.fill(upuser, 'upper')
        response = import_status('get_order_list_success', 'OK')
        response["count"] = request.all_count
        response["page_count"] = request.page_count
        response["data"] = order_list
        return response

    @verify_token_decorator
    def update_order(self):
        """没用"""
        if is_tourist():
            return TOKEN_ERROR
        parameter_required(*self.update_order_params)
        data = request.json
        orid = data.get('orid')
        oipaystatus = data.get("oipaystatus")
        update_result = self.sorder.update_orderinfo_status(orid, {"OIpaystatus": oipaystatus})
        if not update_result:
            raise SYSTEM_ERROR(u'数据库连接异常')
        # if oipaystatus:

    @verify_token_decorator
    def pay_order(self):
        """付款"""
        if is_tourist():
            raise TOKEN_ERROR()
        data = parameter_required(u'oiid')
        oiid = data.get('oiid')
        order = self.sorder.get_order_by_oiid(oiid)
        if not order or order.USid != request.user.id or order.OIpaystatus != 1:
            raise NOT_FOUND()
        openid = request.user.openid
        total_fee = order.OImount * 100
        oisn = order.OIsn  # 订单号
        raw = self.pay.jsapi(trade_type="JSAPI", openid=openid,
                             out_trade_no=oisn,
                             total_fee=int(total_fee),
                             spbill_create_ip=request.remote_addr)
        res = dict(raw)
        res['paySign'] = res.get('sign')
        data = import_status('messages_get_item_ok', res)
        return data

    def pay_callback(self):
        """支付回调"""
        data = self.pay.to_dict(request.data)
        from WeiDian.common.loggers import generic_log
        generic_log(data)
        if not self.pay.check(data):
            return self.pay.reply(u"签名验证失败", False)
        sn = data.get('out_trade_no')
        order = self.sorder.get_order_by_oisn(sn)
        if not order or order.OIpaystatus != 1:
            # 无效请求
            return self.pay.reply("OK", True)
        # 此处可能会放到确认收货的接口中
        order_owner = self.suser.get_user_by_user_id(order.USid)
        # 修改订单状态
        paytime = data.get('time_end')
        update_dict = {
            'OIpaystatus': 5,  # 待发货
            'OIpaytime': paytime,
            'OIpaytype': 1,  # 统一微信支付
        }
        # 如果存在上一级
        if order_owner and order_owner.UPPerd:
            try:
                uppid = order_owner.UPPerd
                update_dict['Sellerid'] = uppid
                # 记录销售额活动
                from WeiDian.service.SPartnerSellOrInviteMatch import SPartnerSellOrInviteMatch
                self.spartnermatch = SPartnerSellOrInviteMatch()
                match = self.spartnermatch.get_lasting_partner_match(1)  # 销售比赛, 不分等级
                # 如果活动在进行中
                if match:
                    match_item = self.spartnermatch.get_partner_match_mount_by_usidpsmid(uppid, match.PSIMid)
                    # 如果有此人上级的记录
                    if match_item:
                        from WeiDian.models.model import PartnerSellOrinviteMount
                        self.spartnermatch.update_partner_match_mount_by_psomid(match_item.PSOMid, {
                            'sellorinvitemount': PartnerSellOrinviteMount.sellorinvitemount + order.OImount
                        })
                    else:  # 无记录
                        add_mount = {
                            'PSOMid': str(uuid.uuid4()),
                            'USid': order_owner.UPPerd,
                            'sellorinvitemount': order.OImount,
                            'PSIMid': match.PSIMid
                        }
                        self.spartnermatch.add_model('PartnerSellOrinviteMount', add_mount)
            except Exception as e:
                generic_log(e, 'paycall_back_error')
        updated = self.sorder.update_orderinfo_by_oisn(sn, update_dict)
        return self.pay.reply("OK", True)

    def get_kd_list(self):
        data = request.args.to_dict()
        response = import_status('get_success', 'OK')
        from WeiDian.config.kd import kd_list
        kw = data.get('kw', '').strip()
        if not kw:
            response['kd_list'] = kd_list
            return response
        if not isinstance(kw, basestring):
            kw = str(kw).encode('utf8')
        elif isinstance(kw, unicode):
            kw = kw.encode('utf8')
        res = filter(lambda x: kw in x.get('expressname'), kd_list)
        response['kd_list'] = res
        return response

    @verify_token_decorator
    def send_order(self):
        """发货, 发货的的对象是订单中的商品而不是订单"""
        if not is_admin():
            raise TOKEN_ERROR(u'使用管理员登录')
        data = parameter_required(u'send_infos')
        send_infos = data.get('send_infos')
        if not isinstance(send_infos, list) or not send_infos:
            raise PARAMS_MISS(u'发货参数格式错误')
        order_info_list = []
        kd_company_list = [x['expresskey'] for x in kd_list]
        with self.sorder.auto_commit() as session:
            session_list = []
            for send_info in send_infos:
                opiid = send_info.get('opiid')  # 订单中的详情id
                opilogisticssn = send_info.get('opilogisticssn')  # 运单号
                kdcompany = send_info.get('kdcompany')  # 物流公司
                # 判断参数
                if kdcompany not in kd_company_list:
                    raise PARAMS_MISS(u'不正确的快递公司{}'.format(kdcompany))
                if not opiid or not opilogisticssn or not kdcompany:
                    raise PARAMS_MISS(u'缺少opiid或者opilogisticssn或者kdcompany')
                # 改变订单商品状态
                opilogisticssn = opilogisticssn
                order_product = session.query(OrderProductInfo).filter(
                        OrderProductInfo.OPIid == opiid
                ).first()
                if not order_product:
                    raise PARAMS_MISS(u'不存在的订单商品详情: {}'.format(opiid))
                if order_product.OPIstatus != 0:
                    raise PARAMS_MISS(u'重复发货: {}'.format(opiid))
                order_product.OPIlogisticsSn = opilogisticssn
                order_product.OPIlogisticsCompnay = kdcompany
                order_product.OPIstatus = 1
                now_time = datetime.now()
                order_product.OPIresendLogistictime = datetime.strftime(now_time, format_for_db)
                session_list.append(order_product)
                # 改变订单状态
                oiid = order_product.OIid
                order = session.query(OrderInfo).filter(OrderInfo.OIid == oiid).first()
                if not order:
                    raise PARAMS_MISS(u'不存在的订单')
                if order.OIpaystatus == 1:
                    raise PARAMS_MISS(u'未付款的订单')
                if order not in order_info_list:
                    order.OIpaystatus = 5
                    session_list.append(order)
                    order_info_list.append(order)
            session.add_all(session_list)
        response = import_status('send_product_success', 'OK')
        return response

    @verify_token_decorator
    def confim_order(self):
        """确认收货"""
        if is_tourist():
            raise TOKEN_ERROR()
        data = parameter_required(u'oiid')
        oiid = data.get('oiid')
        order = self.sorder.get_order_by_oiid(oiid)
        if not order or order.USid != request.user.id:
            raise NOT_FOUND()
        if order.OIpaystatus not in [5, 12]:
            raise NOT_FOUND(u'订单未发货或已收货')
        order_product_list = self.sorder.get_orderproductinfo_by_oiid(oiid)
        with self.sorder.auto_commit() as session:
            if len(filter(lambda x: x.OPIstatus in [0], order_product_list)):
                raise PARAMS_MISS(u'部分商品未发货')
            # 判断订单中的所有商品是否都已经完成, 如果已经完成则更改订单状态为交易成功
            session.query(OrderInfo).filter(OrderInfo.OIid == oiid).update({
                'OIpaystatus': 6  # 交易完成
            })
            session.query(OrderProductInfo).filter(OrderProductInfo.OIid == oiid).update({
                'OPIstatus': 2  # 已发货
            })
            # 上级福利

        response = import_status('confirm_order_success', 'OK')
        return response

    @verify_token_decorator
    def apply_refund(self):
        """申请退货(换货)"""
        if is_tourist():
            raise TOKEN_ERROR(u'请登录')
        data = parameter_required(u'opiid', u'oprreason', u'oprtype')
        opiid = data.get('opiid')
        OPRtype = data.get('oprtype')
        if OPRtype not in [0, 1]:
            raise PARAMS_MISS(u'参数错误')
        usid = request.user.id
        order_product = self.sorder.get_orderproductinfo_by_opiid(opiid)
        if not order_product:
            raise NOT_FOUND(u'不存在的订单商品')
        oiid = order_product.OIid
        order = self.sorder.get_order_by_oiid(oiid)
        if not order or order.USid != usid:
            raise NOT_FOUND(u'不存在订单')
        if order.OIpaystatus == 1:
            raise NOT_FOUND(u'未付款的订单')
        already_apply = self.sorder.get_orderproduct_resend_by_opiid(opiid)
        if already_apply:
            raise DumpliError()
        with self.suser.auto_commit() as session:
            session_list = []
            # 创建退款记录
            voucher_images = data.get('oprimage')
            oprmount = data.get('oprmount')
            if oprmount > order_product.SmallTotal or oprmount is None:
                oprmount = order_product.SmallTotal
            model_dict = {
                'OPRid': str(uuid.uuid4()),
                'OPRsn': self._geceric_sn(),
                'OPIid': opiid,
                'OPRtype': OPRtype,
                'OPRreason': data.get('oprreason'),
                'OPRdesc': data.get('oprdesc'),
                'OPRimage': json.dumps(voucher_images)
            }
            msg = u'申请换货成功'
            if OPRtype == 0:
                # 退货退款
                model_dict['OPRmount'] = oprmount
                msg = u'申请退货成功'
            new_resend = OrderProductResend()
            [setattr(new_resend, k, v) for k, v in model_dict.items() if v is not None]
            session_list.append(new_resend)
            # # 更改商品详情状态   不需要改, 需要记住以前的状态
            # session.query(OrderProductInfo).filter(OrderProductInfo.OPIid == opiid).update({
            #     'OPIstatus': OPIstatus
            # })
            # 更改订单状态
            session.query(OrderInfo).filter(OrderInfo.OIid == oiid).update({
                'OIpaystatus': 11
            })
            session.add_all(session_list)
        response = {"message": msg, "status": 200}
        return response

    @verify_token_decorator
    def agree_refund(self):
        """同意退货"""
        if not is_admin():
            raise TOKEN_ERROR(u'请使用管理员登录')
        data = parameter_required(u'opiid')
        agree = data.get('agree', 1)
        opiid = data.get('opiid')
        order_product_info = self.sorder.get_orderproductinfo_by_opiid(opiid)
        if not order_product_info:
            raise NOT_FOUND(u'不存在的订单')
        order_product_resend = self.sorder.get_orderproduct_resend_by_opiid(opiid)
        if not order_product_resend or order_product_resend.OPRschedule != 0:
            raise DumpliError(u'未申请或已处理')
        # 判断状态
        if agree == 1:
            with self.sorder.auto_commit() as session:
                # 更改退款表状态
                session.query(OrderProductResend).filter(
                        OrderProductResend.OPIid == opiid
                ).update({'OPRschedule': 1})
            msg = '同意退货, 等待买家发货'
        elif agree == 0:
            with self.sorder.auto_commit() as session:
                session.query(OrderProductResend).filter(
                        OrderProductResend.OPIid == opiid
                ).update({'OPRschedule': 5})
            msg = '拒绝成功'
        response = {"message": msg, "status": 200}
        return response

    def buyser_send_out(self):
        """买家发货"""
        if is_tourist():
            raise TOKEN_ERROR(u'请登录')
        data = parameter_required(u'opiid')
        order_product_resend = self.sorder.get_orderproduct_resend_by_opiid(opiid)
        if not order_product_resend:
            raise NOT_FOUND(u'未申请')


    def fix_orderproduct_info(self, sku_list, oiid):
        """
        调整参数以可以持久化到orderproductinfo表
        sku_list: 客户端请求中的sku列表:"sku":{[pskid:..., num: 2], [pskid: ..., num:2]}
        oiid: 订单id
        return: 返回一个可以使用list_to_model的字典列表
        字典中的key有: opiid, oiid, pskproperkey, opiproductname,
                        opiproductimages, opiproductnum, opiproductprice
       """
        sku_dict_list = []
        for sku in sku_list:
            pskid = sku.get('pskid')
            productskukey = self.sproductskukey.get_psk_by_pskid(pskid)
            if not productskukey:
                raise NOT_FOUND(u'不存在sku')
            prid = productskukey.PRid
            product = self.sproduct.get_product_by_prid(prid)
            if not product:
                raise NOT_FOUND(u'商品不存在')
            orderproductinfo_dict = dict(
                opiid=str(uuid.uuid4()),
                oiid=oiid,
                prid=prid,
                PSKproperkey=productskukey.PSKproperkey,  # 商品属性组合(sku)
            )
            orderproductinfo_dict['opiproductname'] = product.PRname
            orderproductinfo_dict['opiproductimages'] = product.PRmainpic
            orderproductinfo_dict['opiproductnum'] = int(sku.get('num', 1))
            orderproductinfo_dict['OIproductprice'] = self.sproductskukey.get_true_price(pskid, partner=is_partner())
            orderproductinfo_dict['SmallTotal'] = self.sproductskukey.get_true_price(pskid, partner=is_partner()) *\
                                                            orderproductinfo_dict['opiproductnum']
            sku_dict_list.append(orderproductinfo_dict)
        return sku_dict_list

    def fill_productinfo(self, order):
        oiid = order.OIid
        productinfos = self.sorder.get_orderproductinfo_by_oiid(oiid)
        order.productinfo = productinfos
        for productinfo in productinfos:
            productinfo.fields = ['OPIproductname', 'OPIproductimages', 'OPIstatus', 'OPIid', 'PRid', 'PSKproperkey', 'OIproductprice', 'OPIproductnum', 'SmallTotal']
            productinfo.OPIlogisticstime = get_web_time_str(productinfo.OPIlogisticstime)
            productinfo.fill(order.OIsn, 'oisn')
            # 0: 待发货, 1 待收货, 2 交易成功(未评价), 3 交易成功(已评价), 4 已签收'
            if productinfo.OPIstatus != 0:
                # 发货信息
                productinfo.add('OPIlogisticsSn', 'OPIlogisticsCompnay', 'OPIlogisticsText', 'OPIlogisticstime')
                send_time = productinfo.OPIlogisticstime
                if send_time:
                    productinfo.OPIresendLogistictime = get_web_time_str(send_time)
                logistic_name = self.get_current_kd(productinfo.OPIlogisticsCompnay)
                if logistic_name:
                    productinfo.fill(logistic_name, 'zh_logistic_compnay')
                if productinfo.OPIlogisticsText:
                    productinfo.OPIlogisticsText = json.loads(productinfo.OPIlogisticsText)
                productinfo.fill(False, 'resend')
            # 退货信息
            product_resend = self.sorder.get_orderproduct_resend_by_opiid(productinfo.OPIid)
            if product_resend:  # 退换货, 需要查询退换货表
                product_resend = self.sorder.get_orderproduct_resend_by_opiid(productinfo.OPIid)
                product_resend.fields = product_resend.all
                product_resend.zh_OPRschedule = OrderResend.get(product_resend.OPRschedule)
                product_resend.zh_OPRtype = OrderResendType.get(product_resend.OPRtype)
                product_resend.add('zh_OPRtype', 'zh_OPRschedule')
                productinfo.fill(True, 'resend')

            productinfo.fill(order_product_info_status.get(productinfo.OPIstatus, u'异常'), 'zh_status')
        order.add('productinfo')
        return order

    def fill_complainstatus(self, order):
        oiid = order.OIid
        complainstatus = self.scomplain.get_complain_by_oiid(oiid)
        if complainstatus:
            complainstatus.fields = ['COtreatstatus']
            order.complainstatus = complainstatus
        else:
            order.complainstatus = {"cotreatstatus": 0}
        order.add('complainstatus')
        return order

    @staticmethod
    def _geceric_sn():
        return datetime.strftime(datetime.now(), format_for_db) + str(random.randint(10000, 100000))

    @staticmethod
    def get_current_kd(alias):
        for kd in kd_list:
            if kd.get('expresskey') == alias:
                return kd.get('expressname')

    

