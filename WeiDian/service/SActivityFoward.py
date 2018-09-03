# *- coding:utf8 *-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import ActivityFoward, Activity
sys.path.append(os.path.dirname(os.getcwd()))


class SActivityFoward(SBase):

    @close_session
    def get_fowardnum_by_acid(self, acid):
        """活动的转发量"""
        cur_activity = self.session.query(Activity).filter_by(ACid=acid).first()
        if cur_activity.ACProductsSoldFakeNum:
            return cur_activity.ACProductsSoldFakeNum
        return self.session.query(ActivityFoward).filter_by(ACid=acid).count()
