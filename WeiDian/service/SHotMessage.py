# *- coding:utf8 *-
import sys
import os
from datetime import datetime
from WeiDian.common.timeformat import format_for_db
from SBase import SBase, close_session
from WeiDian.models.model import HotMessage
sys.path.append(os.path.dirname(os.getcwd()))


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

    @close_session
    def update_one_hot(self, hmid, **kwargs):
        hotmessage = self.session.query(HotMessage).filter_by(HMid=hmid).first()
        if hotmessage:
            if 'hmtext' in kwargs.keys():
                hotmessage.HMtext = kwargs['hmtext']
            if 'prid' in kwargs.keys():
                hotmessage.PRid = kwargs['prid']
            if 'hmstarttime' in kwargs.keys():
                hotmessage.HMstarttime = kwargs['hmstarttime']
            if 'hmendtime' in kwargs.keys():
                hotmessage.HMendtime = kwargs['hmendtime']
            if 'hmsort' in kwargs.keys():
                hotmessage.HMsort = kwargs['hmsort']
            self.session.add(hotmessage)
            return True

    @close_session
    def del_one_hot(self, hmid):
        return self.session.query(HotMessage).filter(HotMessage.HMid == hmid).delete()



