# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from SBase import SBase, close_session
from WeiDian.models.model import ProductLike



class SProductLike(SBase):
    @close_session
    def get_product_like_num_by_prid(self, prid):
        """获取商品的收藏数"""
        return self.session.query(ProductLike).filter_by(PRid=prid).count()

    @close_session
    def get_productlike_list_by_usid(self, usid):
        """获取用户的收藏列表"""
        return self.session.query(ProductLike).filter_by(USid=usid).all()

    @close_session
    def get_productlike_by_usidprid(self, usid, prid):
        return self.session.query(ProductLike).filter_by(USid=usid, PRid=prid).first()

