# *- coding:utf8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
from SBase import SBase, close_session
from WeiDian.models.model import User


class SUser(SBase):

    @close_session
    def get_user_by_activity_id(self, acid):
        """通过活动id获取发布者"""
        return self.session.query(
            User.USid,
            User.USname,
            User.UShader
        ).filter_by(ACid=acid).first()
