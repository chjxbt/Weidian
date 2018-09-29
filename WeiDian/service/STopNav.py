# *- coding:utf8 *-
import sys
import os
from WeiDian.config.response import SYSTEM_ERROR
from SBase import SBase, close_session
from WeiDian.models.model import TopNav
sys.path.append(os.path.dirname(os.getcwd()))


class STopNav(SBase):

    @close_session
    def get_home_list_by_parentid(self, tnparentid=0):
        return self.session.query(TopNav).filter_by(Tisdelete=False, TNparentid=tnparentid, TNtype = 1).order_by(TopNav.TSort).all()

    @close_session
    def get_dp_list_by_parentid(self, tnparentid=0):
        return self.session.query(TopNav).filter_by(Tisdelete=False, TNparentid=tnparentid, TNtype = 2).order_by(TopNav.TSort).all()

    @close_session
    def get_list_by_parentid(self, tnparentid=0):
        return self.session.query(TopNav).filter_by(Tisdelete=False, TNparentid=tnparentid).order_by(TopNav.TSort).all()

    @close_session
    def add_one(self, topnav):
        self.session.add(topnav)

    @close_session
    def del_topnav(self, tnid):
        return self.session.query(TopNav).filter_by(TNid=tnid).delete()

    @close_session
    def get_topnav_by_name(self, name):
        return self.session.query(TopNav).filter(TopNav.TNname == name).first()
