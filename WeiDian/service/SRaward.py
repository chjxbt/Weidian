# *- coding:utf8 *-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import Raward, TaskRaward, UserRaward, RewardToUser, RewardTransfer
from sqlalchemy import or_

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
    def get_reward_by_raid_usid(self, raid, usid):
        return self.session.query(UserRaward).filter(UserRaward.USid == usid, UserRaward.RAid == raid).first()

    @close_session
    def get_gifts_and_reward_by_usid(self, usid):
        """两表查询"""
        # return self.session.query(UserRaward, RewardTransfer).filter(UserRaward.USid == usid).filter(RewardTransfer.USid == usid).all()
        return self.session.query(RewardTransfer).filter(RewardTransfer.USid == usid).all()
    
    @close_session
    def get_gifts_by_usfrom_or_usid(self, rtfilter):
        return self.session.query(RewardTransfer).filter(or_(*rtfilter)).all()

    @close_session
    def get_gifts_and_reward_by_usfilter(self, usfiler):
        """在转赠表中根据条件查询拥有券"""
        return self.session.query(RewardTransfer).filter_by(**usfiler).all()

    @close_session
    def is_user_hold_reward_in_gift(self, grfilter):
        """在转增表中查看是否拥有该券"""
        return self.session.query(RewardTransfer).filter_by(**grfilter).first()

    @close_session
    def update_reward_transfer_info(self, upfilter, upinfo):
        """更新转增表中相应的状态"""
        return self.session.query(RewardTransfer).filter_by(**upfilter).update(upinfo)

    @close_session
    def is_user_hold_reward(self, rafilter):
        """查看该用户是否已拥有该种优惠券"""
        return self.session.query(UserRaward).filter_by(**rafilter).first()

    @close_session
    def update_user_reward(self, rafilter, change_info):
        """更新用户持有优惠券"""
        return self.session.query(UserRaward).filter_by(**rafilter).update(change_info)

    @close_session
    def is_hand_out(self, rtfilter):
        """检查该优惠券是否已在页面进行发放"""
        return self.session.query(RewardToUser).filter_by(**rtfilter).first()

    @close_session
    def get_all_hand_out(self):
        """获取所有在页面内发放的优惠券"""
        return self.session.query(RewardToUser).all()

    @close_session
    def update_is_hand_out(self, rtfilter, change_info):
        """更改已在页面发放优惠券的状态"""
        return self.session.query(RewardToUser).filter_by(rtfilter).update(change_info)
