# *- coding:utf8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
from SBase import SBase, close_session
from WeiDian.models.model import ProductSkuKey


class SProductSkuKey(SBase):
    @close_session
    def get_psk_by_pid(self, prid):
        return self.session.query(ProductSkuKey).filter_by(PRid=prid).all()