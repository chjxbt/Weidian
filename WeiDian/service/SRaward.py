# *- coding:utf8 *-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import Raward, TaskRaward, UserRaward
sys.path.append(os.path.dirname(os.getcwd()))

class SRaward(SBase):

    @close_session
    def get_raward_by_id(self, raid):
        return self.session.query(Raward).filter(Raward.RAid == raid).first()

    @close_session
    def get_raward_by_taid(self, taid):
        return self.session.query(TaskRaward).filter(TaskRaward.TAid == taid).all()

    # @close_session
    # def get_raward_by_taid(self):
