# *- coding:utf8 *-
import sys
import os

from werkzeug.security import check_password_hash

sys.path.append(os.path.dirname(os.getcwd()))
from SBase import SBase, close_session
from WeiDian.models.model import User, Activity


class SUser(SBase):

    @close_session
    def get_user_by_activity_id(self, acid):
        """通过活动id获取发布者"""
        activity = self.session.query(Activity).filter_by(ACid=acid).first()
        usid = activity.USid
        return self.session.query(
            User.USid,
            User.USname,
            User.UShader
        ).filter_by(USid=usid).first()

    @close_session
    def get_user_by_user_id(self, usid):
        """通过活动id获取发布者"""
        return self.session.query(User).filter_by(USid=usid).first()

    @close_session
    def verify_super(self, usname, uspassword):
        """通过用户名和密码验证"""
        user = self.session.query(User).filter_by(USname=usname).first()
        if user:
            if check_password_hash(user.USpassword, uspassword):
                return user
