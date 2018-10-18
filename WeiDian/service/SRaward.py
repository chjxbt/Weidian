# *- coding:utf8 *-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import Raward, TaskRaward, UserRaward
sys.path.append(os.path.dirname(os.getcwd()))


class SRaward(SBase):

    @close_session
    def get_raward_by_id(self, raid):
        return self.session.query(Raward).filter(Raward.RAid == raid).first()

    @close_session
    def get_raward_by_tlid(self, tlid):
        return self.session.query(TaskRaward).filter(TaskRaward.TLid == tlid).all()

    @close_session
    def delte_task_raward_by_tlid(self, tlid):
        return self.session.query(TaskRaward).filter(TaskRaward.TLid == tlid).delete()

    @close_session
    def get_all_reward(self):
        return self.session.query(Raward).all()

    @close_session
    def get_reward_by_usid(self, usid):
        return self.session.query(UserRaward).filter(UserRaward.USid == usid).all()

    @close_session
    def is_user_hold_reward(self, rafilter):
        """查看该用户是否已拥有该种优惠券"""
        return self.session.query(UserRaward).filter_by(**rafilter).first()

    @close_session
    def update_user_reward(self, rafilter, change_info):
        """更新用户持有优惠券"""
        return self.session.query(UserRaward).filter_by(**rafilter).update(change_info)