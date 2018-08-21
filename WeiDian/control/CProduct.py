# *- coding:utf8 *-
import sys
import os
import uuid

from WeiDian.common.MakeToken import verify_token_decorator
from WeiDian.common.TransformToList import list_add_models
from WeiDian.common.import_status import import_status
from WeiDian.config.response import TOKEN_ERROR, AUTHORITY_ERROR

sys.path.append(os.path.dirname(os.getcwd()))
from flask import request



class CProduct():
    def __init__(self):
        from WeiDian.service.SProduct import SProduct
        self.sproduct = SProduct()
        from WeiDian.service.SProductSkuValue import SProductSkuValue
        self.sproductskuvalue = SProductSkuValue()

    @verify_token_decorator
    def add_product_list(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if request.user.scope != 'SuperUser':
            return AUTHORITY_ERROR  # 权限不足
        json_data = request.json
        product_list = json_data.get('products')
        self.fill_product_list(product_list)
    
    def fill_product_list(self, items):
        for item in items:
            import ipdb
            ipdb.set_trace()
            item['prid'] = str(uuid.uuid1())  # 生成id
            psvid = str(uuid.uuid1())  # 每一个商品对应一个psv
            image_items = item['images']  # 取出image
            if image_items:
                for image_item in image_items:
                    image_item['piid'] = str(uuid.uuid1())
                    image_item['prid'] = item['prid']

            item['skuvalue'] = {}  # 顺便填充psv
            item['skuvalue']['PSVpropervalue'] = []  # value值是一个列表
            psk_items = item['psk']  # 取psk
            if psk_items:
                for psk_item in psk_items:
                    psk_item['pskid'] = str(uuid.uuid1())
                    psk_item['prid'] = item['prid']
                    psk_item['psvid'] = psvid
                    pskkey = psk_item['pskproperkey']  # key值是一个列表, 元素是个字典, 类似{key: 大小, value: xl}
                    pskkey['kid'] = str(uuid.uuid1()) # ?
                    pskkey['vid'] = str(uuid.uuid1()) # ?
            # 需要询问kid和vid是自己生成的还是已经定义好的. 
            # 如果是已经定义好的较为简单, 直接插入
            # 如果需要自行生成, 将所有的key值拼接去重便是value值,避免
            # skuvalue 填充
            # 以下几行可能需要缩进
            item['skuvalue']['piid'] = psvid
            item['skuvalue']['prid'] = item['prid']
