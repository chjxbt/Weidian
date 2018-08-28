# *- coding:utf8 *-
import uuid
import random
from datetime import datetime

from flask import request

from WeiDian.common.TransformToList import dict_add_models, list_add_models
from WeiDian.common.timeformat import format_for_db
from WeiDian.common.token_required import verify_token_decorator, is_partner
from WeiDian.common.import_status import import_status
from WeiDian.service.SOrder import SOrder
from WeiDian.service.SProductImage import SProductImage
from WeiDian.service.SProductSkuKey import SProductSkuKey
from WeiDian.service.SProduct import SProduct
from WeiDian.config.response import PARAMS_MISS, SYSTEM_ERROR, AUTHORITY_ERROR, TOKEN_ERROR
from WeiDian.common.token_required import is_tourist



class COrder():
    def __init__(self):
        self.sorder = SOrder()
        self.sproductskukey = SProductSkuKey()
        self.sproduct = SProduct()
        self.sproductimage = SProductImage()

    @verify_token_decorator
    def add_one(self):
        if is_tourist():
            return TOKEN_ERROR
        data = request.json
        if not data:
            return PARAMS_MISS
        required = ['oiaddress', 'oisingername', 'oisingerphone', 'sku']
        missed = filter(lambda x: x not in data, required)
        if missed:
            return PARAMS_MISS('必要参数缺失: ' + '/'.join(missed))
        order_dict = dict(
            oiid=str(uuid.uuid4()),
            oisn=datetime.strftime(datetime.now(), format_for_db) + str(random.randint(10000, 100000)),
            oileavetext=data.get('oileavetext') or '',
            oiaddress=data.get('oiaddress'),
            oisingername=data.get('oisingername'),
            oisingerphone=data.get('oisingerphone'),
        )
        sku = data.get('sku')
        orderproductinfo_dict_list = self.fix_orderproduct_info(sku, order_dict['oiid'])
        list_add_models('OrderProductInfo', orderproductinfo_dict_list)
        order_dict['OIproductprice'] = sum([x['OIproductprice'] for x in orderproductinfo_dict_list])
        dict_add_models('OrderInfo', order_dict)
        return 'ok'

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
            # 商品价格
            orderproductinfo_dict['OIproductprice'] = self.sproductskukey.get_true_price(pskid, partner=is_partner()) *\
                                                      orderproductinfo_dict['opiproductnum']
            sku_dict_list.append(orderproductinfo_dict)
            import ipdb
            ipdb.set_trace()
        return sku_dict_list

    @verify_token_decorator
    def get_order_list(self):
        if is_tourist():
            return TOKEN_ERROR

    @verify_token_decorator
    def update_order(self):
        if is_tourist():
            return TOKEN_ERROR 
