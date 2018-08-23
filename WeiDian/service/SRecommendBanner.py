# *- coding:utf8 *-
import sys
import os

from datetime import datetime
from WeiDian.common.timeformat import format_for_db

sys.path.append(os.path.dirname(os.getcwd()))
from SBase import SBase, close_session
from WeiDian.models.model import RecommendBanner


class SRecommendBanner(SBase):

    @close_session
    def get_all_banner(self):
        return self.session.query(RecommendBanner).order_by(RecommendBanner.RBsort).all()

    @close_session
    def get_all_lasting_banner(self):
        banners = self.session.query(RecommendBanner).order_by(RecommendBanner.RBsort).all()
        now_time = datetime.strftime(datetime.now(), format_for_db)
        banners = filter(lambda rb: rb.RBstarttime < now_time < rb.RBendtime, banners)
        return banners

    @close_session
    def get_one_by_rbid(self, rbid):
        """通过轮播图id获取轮播"""
        banner = self.session.query(RecommendBanner).filter_by(RBid=rbid).first()
        return banner

    @close_session
    def add_one_banner(self, banner):
        self.session.add(banner)

    @close_session
    def del_banner(self, rbid):
        return self.session.query(RecommendBanner).filter_by(RBid=rbid).delete()
