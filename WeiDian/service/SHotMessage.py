# *- coding:utf8 *-
import sys
import os
from datetime import datetime

from WeiDian.common.timeformat import format_for_db

sys.path.append(os.path.dirname(os.getcwd()))
from SBase import SBase, close_session
from WeiDian.models.model import HotMessage



class SHotMessage(SBase):

    @close_session
    def get_lasting_hot(self):
        """正在进行中的热文"""
        hots = self.session.query(HotMessage).order_by(HotMessage.HMsort).all()
        now_time = datetime.strftime(datetime.now(), format_for_db)
        hots = filter(lambda ht: ht.HMstarttime < now_time < ht.HMendtime, hots)
        return hots

    @close_session
    def get_all_hot(self):
        hots = self.session.query(HotMessage).order_by(HotMessage.HMsort).all()
        return hots

    @close_session
    def add_one_hot(self, hot):
        self.session.add(hot)

