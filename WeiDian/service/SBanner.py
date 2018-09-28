# *- coding:utf8 *-
import sys
import os
from datetime import datetime
from WeiDian.common.timeformat import format_for_db
from SBase import SBase, close_session
from WeiDian.models.model import Banner
sys.path.append(os.path.dirname(os.getcwd()))


class SBnner(SBase):

    @close_session
    def get_all_banner(self):
        return self.session.query(Banner).order_by(Banner.BAsort).all()

    @close_session
    def get_all_lasting_banner(self):
        banners = self.session.query(Banner).order_by(Banner.BAsort).all()
        now_time = datetime.strftime(datetime.now(), format_for_db)
        banners = filter(lambda bn: bn.BAstarttime < now_time < bn.BAendtime, banners)
        return banners

    @close_session
    def get_one_by_baid(self, baid):
        """通过轮播图id获取轮播"""
        banner = self.session.query(Banner).filter_by(BAid=baid).first()
        return banner


    @close_session
    def del_banner(self, baid):
        return self.session.query(Banner).filter_by(BAid=baid).delete()





