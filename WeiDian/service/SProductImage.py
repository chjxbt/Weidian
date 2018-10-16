# *- coding:utf8 *-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import ProductImage
sys.path.append(os.path.dirname(os.getcwd()))


class SProductImage(SBase):
    @close_session
    def get_images_by_prid(self, prid):
        images_list = self.session.query(ProductImage).filter_by(PRid=prid, PIexist=True).order_by(
            ProductImage.PIsort).all()
        return images_list

    @close_session
    def get_images_by_prid_pisort(self, prid, pisort):
        return self.session.query(ProductImage).filter_by(PRid=prid, PIsort=pisort, PIexist=True).order_by(
            ProductImage.PIsort).first()

    @close_session
    def update_image(self, piid, piimage):
        return self.session.query(ProductImage).filter(ProductImage.PIid == piid, ProductImage.PIexist == True).update(
            piimage)