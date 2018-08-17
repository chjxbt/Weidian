# *- coding:utf8 *-
import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.getcwd()))
from SBase import SBase, close_session
from WeiDian.models.model import TopNav


class STopNav(SBase):

    @close_session
    def get_all(self):
        return self.session.query(TopNav).filter_by(Tisdelte=False).order_by(TopNav.TSort).all()
