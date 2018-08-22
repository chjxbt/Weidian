# *- coding:utf8 *-
from flask import request

from WeiDian.common.MakeToken import verify_token_decorator
from WeiDian.common.TransformToList import list_add_models, dict_add_models
from WeiDian.common.import_status import import_status
from WeiDian.config.response import TOKEN_ERROR, AUTHORITY_ERROR, PARAMS_MISS, SYSTEM_ERROR
from WeiDian.control.BaseControl import BaseProductControl


class CProduct(BaseProductControl):
    def __init__(self):
        from WeiDian.service.SProduct import SProduct
        self.sproduct = SProduct()
        from WeiDian.service.SProductSkuValue import SProductSkuValue
        self.sproductskuvalue = SProductSkuValue()
        from WeiDian.service.SProductImage import SProductImage
        self.sproductimage = SProductImage()
        from WeiDian.service.SProductSkuKey import SProductSkuKey
        self.sproductskukey = SProductSkuKey()
        from WeiDian.service.SActivity import SActivity
        self.sactivity = SActivity()

    @verify_token_decorator
    def add_product_list(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if request.user.scope != 'SuperUser':
            return AUTHORITY_ERROR  # 权限不足
        json_data = request.json
        product_list = json_data.get('products')
        product_list = self.fix_product_list(product_list)
        list_add_models('Product', product_list)
        data = import_status('add_product_list_success', 'OK')
        data['data'] = {'prid': self.prid_list}
        return data

    def get_product_list(self):
        args = request.args.to_dict()
        start = int(args.get('start', 0))  # 起始位置
        count = int(args.get('count', 15))  # 取出条数
        product_list = self.sproduct.get_all()
        len_product_list = len(product_list)
        if count > 30:
            count = 30
        end = start + count
        if end > len_product_list:
            end = len_product_list
        product_list = product_list[start: end]
        data = import_status('get_product_list_success', 'OK')
        data['data'] = product_list
        return data

    def get_product_one(self):
        args = request.args.to_dict()
        prid = args.get('prid')
        if not prid:
            return PARAMS_MISS
        product = self.sproduct.get_product_by_prid(prid)
        if not product:
            return SYSTEM_ERROR
        product.fields = product.all
        product.hide('PRsalefakenum', '')
        self.fill_images(product)
        self.fill_product_sku_key(product)
        self.fill_product_sku_value(product)
        data = import_status('get_product_success', 'OK')
        data['data'] = product
        return data

    def trans_product_for_fans(self, product):
        """调整为粉丝版本"""
        pass

    def trans_product_for_shopkeeper(self, product):
        """调整为店主版本"""
        pass
        

