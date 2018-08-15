# *- coding:utf8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
from SBase import SBase, close_session
from WeiDian.models.model import ActivityFoward, Activity



class SActivityFoward(SBase):

    @close_session
    def get_fowardnum_by_acid(self, acid):
        """活动的转发量"""
        return self.session.query(ActivityFoward).filter_by(ACid=acid).count()