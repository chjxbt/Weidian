# *- coding:utf8 *-
import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.getcwd()))
from SBase import SBase, close_session
from WeiDian.models.model import Product


class SProductSkuValue(SBase):
    @close_session
    def get_skvalue_by_prid(self, prid):
        """根据prid获取productskuvalue"""
        return self.session.query(Product).filter_by(PRid=prid).first()
