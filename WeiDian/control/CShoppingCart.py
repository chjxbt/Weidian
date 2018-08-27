# *- coding:utf8 *-
import uuid

from flask import request

from WeiDian.common.token_required import verify_token_decorator, is_tourist
from WeiDian.common.TransformToList import add_model, dict_add_models
from WeiDian.common.import_status import import_status
from WeiDian.config.response import PARAMS_MISS, TOKEN_ERROR, SYSTEM_ERROR
from WeiDian.control.BaseControl import BaseShoppingCart


class CShoppingCart(BaseShoppingCart):
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
        if is_tourist():
            return TOKEN_ERROR  # token失效或者未携带token
        carts_list = self.sshoppingcart.get_shoppingcart_by_usid(request.user.id)
        map(self.fill_sku, carts_list)
        map(self.fill_product, carts_list)
        data = import_status('get_cart_success', "OK")
        data['data'] = {"cart": carts_list}
        data['total'] = self.total_price(carts_list)
        return data

    @verify_token_decorator
    def update_shoppingcart(self):
        """购物车添加或者修改"""
        if is_tourist():
            return TOKEN_ERROR  # token无效或者未登录的用户
        data = request.json  
        # pskid
        pskid = data.get('pskid')
        scahangenums = int(data.get('changenum', 1))  # 更改数量
        usid = request.user.id
        if not pskid:
            return PARAMS_MISS
        cart = self.sshoppingcart.get_shoppingcar_by_usidandpskid(usid, pskid)
        # 如果是已经存在的购物车
        if cart:
            scid = cart.SCid
            scnums = cart.SCnums + scahangenums
            if scnums < 1:
                # 删除
                return self.delete_shoppingcart(scid)
            self.sshoppingcart.update_shoppingcart(cart, scnums)
        # 创建
        else:
            if scahangenums < 1:
                return SYSTEM_ERROR('错误的数量')
            scid = str(uuid.uuid4())
            psk = self.sproductskukey.get_psk_by_pskid(pskid)
            if not psk:
                raise SYSTEM_ERROR('不存在的商品')
            prid = psk.PRid
            cartdict = {
                'scid': scid,
                'usid': usid,
                'pskid': pskid,
                'scnums': scahangenums,
                'prid': prid
            }
            dict_add_models('ShoppingCart', cartdict)
        data = import_status('update_cart_success', 'OK')
        data['data'] = {
            'scid': scid
        }
        return data

    @verify_token_decorator
    def delete_one(self):
        """删除购物车"""
        if is_tourist(): 
            return TOKEN_ERROR
        data = request.json
        if not data:
            return PARAMS_MISS
        scid = data.get('scid')
        if not scid:
            return PARAMS_MISS
        return self.delete_shoppingcart(scid)

    def delete_shoppingcart(self, scid=None):
        if not scid:
            return PARAMS_MISS
        self.sshoppingcart.delete_shoppingcart_by_scid(scid)
        data = import_status('delete_success', 'OK')
        data['data'] = {
            "scid": scid
        }
        return data

