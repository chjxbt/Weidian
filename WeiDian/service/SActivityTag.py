# *- coding:utf8 *-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import ActivityTag
sys.path.append(os.path.dirname(os.getcwd()))


class SActivityTag(SBase):

    @close_session
    def get_exist_tags(self):
        return self.session.query(ActivityTag).filter(ActivityTag.ACid == 'customupload').all()

    @close_session
    def del_exist_tags(self, atid):
        return self.session.query(ActivityTag).filter(ActivityTag.ATid == atid).delete()

    @close_session
    def get_show_tags_by_acid(self, tgfilter):
        """该活动的显示状态的角标"""
        return self.session.query(ActivityTag).filter_by(**tgfilter).all()

    @close_session
    def del_tags_by_acid(self, acid):
        return self.session.query(ActivityTag).filter(ActivityTag.ACid == acid).delete()
