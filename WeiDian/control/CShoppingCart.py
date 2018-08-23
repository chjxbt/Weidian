# *- coding:utf8 *-
import sys
import os
import uuid
from datetime import datetime, timedelta

from flask import request

from WeiDian.config.messages import delete_activity_success, stop_activity_success
from WeiDian.common.token_required import verify_token_decorator, is_tourist
from WeiDian.common.TransformToList import add_model, dict_add_models
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
        """获取当前用户的购物车"""
        if not hasattr(request, 'user'):
            return SYSTEM_ERROR  # token失效或者未携带token
        carts_list = self.sshoppingcart.get_shoppingcart_by_usid(request.user.id)
        map(self.fill_product, carts_list)
        map(self.fill_sku, carts_list)
        data = import_status('get_cart_success', "OK")
        data['data'] = carts_list
        return data


    @verify_token_decorator
    def update_shoppingcart(self):
        """购物车添加或者修改"""
        if is_tourist():
            return SYSTEM_ERROR  # token无效或者未登录的用户
        data = request.json  
        # pskid 和 prid 至少需要一个, 如果用户选择的商品有productskukey则必须使用pskid
        pskid = data.get('pskid')
        prid = data.get('prid')
        scnums = int(data.get('scnums'))
        usid = request.user.id
        if not pskid and not prid:
            return PARAMS_MISS
        cart = self.sshoppingcart.get_shoppingcart_by_usidandpid(usid, prid)
        scid = cart.SCid
        if cart:  # 如果是也存在的购物车记录
            self.sshoppingcart.update_shoppingcart(cart, scnums)
        else:
            scid = str(uuid.uuid4())
            cartdict = {
                'scid': scid,
                'usid': usid,
                'pskid': pskid,
                'prid': prid,
                'scnums': scnums
            }
            dict_add_models('ShoppingCart', cartdict)
        data = import_status('update_cart_success', 'OK')
        data['data'] = {
            'scid': scid
        }
        return data





    def fill_sku(self, cart):
        """
        填充选择的sku信息
        """
        pskid = cart.PSKid
        if pskid:
            sku = self.sproductskukey.get_psk_by_pskid(pskid)
            sku.add('PSKproperkey')
            cart.PRprice = sku.PSKprice  # 价格, 如果sku有价格, 会直接覆盖掉商品表中的价格
            cart.sku = sku
            cart.add('sku') 
        return cart

    def fill_product(self, cart):
        """填充购物车的商品信息, 不包括sku"""
        prid = cart.prid
        product = self.sproduct.get_product_by_prid(prid)
        cart.PRimage = product.PRmainpic
        cart.PRtitle = product.PRtitle
        cart.PRstatus = product.PRstatus
        cart.PRprice = product.price  # 价格, 待计算
        cart.add('PRimage', 'PRtitle', 'PRstatus', 'PRprice')
        return cart
