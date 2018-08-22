# *- coding:utf8 *-
import sys
import os
from datetime import datetime, timedelta

from flask import request

from WeiDian.config.messages import delete_activity_success, stop_activity_success
from WeiDian.common.MakeToken import verify_token_decorator
from WeiDian.common.TransformToList import add_model
from WeiDian.common.import_status import import_status
from WeiDian.common.timeformat import format_for_db
from WeiDian.config.response import PARAMS_MISS, TOKEN_ERROR, AUTHORITY_ERROR, SYSTEM_ERROR


class CShoppingCart():
    def __init__(self):
        from WeiDian.service.SShoppingCart import SShoppingCart
        self.sshoppingcart = SShoppingCart()
        from WeiDian.service.SProduct import SProduct
        self.sproduct = SProduct()
        from WeiDian.service.SProductSkuKey import SProductSkuKey
        self.sproductskukey = SProductSkuKey()

    @verify_token_decorator
    def get_shopingcart_all(self):
        if not hasattr(request, 'user'):
            return SYSTEM_ERROR  # token失效或者未携带token
        carts_list = self.sshoppingcart.get_shoppingcart_by_usid(request.user.id)

    @verify_token_decorator
    def update_shoppingcart(self):
        """购物车添加或者修改"""
        pass

    def fill_product_key(self, cart):
        """填充psk, 以及必须的商品信息"""
        pskid = cart.PSKid
        psk_key = self.sproductskukey.get_psk_by_pskid(pskid)
        if pskid:
            prid = psk_key.prid
            product = self.sproduct.get_product_by_prid(prid)

