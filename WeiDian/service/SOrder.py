# *- coding:utf8 *-
import sys
import os

from WeiDian.models.model import OrderInfo, OrderProductInfo, PartnerSellMount
from sqlalchemy import or_
from SBase import SBase, close_session
sys.path.append(os.path.dirname(os.getcwd()))

class SOrder(SBase):

    @close_session
    # def get_order_by_usid(self, sell, usid, page_num, page_size):
    #     """获取用户的订单"""
    #     if sell:
    #         return self.session.query(OrderInfo).filter_by(Sellerid=usid, OIisdelete=False).order_by(
    #             OrderInfo.OIcreatetime).offset(page_size * (page_num - 1)).limit(page_size).all()
    #     else:
    #         return self.session.query(OrderInfo).filter_by(USid=usid, OIisdelete=False).order_by(
    #             OrderInfo.OIcreatetime).offset(page_size * (page_num - 1)).limit(page_size).all()

    @close_session
    def get_order_by_oiid(self, oiid):
        """根据订单id获取订单"""
        return self.session.query(OrderInfo).filter_by(OIid=oiid, OIisdelete=False).first()

    @close_session
    def get_user_order_by_status(self, usid, status, page_num, page_size):
        """根据支付状态获取自买订单"""
        return self.session.query(OrderInfo).filter(OrderInfo.USid == usid, or_(OrderInfo.OIpaystatus == s for s in (status))).offset(page_size * (page_num - 1)).limit(page_size).all()

    @close_session
    def get_sell_order_by_status(self, usid, status, page_num, page_size):
        """根据支付状态获取销售订单"""
        return self.session.query(OrderInfo).filter(OrderInfo.Sellerid == usid, or_(OrderInfo.OIpaystatus == s for s in (status))).offset(page_size * (page_num - 1)).limit(page_size).all()

    @close_session
    def get_sellorder_by_user_status(self, usid, status):
        """根据状态和用户获取所有的销售订单"""
        return self.session.query(OrderInfo).filter(OrderInfo.Sellerid == usid,
                                                    or_(OrderInfo.OIpaystatus == s for s in status)).all()

    @close_session
    def get_sellorder_fitler_status__all(self, status, mount=0):
        """获取某状态的所有订单"""
        return self.session.query(OrderInfo).filter(or_(OrderInfo.OIpaystatus == s for s in status),).all()

    @close_session
    def get_partner_sellmount_by_usid(self, usid):
        """获取某个合伙人的销售状态"""
        return self.session.query(PartnerSellMount).filter(PartnerSellMount.usid == usid).first()

    @close_session
    def get_parter_sellmount_gt(self, mount):
        """获取比某个数额多的"""
        return self.session.query(PartnerSellMount).filter(PartnerSellMount.sellmount > mount).count()

    # @close_session
    # def get_user_ordercount(self, usid, status):
    #     """获取自买订单总数"""
    #     if status == 0:
    #         return self.session.query(OrderInfo).filter(OrderInfo.USid == usid, OrderInfo.Sellerid != OrderInfo.USid, or_(OrderInfo.OIpaystatus == status for status in (1, 5, 6, 7))).count()

    # @close_session
    # def get_sell_ordercount(self, usid, status):
    #     """获取销售订单总数"""
    #     if status == 0:
    #         return self.session.query(OrderInfo).filter(OrderInfo.Sellerid == usid, or_(OrderInfo.OIpaystatus == status for status in (1, 5, 6, 7))).count()

    @close_session
    def get_user_ordercount_by_status(self, usid, status):
        """获取自买订单预览数"""
        return self.session.query(OrderInfo).filter(OrderInfo.USid == usid, OrderInfo.Sellerid != OrderInfo.USid, or_(
            OrderInfo.OIpaystatus == status for status in (status))).count()

    @close_session
    def get_sell_ordercount_by_status(self, usid, status):
        """获取销售订单预览数"""
        return self.session.query(OrderInfo).filter(OrderInfo.Sellerid == usid, or_(OrderInfo.OIpaystatus == status for status in (status))).count()

    @close_session
    def get_order_by_oisn(self, oisn):
        """根据订单号获取订单"""
        return self.session.query(OrderInfo).filter_by(OIsn=oisn).first()

    @close_session
    def get_orderinfowithproduct_by_opiid(self, oiid):
        """联合查询测试"""
        return self.session.query(OrderInfo).join(
            OrderProductInfo,
            OrderInfo.OIid == OrderProductInfo.OIid).filter(
            OrderInfo.OIid == oiid).all()

    @close_session
    def get_orderproductinfo_by_oiid(self, oiid):
        return self.session.query(
            OrderProductInfo).filter_by(OIid=oiid).first()
