# -*- coding:utf8 -*-
import sys
import os
import uuid
import random
from datetime import datetime

from WeiDian.common.log import make_log, judge_keys
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

    @verify_token_decorator
    def get_order_list(self):
        """获取所有订单"""
        if is_tourist():
            return AUTHORITY_ERROR(u"未登录")
        print '已登录'
        args = request.args.to_dict()
        make_log("args", args)
        true_args = ["sell", "page_size", "page_num"]
        if judge_keys(true_args, args.keys()) != 200:
            return judge_keys(true_args, args.keys())
        order_list = self.sorder.get_order_by_usid(args["sell"], request.user.id, int(args["page_num"]), int(args["page_size"]))
        for order in order_list:
            order.fields = ['OIsn', 'OIpaystatus', 'OIcreatetime']
        map(self.fill_productinfo, order_list)
        map(self.fill_complainstatus, order_list)
        data = import_status('get_order_list_success', 'OK')
        data['data'] = order_list
        return data

    @verify_token_decorator
    def get_order_list_by_status(self):
        """根据支付状态获取订单"""
        if is_tourist():
            return AUTHORITY_ERROR(u"未登录")
        print '已登录'
        args = request.args.to_dict()
        make_log("args", args)
        sell = args.get('sell')
        true_args = ["paystatus", "sell", "page_size", "page_num"]
        if judge_keys(true_args, args.keys()) != 200:
            return judge_keys(true_args, args.keys())
        if sell:
            order_list = self.sorder.get_sell_order_by_status(request.user.id, args["paystatus"], int(args["page_num"]), int(args["page_size"]))
        else:
            order_list = self.sorder.get_user_order_by_status(request.user.id, args["paystatus"], int(args["page_num"]), int(args["page_size"]))
        for order in order_list:
            order.fields = ['OIid', 'OIsn', 'OIpaystatus', 'OIcreatetime']
        map(self.fill_productinfo, order_list)
        map(self.fill_complainstatus, order_list)
        data = import_status('get_order_list_success', 'OK')
        data['data'] = order_list
        return data

    @verify_token_decorator
    def get_order_count(self):
        """获取订单预览数"""
        if is_tourist():
            return AUTHORITY_ERROR(u"未登录")
        print '已登录'
        args = request.args.to_dict()
        make_log("args", args)
        sell = args.get('sell')
        if sell:
            json_data = [
                {
                    'status': u'待支付',
                    'count': self.sorder.get_sell_ordercount_by_status(request.user.id, 0)
                },
                {
                    'status': u'待发货',
                    'count': self.sorder.get_sell_ordercount_by_status(request.user.id, 4)
                },
                {
                    'status': u'已发货',
                    'count': self.sorder.get_sell_ordercount_by_status(request.user.id, 5)
                },
                {
                    'status': u'已取消',
                    'count': self.sorder.get_sell_ordercount_by_status(request.user.id, 6)
                }
            ]
        else:
            json_data = [
                {
                    'status': u'待支付',
                    'count': self.sorder.get_user_ordercount_by_status(request.user.id, 0)
                },
                {
                    'status': u'待发货',
                    'count': self.sorder.get_user_ordercount_by_status(request.user.id, 4)
                },
                {
                    'status': u'已发货',
                    'count': self.sorder.get_user_ordercount_by_status(request.user.id, 5)
                },
                {
                    'status': u'已取消',
                    'count': self.sorder.get_user_ordercount_by_status(request.user.id, 6)
                }
            ]

        data = import_status('get_order_count_success', 'OK')
        data['data'] = json_data
        return data

    @verify_token_decorator
    def update_order(self):
        if is_tourist():
            return TOKEN_ERROR 

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
        order.complainstatus = self.scomplain.get_complain_by_oiid(oiid)
        order.complainstatus.fields = ['COtreatstatus']
        order.add('complainstatus')
        return order