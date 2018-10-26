# -*- coding: utf-8 -*-
from WeiDian.service.SOrder import SOrder


class GMV(object):
    def __init__(self):
        self.sorder = SOrder()

    def total_gmv(self):
        """平台总gmv"""
        data = {
            'total_order': self.sorder.get_order_all()
        }

    def order_count(self):
        return len(self.order_all)

    @property
    def order_all(self):
        return self.sorder.get_order_all()
