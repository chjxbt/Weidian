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
    def get_all_super_by_sufilter(self, sufilter):
        """根据条件获取所有管理"""
        return self.session.query(SuperUser).filter_by(**sufilter).all()

    @close_session
    def get_one_super_by_suid(self, suid):
        """通过suid获取超级用户"""
        return self.session.query(SuperUser).filter_by(SUid=suid).first()

    @close_session
    def get_existuser_by_name(self, sufilter):
        """用于判断用户是否已存在"""
        return self.session.query(SuperUser).filter_by(**sufilter).first()

    @close_session
    def verify_super(self, suname, supassword):
        """通过用户名和密码验证"""
        super = self.session.query(SuperUser).filter_by(SUname=suname).first()
        if super:
            if check_password_hash(super.SUpassword, supassword):
                return super

    @close_session
    def update_info(self, suid, info):
        """修改基本信息"""
        return self.session.query(SuperUser).filter_by(SUid=suid).update(info)
