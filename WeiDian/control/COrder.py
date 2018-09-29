# -*- coding:utf8 -*-
import sys
import os
import uuid
import random
from datetime import datetime

from WeiDian import logger
from WeiDian.common.params_require import parameter_required
from WeiDian.config.enums import ORDER_STATUS
from flask import request
from WeiDian.common.TransformToList import dict_add_models, list_add_models
from WeiDian.common.timeformat import format_for_db
from WeiDian.common.token_required import verify_token_decorator, is_partner
from WeiDian.common.import_status import import_status
from WeiDian.service.SOrder import SOrder
from WeiDian.service.SProductImage import SProductImage
from WeiDian.service.SProductSkuKey import SProductSkuKey
from WeiDian.service.SProduct import SProduct
from WeiDian.service.SComplain import SComplain
from WeiDian.service.SUser import SUser
from WeiDian.config.response import PARAMS_MISS, SYSTEM_ERROR, AUTHORITY_ERROR, TOKEN_ERROR
from WeiDian.common.token_required import is_tourist
sys.path.append(os.path.dirname(os.getcwd()))


class COrder():
    def __init__(self):
        self.sorder = SOrder()
        self.sproductskukey = SProductSkuKey()
        self.sproduct = SProduct()
        self.sproductimage = SProductImage()
        self.suser = SUser()
        self.scomplain = SComplain()

    @verify_token_decorator
    def add_one(self):
        if is_tourist():
            return TOKEN_ERROR
        data = request.json
        if not data:
            return PARAMS_MISS
        required = ['oiaddress', 'oirecvname', 'oirecvphone', 'sku']
        missed = filter(lambda x: x not in data, required)
        if missed:
            return PARAMS_MISS('必要参数缺失: ' + '/'.join(missed))
        order_dict = dict(
            oiid=str(uuid.uuid4()),
            usid=request.user.id,
            oisn=datetime.strftime(datetime.now(), format_for_db) + str(random.randint(10000, 100000)),
            oileavetext=data.get('oileavetext') or '',
            oiaddress=data.get('oiaddress'),
            oirecvname=data.get('oirecvname'),
            oirecvphone=data.get('oirecvphone'),
        )
        sku = data.get('sku')
        orderproductinfo_dict_list = self.fix_orderproduct_info(sku, order_dict['oiid'])
        list_add_models('OrderProductInfo', orderproductinfo_dict_list)
        order_dict['oimount'] = sum([x['OIproductprice'] for x in orderproductinfo_dict_list]) # 总价
        dict_add_models('OrderInfo', order_dict)
        data = import_status('add_order_success', 'OK')
        data['data'] = {
            'oiid': order_dict['oiid']
        }
        return data

    # @verify_token_decorator
    # def get_order_list(self):
    #     """获取所有订单"""
    #     if is_tourist():
    #         return AUTHORITY_ERROR(u"未登录")
    #     args = request.args.to_dict()
    #     make_log("args", args)
    #     true_args = ["sell", "page_size", "page_num"]
    #     if judge_keys(true_args, args.keys()) != 200:
    #         return judge_keys(true_args, args.keys())
    #     try:
    #         order_list = self.sorder.get_order_by_usid(args["sell"], request.user.id, int(args["page_num"]), int(args["page_size"]))
    #         for order in order_list:
    #             order.fields = ['OIsn', 'OIpaystatus', 'OIcreatetime']
    #         map(self.fill_productinfo, order_list)
    #         map(self.fill_complainstatus, order_list)
    #         data = import_status('get_order_list_success', 'OK')
    #         data['data'] = order_list
    #         return data
    #     except:
    #         logger.exception("get order list error")
    #         return SYSTEM_ERROR

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
        status = [str(i) for i in range(1, 12)] if status == '0' else status
        status = ['2', '4', '5', '7', '9', '10', '11'] if status == '20' else status
        print status
        try:
            if sell == 'true':
                order_list = self.sorder.get_sell_order_by_status(request.user.id, status, int(args["page_num"]), int(args["page_size"]))
                order_list_count = self.sorder.get_sell_ordercount_by_status(request.user.id, status)
            else:
                order_list = self.sorder.get_user_order_by_status(request.user.id, status, int(args["page_num"]), int(args["page_size"]))
                order_list_count = self.sorder.get_user_ordercount_by_status(request.user.id, status)
            for order in order_list:
                order.fields = ['OIid', 'OIsn', 'OIpaystatus', 'OIcreatetime']
            map(lambda x: x.fill(ORDER_STATUS.get(str(x.OIpaystatus)), 'oipaystatusmsg'), order_list)
            # map(self.fill_oistatusmessage, order_list)
            map(self.fill_productinfo, order_list)
            map(self.fill_complainstatus, order_list)
            data = import_status('get_order_list_success', 'OK')
            data['totalcount'] = order_list_count
            data['data'] = order_list
            return data
        except:
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
        all_status = ['1', '5', '6', '10', '11']
        if sell == 'true':
            json_data = [
                {
                    'status': u'全部',
                    'statusnum': u'0',
                    'count': self.sorder.get_sell_ordercount_by_status(request.user.id, all_status)
                },
                {
                    'status': u'待支付',
                    'statusnum': u'1',
                    'count': self.sorder.get_sell_ordercount_by_status(request.user.id, '1')
                },
                {
                    'status': u'待收货',
                    'statusnum': u'5',
                    'count': self.sorder.get_sell_ordercount_by_status(request.user.id, '5')
                },
                {
                    'status': u'已完成',
                    'statusnum': u'6',
                    'count': self.sorder.get_sell_ordercount_by_status(request.user.id, '7')
                },
                # {
                #     'status': u'已取消',
                #     'statusnum': u'7',
                #     'count': self.sorder.get_sell_ordercount_by_status(request.user.id, '7')
                # },
                # {
                #     'status': u'待评价',
                #     'statusnum': u'10',
                #     'count': self.sorder.get_sell_ordercount_by_status(request.user.id, '10')
                # },
                {
                    'status': u'退换货',
                    'statusnum': u'11',
                    'count': self.sorder.get_sell_ordercount_by_status(request.user.id, '11')
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
                    'status': u'待支付',
                    'statusnum': u'1',
                    'count': self.sorder.get_user_ordercount_by_status(request.user.id, '1')
                },
                {
                    'status': u'待发货',
                    'statusnum': u'5',
                    'count': self.sorder.get_user_ordercount_by_status(request.user.id, '5')
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
                    'count': self.sorder.get_user_ordercount_by_status(request.user.id, '11')
                }
            ]

        data = import_status('get_order_count_success', 'OK')
        data['data'] = json_data
        return data

    @verify_token_decorator
    def update_order(self):
        if is_tourist():
            return TOKEN_ERROR
        pass

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
            prid = productskukey.PRid
            product = self.sproduct.get_product_by_prid(prid)
            orderproductinfo_dict = dict(
                opiid=str(uuid.uuid4()),
                oiid=oiid,
                prid=prid,
                PSKproperkey=productskukey.PSKproperkey,  # 商品属性组合(sku)
            )
            # 商品名字
            orderproductinfo_dict['opiproductname'] = product.PRname
            # 商品主图
            orderproductinfo_dict['opiproductimages'] = product.PRmainpic
            # 商品数量
            orderproductinfo_dict['opiproductnum'] = int(sku.get('num', 1))
            # 商品价格(小计)
            orderproductinfo_dict['OIproductprice'] = self.sproductskukey.get_true_price(pskid, partner=is_partner()) *\
                                                      orderproductinfo_dict['opiproductnum']
            sku_dict_list.append(orderproductinfo_dict)
        return sku_dict_list

 
    def fill_productinfo(self, order):
        oiid = order.OIid
        order.productinfo = self.sorder.get_orderproductinfo_by_oiid(oiid)
        order.productinfo.fields = ['OPIproductname', 'OPIproductimages']
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

    # @staticmethod
    # def fill_oistatusmessage(order):
    #     oistatus = order.OIpaystatus
    #     if oistatus == 1:
    #         order.oipaystatusmsg = '待支付'
    #     elif oistatus == 5:
    #         order.oipaystatusmsg = '待发货'
    #     elif oistatus == 6:
    #         order.oipaystatusmsg = '已发货'
    #     elif oistatus == 7:
    #         order.oipaystatusmsg = '已取消'
    #     else:
    #         order.oipaystatusmsg = '暂无此类订单'
    #     # oipaystatusmsg = ORDER_STATUS[1]
    #     order.add('oipaystatusmsg')
    #     return order


