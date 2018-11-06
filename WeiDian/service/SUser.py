# *- coding:utf8 *-
import sys
import os
from werkzeug.security import check_password_hash
from SBase import SBase, close_session
from WeiDian.models.model import User, Activity, UserLoginTime
from sqlalchemy import func, or_

sys.path.append(os.path.dirname(os.getcwd()))


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
        """通过suid获取发布者"""
        return self.session.query(User).filter_by(USid=usid).first()

    @close_session
    def verify_user(self, usname):
        """通过用户名和密码验证"""
        return self.session.query(User).filter_by(USname=usname).first()
        # if user:
        #     if check_password_hash(user.USpassword, uspassword):
        #         return user

    @close_session
    def get_user_by_openid(self, openid):
        return self.session.query(User).filter(User.openid == openid).first()

    @close_session
    def update_user(self, userid, user):
        return self.session.query(User).filter(User.USid == userid).update(user)

    @close_session
    def get_user_login_time(self, usid):
        return self.session.query(UserLoginTime).filter(UserLoginTime.USid == usid).order_by(
            UserLoginTime.USTcreatetime.desc()).first()

    @close_session
    def get_partner_count(self):
        """合伙人数量"""
        return self.session.query(User).filter(User.USlevel > 0).count()

    @close_session
    def get_all_user(self, page_size, page_num):
        return self.session.query(User).offset(page_size * (page_num - 1)).limit(
            page_size).all(), self.session.query(User).count()

    @close_session
    def get_sub_user(self, upperd, page_size, page_num):
        return self.session.query(User).filter(User.UPPerd == upperd).offset(
            page_size * (page_num - 1)).limit(page_size).all(),\
               self.session.query(func.count(User.USid)).filter(User.UPPerd == upperd).scalar()

    @close_session
    def get_partner_count_in_current_level(self, level):
        """该等级的合伙人总数"""
        return self.session.query(User).filter(User.USlevel == level).count()

    @close_session
    def get_user_by_phone_or_name(self, usfilter):
        """或条件筛选用户"""
        return self.session.query(User).filter(or_(*usfilter)).all()

    @close_session
    def get_all_partner_by_filter(self, page_num, page_size, kw=None):
        """获取所有合伙人"""
        if kw is None:
            return (self.session.query(User).filter(User.USlevel > 0)
                    .offset(page_size * (page_num - 1)).limit(page_size).all(),
                    self.session.query(User).filter(User.USlevel > 0).count())
        else:
            return (self.session.query(User).filter(or_(
                User.USname.like("%{0}%".format(kw)),
                User.USphone.like("%{0}%".format(kw)))
            ).filter(User.USlevel > 0).offset(page_size * (page_num - 1)).limit(page_size).all(),
                    self.session.query(User).filter(or_(
                        User.USname.like("%{0}%".format(kw)),
                        User.USphone.like("%{0}%".format(kw)))
                    ).filter(User.USlevel > 0).count())
