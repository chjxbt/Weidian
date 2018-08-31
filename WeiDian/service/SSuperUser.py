# *- coding:utf8 *-
import sys
import os
# from datetime import datetime
# from WeiDian.common.timeformat import format_for_db
from werkzeug.security import generate_password_hash, check_password_hash
from SBase import SBase, close_session
from WeiDian.models.model import SuperUser
sys.path.append(os.path.dirname(os.getcwd()))


class SSuperUser(SBase):
    
    @close_session
    def get_all_super(self):
        """获取所有的超级用户"""
        return self.session.query(SuperUser).filter_by(SUisdelete=False).all()

    @close_session
    def get_one_super_by_suid(self, suid):
        """通过suid获取超级用户"""
        return self.session.query(SuperUser).filter_by(SUid=suid).first()

    @close_session
    def verify_super(self, suname, supassword):
        """通过用户名和密码验证"""
        super = self.session.query(SuperUser).filter_by(SUname=suname).first()
        if super:
            if check_password_hash(super.SUpassword, supassword):
                return super
