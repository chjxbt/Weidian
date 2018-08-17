# *- coding:utf8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
from SBase import SBase, close_session
from WeiDian.models.model import Product, Activity


class SProduct(SBase):

    @close_session
    def get_soldnum_by_pid(self, prid):
        product = self.session.query(Product).filter_by(PRid=prid).first()
        return product.PRsalesvolume
