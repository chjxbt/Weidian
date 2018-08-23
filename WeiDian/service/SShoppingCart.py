# *- coding:utf8 *-
import sys
import os
from datetime import datetime

from WeiDian.common.timeformat import format_for_db
from WeiDian.models.model import ShoppingCart

sys.path.append(os.path.dirname(os.getcwd()))
from SBase import SBase, close_session


class SShoppingCart(SBase):
    @close_session
    def get_shoppingcart_by_usid(self, usid):
        """根据用户搜索购物车"""
        return self.session.query(ShoppingCart).filter_by(USid=usid).all()

    @close_session
    def get_shoppingcart_by_usidandpid(self, usid, prid):
        """根据用户和商品搜索购物车"""
        return self.session.query(ShoppingCart).filter_by(USid=usid, PRid=prid).first()

    @close_session
    def get_shoppingcar_by_usidandpskid(self, usid, pskid):
        """根据用户和sku搜索购物车"""
        return self.session.query(ShoppingCart).filter_by(USid=usid, PSKid=pskid).first()

    @close_session
    def update_shoppingcart(self, cart, scnums):
        """修改购物车"""
        cart.SCnums = scnums
        self.session.add(cart)

    @close_session
    def get_shoppingcart_list(self, usid):
        """根据用户id获取购物车"""
        return self.session.query(ShoppingCart).filter_by(USid=usid).all()

    @close_session
    def delete_shoppingcart_by_usidandpskid(self, usid, pskid):
        """删除购物车"""
        return self.session.query(ShoppingCart).filter_by(PSKid=pskid, USid=usid).delete()

