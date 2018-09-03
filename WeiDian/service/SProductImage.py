# *- coding:utf8 *-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import ProductImage
sys.path.append(os.path.dirname(os.getcwd()))


class SProductImage(SBase):
    @close_session
    def get_images_by_prid(self, prid):
        images_list = self.session.query(ProductImage).filter_by(PRid=prid).order_by(ProductImage.PIsort).all()
        return images_list
