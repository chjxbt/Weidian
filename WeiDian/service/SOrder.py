# *- coding:utf8 *-
import sys
import os
from datetime import datetime, date, timedelta

from WeiDian.common.timeformat import format_for_db
from WeiDian.models.model import OrderInfo, OrderProductInfo, OrderProductResend
from sqlalchemy import or_, extract
from SBase import SBase, close_session
sys.path.append(os.path.dirname(os.getcwd()))

class SOrder(SBase):

    # @close_session
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
        filter_order = {
            OrderInfo.USid == usid,
            OrderInfo.OIisdelete == False
        }
        if isinstance(status, list):
            filter_order.add(OrderInfo.OIpaystatus.in_(status))
        else:
            filter_order.add(OrderInfo.OIpaystatus == status)
        return self.session.query(OrderInfo).filter(*filter_order).order_by(OrderInfo.OIcreatetime.desc()).all_with_page(page_num, page_size)

    @close_session
    def get_sell_order_by_status(self, usid, status, page_num, page_size):
        """根据支付状态获取销售订单"""
        filter_order = {
            OrderInfo.Sellerid == usid,
            OrderInfo.OIisdelete == False
        }
        if isinstance(status, list):
            filter_order.add(OrderInfo.OIpaystatus.in_(status))
        else:
            filter_order.add(OrderInfo.OIpaystatus == status)
        return self.session.query(OrderInfo).filter(*filter_order).order_by(OrderInfo.OIcreatetime.desc()).all_with_page(page_num, page_size)

    @close_session
    def get_sell_order_by_status2(self, status, page_num, page_size, usid=None, phone=None):
        """同上"""
        filter_order = set()
        if isinstance(status, list):
            filter_order.add(OrderInfo.OIpaystatus.in_(status))
        else:
            filter_order.add(OrderInfo.OIpaystatus == status)
        return self.session.query(OrderInfo).filter(*filter_order).filter_without_none(
            OrderInfo.USid == usid,
            OrderInfo.OIrecvphone == phone,
            OrderInfo.OIisdelete == False
        ).order_by(OrderInfo.OIcreatetime.desc()).all_with_page(page_num, page_size)

    @close_session
    def get_sellorder_by_user_status(self, usid, status):
        """根据状态和用户获取所有的销售订单"""
        return self.session.query(OrderInfo).filter(OrderInfo.Sellerid == usid,
                                                    or_(OrderInfo.OIpaystatus == s for s in status)).filter(OrderInfo.OIisdelete == False).\
            order_by(OrderInfo.OIcreatetime.desc()).all()

    @close_session
    def get_sellorder_fitler_status__all(self, status, mount=0):
        """获取某状态的所有订单"""
        return self.session.query(OrderInfo).filter(or_(OrderInfo.OIpaystatus == s for s in status),).order_by(OrderInfo.OIcreatetime.desc()).all()

    @close_session
    def get_today_order_by_usid_status(self, usid, status):
        """获取某人今日指定状态订单"""
        today = datetime.now()
        today_str = datetime.strftime(today, format_for_db)[:8]
        return self.session.query(OrderInfo).filter(or_(OrderInfo.OIpaystatus == s for s in status)).filter(
            OrderInfo.USid == usid,
            OrderInfo.OIisdelete == False,
            OrderInfo.OIpaytime.like(today_str + '%')
        ).all()
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
        return self.session.query(OrderInfo).filter(
            OrderInfo.USid == usid,
            OrderInfo.OIisdelete == False,
            # or_(OrderInfo.Sellerid != OrderInfo.USid, OrderInfo.Sellerid.in_(["", None])),
            OrderInfo.OIpaystatus.in_(status)
        ).count()

    @close_session
    def get_user_ordercount_by_item_status(self, usid, staus):
        return self.session.query(OrderInfo).filter(
            OrderInfo.USid == usid,  # OrderInfo.Sellerid != usid,
            OrderInfo.OIpaystatus == staus,
            OrderInfo.OIisdelete == False
        ).count()

    @close_session
    def get_sell_ordercount_by_status(self, usid=None, status=[]):
        """获取销售订单预览数"""
        return self.session.query(OrderInfo).filter_without_none(
            OrderInfo.Sellerid == usid,
            OrderInfo.OIisdelete == False
        ).filter(OrderInfo.OIpaystatus.in_(status)).count()

    @close_session
    def get_sell_ordercount_by_item_status(self, usid=None, status=None):
        return self.session.query(OrderInfo).filter_without_none(
            OrderInfo.Sellerid == usid, OrderInfo.OIpaystatus == status,
            OrderInfo.OIisdelete == False
        ).count()

    @close_session
    def get_order_by_oisn(self, oisn):
        """根据订单号获取订单"""
        return self.session.query(OrderInfo).filter_by(OIsn=oisn, OIisdelete=False).first()

    @close_session
    def get_orderinfowithproduct_by_opiid(self, oiid):
        """联合查询测试"""
        return self.session.query(OrderInfo).join(
            OrderProductInfo,
            OrderInfo.OIid == OrderProductInfo.OIid).filter(
            OrderInfo.OIid == oiid).all()

    @close_session
    def get_orderproduct_by_prid(self, prid):
        return self.session.query(OrderProductInfo).filter(OrderProductInfo.PRid == prid).all()

    @close_session
    def get_orderproductinfo_by_oiid(self, oiid):
        return self.session.query(
            OrderProductInfo).filter_by(OIid=oiid).all()

    @close_session
    def get_orderproductinfo_by_oisn(self, oisn):
        """通过订单号获取订单商品信息"""
        return self.session.query(OrderProductInfo).\
            join(OrderInfo, OrderProductInfo.OIid == OrderInfo.OIid).filter(
            OrderInfo.OIsn == oisn
        ).all()

    @close_session
    def update_orderinfo_status(self, oiid, orderinfo):
        return self.session.query(OrderInfo).filter(OrderInfo.OIid == oiid).update(orderinfo)

    @close_session
    def update_orderinfo_by_oisn(self, oisn, data):
        """更新订单"""
        return self.session.query(OrderInfo).filter(OrderInfo.OIsn == oisn).update(data)

    @close_session
    def get_orderproductinfo_by_opiid(self, opiid):
        """根据id获取订单中的商品"""
        return self.session.query(OrderProductInfo).filter(OrderProductInfo.OPIid == opiid).first()

    @close_session
    def get_orderproduct_resend_by_opiid(self, opiid):
        """根据订单商品详情获取退货(款)信息"""
        return self.session.query(OrderProductResend).filter(OrderProductResend.OPIid == opiid).first()

    @close_session
    def get_refund_product(self):
        """获取所有退货"""
        return self.session.query(OrderProductResend).filter(OrderProductResend.OPRtype == 0).all()

    @close_session
    def update_orderproductinfo_by_opiid(self, opiid, data):
        """根据opiid更新订单中的商品信息"""
        return self.session.query(OrderProductInfo).filter(
            OrderProductInfo.OPIid == opiid
        ).update(data)

    @close_session
    def get_order_by_opiid(self, opiid):
        """根据订单商品的id获取所属的订单"""
        return self.session.query(OrderInfo).join(OrderProductInfo, OrderProductInfo.OIid == OrderInfo.OIid).filter(
            OrderProductInfo.OPIid == opiid
        ).first()

    @close_session
    def update_order_productinfo_by_oiid(self, oiid, data):
        """根据订单id更新详情信息
        """
        return self.session.query(OrderProductInfo).filter(OrderProductInfo.OIid == oiid).update(data)

    @close_session
    def update_order_by_oiid(self, oiid, data):
        """根据订单ip更新订单"""
        return self.session.query(OrderInfo).filter(OrderInfo.OIid == oiid).update(data)

    @close_session
    def get_user_count_order(self, usid):
        usercount = self.session.query(OrderInfo).filter(
            OrderInfo.USid == usid, OrderInfo.OIpaystatus.in_(['1', '4', '5', '6', '11'])).count()
        sellcount = self.session.query(OrderInfo).filter(
            OrderInfo.Sellerid == usid, OrderInfo.OIpaystatus.in_(['1', '4', '5', '6', '11'])
        ).count()
        return usercount, sellcount

    @close_session
    def update_order_product_resend_by_oprid(self, oprid, data):
        """更新退货信息的状态"""
        return self.session.query(OrderProductResend).filter(OrderProductResend.OPRid == oprid).update(data)

    @close_session
    def get_order_all(self):
        """所有订单"""
        return self.session.query(OrderInfo).\
            filter(OrderInfo.OIisdelete == False).all()

    @close_session
    def get_yestoday_order_all(self):
        """昨日订单"""
        yesterday = datetime.now() - timedelta(days=1)
        return self.session.query(OrderInfo).filter(
            extract('day', OrderInfo.OIcreatetime) == yesterday.day,
            extract('month', OrderInfo.OIcreatetime) == yesterday.month,
            extract('year', OrderInfo.OIcreatetime) == yesterday.year,
            OrderInfo.OIisdelete == False
        ).all()

