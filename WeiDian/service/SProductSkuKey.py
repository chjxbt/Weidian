# *- coding:utf8 *-
import json
import sys
import os
from decimal import Decimal

from WeiDian.common.divide import Partner
from SBase import SBase, close_session
from WeiDian.models.model import ProductSkuKey, Product

sys.path.append(os.path.dirname(os.getcwd()))


class SProductSkuKey(SBase):

    @close_session
    def get_psk_by_pid(self, prid):
        """通过prid获取所有的skukey"""
        return self.session.query(ProductSkuKey).filter(ProductSkuKey.PRid == prid, ProductSkuKey.PSisdelete != 0).all()

    @close_session
    def get_psk_by_psskuid(self, psskuid, prid):
        """通过prid获取所有的skukey"""
        return self.session.query(ProductSkuKey).filter(ProductSkuKey.PSskuid == psskuid, ProductSkuKey.PSisdelete != 0).all()

    @close_session
    def get_psk_by_pskid(self, pskid):
        """通过pskid获取"""
        return self.session.query(ProductSkuKey).filter(
            ProductSkuKey.PSKid==pskid, ProductSkuKey.PSisdelete != 0).first()

    @close_session
    def get_true_price(self, pskid=None, partner=False):
        """获取真实价格"""
        psk = self.session.query(ProductSkuKey).filter(
            ProductSkuKey.PSKid == pskid, ProductSkuKey.PSisdelete != 0).first()
        # prid = psk.PRid
        # product = self.session.query(Product).filter(Product.PRid == prid).first()
        profit = Decimal(str(getattr(psk, 'PSKprofict', 5) or 5))
        if partner:
            temp = profit * Decimal(str(Partner().one_level_divide))
            return float(Decimal(str(psk.PSKprice)) - temp)
        return float(Decimal(str(psk.PSKprice)))

    @close_session
    def update_product_sku(self, skuid, prid, ps):
        return self.session.query(ProductSkuKey).filter(ProductSkuKey.PSskuid == skuid, ProductSkuKey. PRid == prid).update(ps)


