# *- coding:utf8 *-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import ActivityTag
sys.path.append(os.path.dirname(os.getcwd()))


class SActivityTag(SBase):

    @close_session
    def get_tags_by_acid(self, acid):
        """该活动的角标"""
        return self.session.query(ActivityTag).filter_by(ACid=acid).all()

    def get_show_tags_by_acid(self, acid):
        """该活动的显示状态的角标"""
        return self.session.query(ActivityTag).filter_by(ACid=acid, ATstate=1).all()

