# *- coding:utf8 *-
import sys
import os

from WeiDian.models.model import OrderInfo, OrderProductInfo

sys.path.append(os.path.dirname(os.getcwd()))
from SBase import SBase, close_session


class SOrder(SBase):

    @close_session
    def get_order_by_usid(self, usid):
        """获取用户的订单"""
        return self.session.query(OrderInfo).filter_by(USid=usid, OIisdelete=False).order_by(OrderInfo.OIcreatetime).all()

    @close_session
    def get_order_by_oiid(self, oiid):
        """根据订单id获取订单"""
        return self.session.query(OrderInfo).filter_by(OIid=oiid, OIisdelete=False).first()

    @close_session
    def get_order_by_oisn(self, oisn):
        """根据订单号获取订单"""
        return self.session.query(OrderInfo).filter_by(OIsn=oisn).first()

    @close_session
    def get_orderinfowithproduct_by_opiid(self, oiid):
        """联合查询测试"""
        return self.session.query(OrderInfo).join(OrderProductInfo, OrderInfo.OIid == OrderProductInfo.OIid).filter(OrderInfo.OIid == oiid).all()

    @close_session
    def get_orderproductinfo_by_oiid(self, oiid):
        return self.session.query(OrderProductInfo).filter_by(OIid=oiid).first()

