# *- coding:utf8 *-
import uuid

from flask import request

from WeiDian.common.MakeToken import verify_token_decorator
from WeiDian.common.TransformToList import list_add_models, dict_add_models
from WeiDian.common.import_status import import_status
from WeiDian.config.response import TOKEN_ERROR, AUTHORITY_ERROR
from WeiDian.control.BaseControl import BaseProductControl


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
        product_list = self.fill_product_list(product_list)
        list_add_models('Product', product_list)
        data = import_status('add_product_list_success', 'OK')
        data['data'] = {'prid': self.prid_list}
        return data
