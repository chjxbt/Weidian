# *- coding:utf8 *-
import uuid

from flask import request

from WeiDian.common.MakeToken import verify_token_decorator
from WeiDian.common.TransformToList import list_add_models, dict_add_models
from WeiDian.common.import_status import import_status
from WeiDian.config.response import TOKEN_ERROR, AUTHORITY_ERROR
from WeiDian.control.BaseActivityControl import BaseProductControl


class CProduct(BaseProductControl):
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
        len_product_list = len_product_list[start: end]

    def fill_images(self):
        pass