# *- coding:utf8 *-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import ProductSkuValue
sys.path.append(os.path.dirname(os.getcwd()))


class SProductSkuValue(SBase):
    @close_session
    def get_skvalue_by_prid(self, prid):
        """根据prid获取productskuvalue"""
        return self.session.query(ProductSkuValue).filter_by(PRid=prid).first()
