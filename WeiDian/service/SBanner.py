# *- coding:utf8 *-
import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.getcwd()))
from SBase import SBase, close_session
from WeiDian.models.model import Activity, Product


class SBnner(SBase):

    @close_session
    def get_all(self):
        pass