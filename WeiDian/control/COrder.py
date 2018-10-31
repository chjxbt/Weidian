# -*- coding:utf8 -*-
import json
import sys
import os
import uuid
import random
from datetime import datetime
from decimal import Decimal

from weixin import WeixinPay
from flask import request

from WeiDian import logger
from WeiDian.common.divide import Partner
from WeiDian.common.loggers import generic_log
from WeiDian.common.params_require import parameter_required, validate_phone
from WeiDian.config.enums import ORDER_STATUS, order_product_info_status, ORDER_STATUS_, OrderResend, OrderResendType
from WeiDian.config.kd import kd_list
from WeiDian.config.setting import QRCODEHOSTNAME, APP_ID, MCH_ID, MCH_KEY, notify_url
from WeiDian.common.timeformat import format_for_db, get_web_time_str
from WeiDian.common.token_required import verify_token_decorator, is_partner, is_admin
from WeiDian.common.import_status import import_status
from WeiDian.control.CRaward import CRaward
from WeiDian.models.model import OrderProductInfo, OrderInfo, OrderProductResend, UserRaward, OrderProductSendTwice, \
    RewardTransfer, Raward, UserCommisionPriview, UserCommision, UserCommisionFlow
from WeiDian.service.SOrder import SOrder
from WeiDian.service.SProductImage import SProductImage
from WeiDian.service.SProductSkuKey import SProductSkuKey
from WeiDian.service.SProduct import SProduct
from WeiDian.service.SComplain import SComplain
from WeiDian.service.SUser import SUser
from WeiDian.config.response import PARAMS_MISS, SYSTEM_ERROR, AUTHORITY_ERROR, TOKEN_ERROR, NOT_FOUND, DumpliError, \
    PARAMS_ERROR
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
            # 建立订单
            model_beans = []
            order_dict = dict(
                OIid=str(uuid.uuid4()),
                USid=usid,
                OIsn=self._geceric_sn(),
                OIleavetext=data.get('oileavetext') or '',
                OIaddress=data.get('oiaddress'),
                OIrecvname=data.get('oirecvname'),
                OIrecvphone=data.get('oirecvphone'),
                Sellerid=request.user.UPPerd
            )
            # 建立订单详情
            sku = data.get('sku')
            orderproductinfo_dict_list, commission_list = self.fix_orderproduct_info(sku, order_dict['OIid'])
            for order_product in orderproductinfo_dict_list:
                orderproduct_instance = OrderProductInfo.create(order_product)
                model_beans.append(orderproduct_instance)
            for commsion in commission_list:
                user_commsion_instance = UserCommisionPriview.create(commsion)
                model_beans.append(user_commsion_instance)
            OImount= sum([Decimal(x['SmallTotal']) for x in orderproductinfo_dict_list])
            # 判断优惠券
            urid = data.get('urid')
            if urid:
                raward_type = self._raward_can_use(urid, OImount)
                if raward_type == 'is_gift':
                    gift = session.query(RewardTransfer).filter(RewardTransfer.RFid == urid).first()
                    gift.RFstatus = 2
                    gift.RFusetime = datetime.strftime(datetime.now(), format_for_db)
                    raid = gift.RAid
                    model_beans.append(gift)
                elif raward_type == 'is_own':
                    user_raward = session.query(UserRaward).filter(UserRaward.URid == urid).first()
                    user_raward.RAnumber -= 1
                    raid = user_raward.RAid
                    model_beans.append(user_raward)
                else:
                    pass
                raward = session.query(Raward).filter(Raward.RAid == raid).first()
                OImount -= raward.RAamount
                order_dict['RAid'] = raid
            order_dict['OImount'] = float(OImount)  # 总价
            orderinfo = OrderInfo.create(order_dict)
            model_beans.append(orderinfo)
            session.add_all(model_beans)
        data = import_status('add_order_success', 'OK')
        data['data'] = {
            'oiid': order_dict['OIid']
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
        # total_fee = order.OImount * 100
        total_fee = 1
        oisn = order.OIsn  # 订单号
        raw = self.pay.jsapi(trade_type="JSAPI", openid=openid,
                             out_trade_no=oisn,
                             total_fee=int(total_fee),
                             spbill_create_ip=request.remote_addr,
                             body='1234')
        res = dict(raw)
        res['paySign'] = res.get('sign')
        data = import_status('messages_get_item_ok', 'OK')
        data['data'] = res
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
        # todo 二三级合伙人升级操作
        if not is_admin():
            biglist = filter(self.check_big, order_product_list)  # 校验订单是否包含大礼包
            self.upgrade_user(data, biglist)  # 如果是大礼包而且当前用户不是店主，则升级为初级合伙人，并且指派上级
        # todo 团队佣金累加计算 按月累计 逻辑有问题待重新规划

        with self.sorder.auto_commit() as session:
            if len(filter(lambda x: x.OPIstatus in [0], order_product_list)):
                raise PARAMS_MISS(u'部分商品未发货')
            add_list = []
            # 判断订单中的所有商品是否都已经完成, 如果已经完成则更改订单状态为交易成功
            session.query(OrderInfo).filter(OrderInfo.OIid == oiid).update({
                'OIpaystatus': 6  # 交易完成
            })
            session.query(OrderProductInfo).filter(OrderProductInfo.OIid == oiid).update({
                'OPIstatus': 2  # 交易成功
            })
            # 佣金到帐 开店上级佣金
            order_products = session.query(OrderProductInfo).filter(OrderProductInfo.OIid == oiid).all()
            for order_product in order_products:
                user_commsion_previews = session.query(UserCommisionPriview).filter(
                    UserCommisionPriview.OPIid == order_product.OPIid,
                    UserCommisionPriview.UCPstatus == 0,
                    UserCommisionPriview.UCtype == 0,
                ).all()  # 预估佣金
                for user_commsion_preview in user_commsion_previews:
                    user_commsion_preview.UCPstatus = 10  # 设置为已到帐
                    usid = user_commsion_preview.USid
                    user_commsion = session.query(UserCommision).filter(UserCommision.USid == usid).first()
                    if user_commsion:
                        user_commsion.UCnum += user_commsion_preview.UCPnums
                        user_commsion.UCtotal += user_commsion_preview.UCtotal
                    else:
                        new_user_commsion = UserCommision.create({
                            'UCid': str(uuid.uuid4()),
                            'USid': usid,
                            'UCnum': user_commsion_preview.UCPnums
                        })  # 佣金到帐
                        add_list.append(new_user_commsion)
                    # 佣金流水表
                    new_commsion_flow = UserCommisionFlow.create({
                        'UCfid': str(uuid.uuid4()),
                        'UCFnums': user_commsion_preview.UCPnums,
                        'USid': usid
                    })
                    add_list.append(new_commsion_flow)

                user_commsion_previews = session.query(UserCommisionPriview).filter(
                    UserCommisionPriview.OPIid == order_product.OPIid,
                    UserCommisionPriview.UCPstatus == 0,
                    UserCommisionPriview.UCtype == 1,
                ).all()  # 预估专粉佣金
                for user_commsion_preview in user_commsion_previews:
                    user_commsion_preview.UCPstatus = 10  # 设置为已到帐
                    usid = user_commsion_preview.USid
                    user_commsion = session.query(UserCommision).filter(UserCommision.USid == usid).first()
                    if user_commsion:
                        user_commsion.UCnum += user_commsion_preview.UCPnums
                        user_commsion.UCtotal += user_commsion_preview.UCtotal
                    else:
                        new_user_commsion = UserCommision.create({
                            'UCid': str(uuid.uuid4()),
                            'USid': usid,
                            'UCnum': user_commsion_preview.UCPnums
                        })  # 佣金到帐
                        add_list.append(new_user_commsion)
                    # 佣金流水表
                    new_commsion_flow = UserCommisionFlow.create({
                        'UCfid': str(uuid.uuid4()),
                        'UCFnums': user_commsion_preview.UCPnums,
                        'USid': usid,
                        'UCFtype': 20
                    })
                    add_list.append(new_commsion_flow)

            session.add_all(add_list)

        response = import_status('confirm_order_success', 'OK')
        return response

    @verify_token_decorator
    def apply_refund(self):
        """申请退货(换货)"""
        if is_tourist():
            raise TOKEN_ERROR(u'请登录')
        # data = parameter_required(u'opiid', u'oprreason', u'oprtype')
        data = parameter_required(u'opiid', u'oprtype')
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
            model_dict = {
                'OPRid': str(uuid.uuid4()),
                'OPRsn': self._geceric_sn(),
                'OPIid': opiid,
                'OPRtype': OPRtype,
            }
            # model_dict = {k: v for k, v in model_dict.items() if v}
            msg = u'申请换货成功'
            if OPRtype == 1 and order_product.OPIstatus == 0:
                raise NOT_FOUND(u'未发货无法申请换货')
            if OPRtype == 0:
                # 退货退款
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
        data = parameter_required(u'opiid', u'oprreceiverphone', u'oprreceiveraddress', u'oprreceivername')
        agree = data.get('agree', 1)
        opiid = data.get('opiid')
        order_product_info = self.sorder.get_orderproductinfo_by_opiid(opiid)
        if not order_product_info:
            raise NOT_FOUND(u'不存在的订单')
        order_product_resend = self.sorder.get_orderproduct_resend_by_opiid(opiid)
        if not order_product_resend or order_product_resend.OPRschedule != 0:
            raise DumpliError(u'未申请或已处理')
        phone = validate_phone(data.get('oprreceiverphone'))
        update_dict = {
            'OPRreceivername': data.get('oprreceivername'),
            'OPRreceiverphone': phone,
            'OPRreceiveraddress': data.get('oprreceiveraddress'),
        }
        # 判断状态
        if agree == 1:
            with self.sorder.auto_commit() as session:
                # 更改退款表状态
                # 如果未发货, 可以直接退款
                update_dict['OPRschedule'] = 1
                # 预估佣金不可用
                session.query(UserCommisionPriview).filter(UserCommisionPriview.OPIid == opiid).update({
                    'UCPstatus': 20
                })
                msg = '同意退货, 等待买家发货'
                if order_product_info.OPIstatus == 0:  # 如果商品并未发货
                    update_dict['OPRschedule'] = 5  # 完成
                    # todo 退款方法
                    self._refund()
                    msg = '已执行退款'
                session.query(OrderProductResend).filter(
                        OrderProductResend.OPIid == opiid
                ).update(update_dict)
        elif agree == 0:
            with self.sorder.auto_commit() as session:
                update_dict['OPRschedule'] = 6
                session.query(OrderProductResend).filter(
                        OrderProductResend.OPIid == opiid
                ).update(update_dict)
                msg = '拒绝成功'
        else:
            raise PARAMS_MISS()
        response = {"message": msg, "status": 200}
        return response

    @verify_token_decorator
    def buyer_send_out(self):
        """买家发货"""
        if is_tourist():
            raise TOKEN_ERROR(u'请登录')
        # data = parameter_required(u'opiid', u'oprresendlogisticcompnay', u'oprresendlogisticsn', u'oprreceivername', u'oprreceiverphone', u'oprreceiveraddress')
        data = parameter_required(u'opiid', u'oprresendlogisticcompnay', u'oprresendlogisticsn',)
        opiid = data.get('opiid')
        order_product_resend = self.sorder.get_orderproduct_resend_by_opiid(opiid)
        if not order_product_resend:
            raise NOT_FOUND(u'未申请')
        if order_product_resend.OPRschedule != 1:
            raise NOT_FOUND(u'请勿重新发货')
        kd_company_list = [x['expresskey'] for x in kd_list]
        kd_company = data.get('oprresendlogisticcompnay')
        if kd_company not in kd_company_list:
            raise PARAMS_ERROR(u'不正确的快递公司')
        oprid = order_product_resend.OPRid
        voucher_images = data.get('oprimage')
        update_dict = {
            'OPRresendLogisticCompany': data.get('oprresendlogisticcompnay'),
            'OPRresendLogisticSn': data.get('oprresendlogisticsn'),
            'OPRresendLogistictime': datetime.now(),
            'OPRreceivername': data.get('oprreceivername'),
            'OPRreceiverphone': data.get('oprreceiverphone'),
            'OPRschedule': 2,  # 3: 买家已发货
            'OPRreceiveraddress': data.get('oprreceiveraddress'),
            'OPRreason': data.get('oprreason'),
            'OPRdesc': data.get('oprdesc'),
            'OPRimage': json.dumps(voucher_images)
        }

        oprmount = data.get('oprmount')
        order_product = self.sorder.get_orderproductinfo_by_opiid(opiid)
        if oprmount is None or oprmount > order_product.SmallTotal:
            oprmount = order_product.SmallTotal
        if order_product_resend.OPRtype == 0:
            # 退货退款
            update_dict['OPRmount'] = oprmount
        update_dict = {k: v for k, v in update_dict.items() if v is not None}
        updated = self.sorder.update_order_product_resend_by_oprid(oprid, update_dict)
        msg = '发货成功'
        response = {'message': msg, 'status': 200}
        return response

    @verify_token_decorator
    def solder_confirm(self):
        """卖家确认收货"""
        if not is_admin():
            raise TOKEN_ERROR(u'请使用管理员登录')
        data = parameter_required(u'opiid')
        # 如果为退款, 则直接退款；如果为换货, 则进入卖家发货中
        opiid = data.get('opiid')
        order_product_resend = self.sorder.get_orderproduct_resend_by_opiid(opiid)
        if not order_product_resend:
            raise NOT_FOUND()
        with self.sorder.auto_commit() as session:
            if order_product_resend.OPRtype == 0:
                # 退货
                session.query(OrderProductResend).filter(OrderProductResend.OPIid == opiid).update({
                    'OPRschedule': 5
                })
                msg = '退款处理中'
                # todo 退款操作
                self._refund()
            elif order_product_resend.OPRtype == 1:
                # 换货
                session.query(OrderProductResend).filter(OrderProductResend.OPIid == opiid).update({
                    'OPRschedule': 3
                })
                msg = '等待卖家发货'
            else:
                raise SYSTEM_ERROR()
        response = {'message': msg, 'status': 200}
        return response

    @verify_token_decorator
    def solder_change_send(self):
        """卖家换货发货"""
        if not is_admin():
            raise TOKEN_ERROR(u'请使用管理员登录')
        data = parameter_required(u'opiid', u'opssendsn', u'opssendlogisticcompany', u'opsreceivername', u'opsreceivephone', u'opsreceiveaddress')
        opiid = data.get('opiid')
        order_product_resend = self.sorder.get_orderproduct_resend_by_opiid(opiid)
        if not order_product_resend:
            raise NOT_FOUND()
        if order_product_resend.OPRtype == 0:
            raise NOT_FOUND(u'非换货订单')
        if order_product_resend.OPRschedule != 3:
            raise NOT_FOUND(u'请先确认收货')
        oprid = order_product_resend.OPRid
        with self.sorder.auto_commit() as session:
            alreadysend = session.query(OrderProductSendTwice).filter(
                OrderProductSendTwice.OPRid == oprid
            ).first()
            if alreadysend:
                raise DumpliError(u'重复发货')
            kd_company_list = [x['expresskey'] for x in kd_list]
            kd_company = data.get('opssendlogisticcompany')
            if kd_company not in kd_company_list:
                raise PARAMS_ERROR(u'不正确的快递公司')
            # 添加记录
            model_dict = {
                'OPSid': str(uuid.uuid4()),
                'OPRid': oprid,
                'OPSsendsn': data.get('opssendsn'),
                'OPSsendLogisticCompany': kd_company,
                'OPSreceivername': data.get('opsreceivername'),
                'OPSreceivephone': data.get('opsreceivephone'),
                'OPSreceiveaddress': data.get('opsreceiveaddress')
            }
            opst = OrderProductSendTwice.create(model_dict)
            # 改变状态
            session.query(OrderProductResend).filter(
                OrderProductResend.OPRid == oprid
            ).update(
                {'OPRschedule': 4}  # 4: 卖家已发货
            )
            session.add(opst)
        response = {'message': u'卖家换货发货成功', 'status': 200}
        return response

    def buyer_confirm_again(self):
        """买家再次确认收货"""
        if is_tourist():
            raise TOKEN_ERROR(u'请登录')
        data = parameter_required(u'opiid')
        opiid = data.get('opiid')
        order_product_resend = self.sorder.get_orderproduct_resend_by_opiid(opiid)
        if not order_product_resend:
            raise NOT_FOUND()
        if order_product_resend.OPRtype == 0:
            raise NOT_FOUND(u'非换货订单')
        if order_product_resend.OPRschedule != 4:
            raise NOT_FOUND(u'卖家未发货或已经确认')
        oprid = order_product_resend.OPRid
        with self.sorder.auto_commit() as session:
            session.query(OrderProductResend).filter(
                OrderProductResend.OPRid == oprid
            ).update({
                'OPRschedule': 5  # 完成
            })
        response = {'message': u'确认收货成功, 交易完成', 'status': 200}
        return response

    @verify_token_decorator
    def delete_order(self):
        """删除订单"""
        if is_tourist():
            raise TOKEN_ERROR(u'请登录')
        data = parameter_required(u'oiid')
        oiid = data.get('oiid')
        order = self.sorder.get_order_by_oiid(oiid)
        usid = request.user.id
        if not order:
            raise NOT_FOUND(u'不存在的订单')
        if order.USid != usid and not is_admin():
            raise NOT_FOUND(u'他人订单')
        if order.OIpaystatus not in [1, 7, 6, 11]:
            raise NOT_FOUND(u'订单未完成, 不可删除')
        updated = self.sorder.update_order_by_oiid(oiid, {
            'OIisdelete': True
        })
        response = {'message': u'删除成功', 'status': 200}
        return response

    @verify_token_decorator
    def cancle_order(self):
        """取消订单, 只有未付款的才可以取消"""
        if is_tourist():
            raise TOKEN_ERROR(u'请登录')
        data = parameter_required(u'oiid')
        oiid = data.get('oiid')
        order = self.sorder.get_order_by_oiid(oiid)
        usid = request.user.id
        if not order:
            raise NOT_FOUND(u'不存在的订单')
        if order.USid != usid and not is_admin():
            raise NOT_FOUND(u'他人订单')
        if order.OIpaystatus != 1:
            raise NOT_FOUND(u'只可取消待付款的订单')
        updated = self.sorder.update_order_by_oiid(oiid, {
            'OIpaystatus': 7
        })
        response = {'message': u'取消成功', 'status': 200}
        return response

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
        commission_list = []
        for sku in sku_list:
            pskid = sku.get('pskid')
            productskukey = self.sproductskukey.get_psk_by_pskid(pskid)
            if not productskukey:
                raise NOT_FOUND(u'不存在sku')
            profict = Decimal(str(productskukey.PSKprofict or 5))  # 利润默认5
            prid = productskukey.PRid
            product = self.sproduct.get_product_by_prid(prid)
            if not product:
                raise NOT_FOUND(u'商品不存在')
            orderproductinfo_dict = dict(
                OPIid=str(uuid.uuid4()),
                OIid=oiid,
                PRid=prid,
                PSKproperkey=productskukey.PSKproperkey,  # 商品属性组合(sku)
            )
            orderproductinfo_dict['OPIproductname'] = product.PRname
            orderproductinfo_dict['OPIproductimages'] = product.PRmainpic
            orderproductinfo_dict['OPIproductnum'] = int(sku.get('num', 1))
            true_price = Decimal(str(self.sproductskukey.get_true_price(pskid, partner=is_partner())))
            orderproductinfo_dict['OIproductprice'] = float(round(true_price, 2))
            orderproductinfo_dict['SmallTotal'] = float(round(true_price * orderproductinfo_dict['OPIproductnum'], 2))
            sku_dict_list.append(orderproductinfo_dict)
            # 三级佣金计算
            commission = self._caculate_commison_by_profit(profict, request.user.id, orderproductinfo_dict['OPIid'], orderproductinfo_dict['OPIproductnum'])
            commission_list.extend(commission)
        return sku_dict_list, commission_list

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
                product_resend.fields = product_resend.all
                product_resend.zh_OPRschedule = OrderResend.get(product_resend.OPRschedule)
                product_resend.zh_OPRtype = OrderResendType.get(product_resend.OPRtype)
                product_resend.OPRimage = json.loads(product_resend.OPRimage)
                product_resend.add('zh_OPRtype', 'zh_OPRschedule')
                productinfo.fill(True, 'resend')
                productinfo.fill(product_resend, 'product_resend')
                logistic_name = self.get_current_kd(product_resend.OPRresendLogisticCompany)
                if logistic_name:
                    product_resend.fill(logistic_name, 'zh_logistic_compnay')
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

    def _refund(self):
        pass

    def _raward_can_use(self, urid, total_price):
        """返回是否可以使用"""
        reward = self.sraward.is_user_hold_reward({'URid': urid})
        gift = self.sraward.is_user_hold_reward_in_gift(
            {'RFid': urid, 'RFstatus': 1})
        craward = CRaward()
        if reward:
            reward_detail = self.sraward.get_raward_by_id(reward.RAid)
            if not reward_detail:
                raise NOT_FOUND(u'该优惠券不存在或已失效')
            reward_detail = craward.fill_reward_detail(reward_detail, total_price)
            reward.fill(reward_detail, 'reward_detail')
            reward = dict(reward)
            lower_reward = {}
            for i, j in reward.items():
                lower_reward[i.lower()] = j
            lower_reward['urcreatetime'] = get_web_time_str(lower_reward.get('urcreatetime'))
            res = lower_reward
        elif gift:
            reward_info = self.sraward.get_raward_by_id(gift.RAid)
            if not reward_info:
                raise NOT_FOUND(u'该优惠券不存在或已失效')
            gift = craward.fill_transfer_detail(gift)
            gift_detail = self.sraward.get_raward_by_id(gift.RAid)
            gift_detail = craward.fill_reward_detail(gift_detail, total_price)
            # 检验转赠券在各情况下的有效性
            gift_detail.valid = gift_detail.valid and gift.transfer_valid
            gift.fill(gift_detail, 'reward_detail')
            gift.RFcreatetime = get_web_time_str(gift.RFcreatetime)
            gift.RFendtime = get_web_time_str(gift.RFendtime)
            gift_dict = {
                'urid': gift.RFid,
                'usid': gift.USid,
                'raid': gift.RAid,
                'ranumber': gift.RAnumber,
                'urcreatetime': gift.RFcreatetime,
                'reendtime': gift.RFendtime,
                'rffrom': gift.RFfrom,
                'rfstatus': gift.RFstatus,
                'urusetime': gift.RFusetime,
                'remarks': gift.remarks,
                'tag': gift.tag,
                'usheader': gift.usheader,
                'reward_detail': gift.reward_detail
            }
            res = gift_dict
        else:
            raise NOT_FOUND(u'不存在的优惠券')
        can_use = res.get('reward_detail')['RAtype'] in [0, 2] and \
               res.get('ranumber') != 0 and \
               res.get('reward_detail')['valid'] == True
        if not can_use:
            raise NOT_FOUND(u'优惠券不可使用')
        return 'is_gift' if gift else 'is_own'

    def _caculate_commison_by_profit(self, profict, usid, opiid, nums):
        # 佣金收益计算
        user = self.suser.get_user_by_user_id(usid)
        profict = Decimal(str(profict * nums))
        p = Partner()
        commissions = []
        if user and user.UPPerd:
            # 专粉佣金计算
            user_order_count = self.sorder.get_sell_ordercount_by_item_status(usid)
            commission_without_ordercount = profict * Decimal(str(p.one_level_divide))  # 上一级佣金, 未根据订单数量加成
            commsion_price = self._caculate_devite_rate(commission_without_ordercount, user_order_count)
            commsion_dict = {
                'UCPid': str(uuid.uuid4()),
                'OPIid': opiid,
                'USid': user.UPPerd,
                'UCPnums': commsion_price,
                'UCtype': 1
            }
            commissions.append(commsion_dict)

            if not user.USshopkeeper:
                return commissions
            # 三级佣金计算
            # commsion_price = commission_without_ordercount
            commsion_dict = {
                'UCPid': str(uuid.uuid4()),
                'OPIid': opiid,
                'USid': user.USshopkeeper,
                'UCPnums': commission_without_ordercount,
            }
            commissions.append(commsion_dict)
            user_upperd = self.suser.get_user_by_user_id(user.UPPerd)
            if user_upperd and user_upperd.UPPerd:
                commission_without_ordercount = profict * Decimal(str(p.two_level_divide))  # 上两级级佣金, 未根据订单数量加成
                # commsion_price = self._caculate_devite_rate(commission_without_ordercount, user_order_count)
                commsion_dict = {
                    'UCPid': str(uuid.uuid4()),
                    'OPIid': opiid,
                    'USid': user_upperd.USshopkeeper,
                    'UCPnums': commission_without_ordercount,
                }
                commissions.append(commsion_dict)
                user_upper_s_upperd = self.suser.get_user_by_user_id(user_upperd.UPPerd)
                if user_upper_s_upperd and user_upper_s_upperd.UPPerd:
                    commission_without_ordercount = profict * Decimal(str(p.three_level_divide))  # 上3级佣金, 未根据订单数量加成
                    # commsion_price = self._caculate_devite_rate(commission_without_ordercount, user_order_count)
                    commsion_dict = {
                        'UCPid': str(uuid.uuid4()),
                        'OPIid': opiid,
                        'USid': user_upperd.USshopkeeper,
                        'UCPnums': commission_without_ordercount,
                    }
                    commissions.append(commsion_dict)

        return commissions

    @staticmethod
    def _caculate_devite_rate(item, user_order_count):
        if not user_order_count:
            user_order_count = 0
        p = Partner()
        level1_max = p.get_item('level_limit_1', 'max')
        level1_min = p.get_item('level_limit_1', 'min')
        level2_max = p.get_item('level_limit_2', 'max')
        level2_min = p.get_item('level_limit_2', 'min')

        if int(level1_min) <= user_order_count <= int(level1_max):
            level_rate = p.get_item('level_limit_1', 'profit')
        elif int(level2_min) <= user_order_count <= int(level2_max):
            level_rate = p.get_item('level_limit_2', 'profit')
        else:
            level_rate = p.get_item('level_limit_3', 'profit')

        rate = Decimal('1') + Decimal(str(level_rate)) / 100
        return float(round(item * rate, 2))

    def pay_error(self):
        data = request.data
        print data
        return {
            "return_code": "SUCCESS",
            "return_msg": "OK"
        }

    def check_big(self, orderproduct):
        # productsku = self.sproduct
        # product = self.sproduct.get_prmainpic_by_prid(orderproduct.PRid)
        # if not product:
        #     raise SYSTEM_ERROR(u"数据库异常")
        prtarget_list = self.sproduct.get_product_target_by_prid(orderproduct.PRid)
        prtarget_list = [prtarget.PRtarget for prtarget in prtarget_list]
        return '101' in prtarget_list

    def upgrade_user(self, data, biglist):
        """如果是大礼包订单则升级该用户并且指派上级"""
        if not biglist:
            return
        USshopkeeper = data.get("usshopkeeper")
        user = dict(USshopkeeper=USshopkeeper, USlevel=1)
        logger.debug('start upgrad user %s, params is %s', request.user.USname, user)
        update_result = self.suser.update_user(request.user.id, user)
        if not update_result:
            logger.error('update user error, check database')
            raise SYSTEM_ERROR