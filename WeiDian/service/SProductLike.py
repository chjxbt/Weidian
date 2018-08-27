# *- coding:utf8 *-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import ProductLike
sys.path.append(os.path.dirname(os.getcwd()))


class SProductLike(SBase):
    @close_session
    def get_product_like_num_by_prid(self, prid):
        return self.session.query(ProductLike).filter_by(PRid=prid).count()
