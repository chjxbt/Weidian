# -*- coding: utf-8 -*-
from WeiDian.service.SOrder import SOrder


class GMV(object):
    def __init__(self):
        self.sorder = SOrder()

    def gmv(self):
        """获取gmv详情"""
        # todo
        data = {
        }
        return data

    def order_resend_info(self):
        """退换货情况"""
        data = {
        }
        return data

    def keeper_info(self):
        """平台店主情况"""

    def _total_gmv(self):
        """总gmv"""
        pass

    def _raward_gmv(self):
        """优惠券发放总额"""
        pass

    def _total_without_raward(self):
        """邀请开店gmv"""
        pass

    def _product_sold(self):
        """商品销售gmv"""
        pass

    def _partener_gmv(self):
        """三级销售GMV"""
        pass

    def _fans_gmv(self):
        """转粉gmv"""
        pass

    def _ordr_gmv(self):
        """订单量"""
        pass

    def _per_price_gmv(self):
        """客单价"""
        pass
