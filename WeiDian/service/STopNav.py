# *- coding:utf8 *-
import sys
import os

from WeiDian.config.response import SYSTEM_ERROR

sys.path.append(os.path.dirname(os.getcwd()))
from SBase import SBase, close_session
from WeiDian.models.model import TopNav


class STopNav(SBase):

    @close_session
    def get_all(self):
        return self.session.query(TopNav).filter_by(Tisdelete=False).order_by(TopNav.TSort).all()

    @close_session
    def add_one(self, topnav):
        self.session.add(topnav)

    @close_session
    def del_topnav(self, tnid):
        top = self.session.query(TopNav).filter_by(TNid=tnid).first()
        if top:
            top.delete()
        else:
            raise SYSTEM_ERROR
        # TODO 有问题

