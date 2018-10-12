# *- coding:utf8 *-
import sys
import os
from WeiDian.config.response import SYSTEM_ERROR
from SBase import SBase, close_session
from WeiDian.models.model import TopNav

sys.path.append(os.path.dirname(os.getcwd()))


class STopNav(SBase):

    @close_session
    def get_all_topnav(self):
        return self.session.query(TopNav).filter_by(Tisdelete=False, TNparentid=0).order_by(TopNav.TSort).all()

    @close_session
    def get_home_list_by_parentid(self, tnparentid=0):
        return self.session.query(TopNav).filter_by(Tisdelete=False, TNparentid=tnparentid, TNtype=1).order_by(
            TopNav.TSort).all()

    @close_session
    def get_dp_list_by_parentid(self, tnparentid=0):
        return self.session.query(TopNav).filter_by(Tisdelete=False, TNparentid=tnparentid, TNtype=2).order_by(
            TopNav.TSort).all()

    @close_session
    def get_list_by_parentid(self, tnparentid=0):
        return self.session.query(TopNav).filter_by(Tisdelete=False, TNparentid=tnparentid).order_by(TopNav.TSort).all()

    @close_session
    def get_topnav_by_tnid(self, tnid):
        return self.session.query(TopNav).filter(TopNav.TNid == tnid).first()

    @close_session
    def del_topnav(self, tnid):
        return self.session.query(TopNav).filter_by(TNid=tnid).delete()

    @close_session
    def get_topnav_by_name(self, name):
        return self.session.query(TopNav).filter(TopNav.TNname == name).first()

    @close_session
    def update_topnav_by_tnidorname(self, data, tnid=None, name=None):
        """更新"""
        return self.session.query(TopNav).\
            filter_without_none(TopNav.TNid == tnid).\
            filter(TopNav.TNname.contains(name)).update(data, synchronize_session='fetch')
