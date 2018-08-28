# *- coding:utf8 *-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import ProductLike
sys.path.append(os.path.dirname(os.getcwd()))


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

    @close_session
    def del_productlike_usidprid(self, usid, prid):
        """删除"""
        return self.session.query(ProductLike).filter_by(USid=usid, PRid=prid).delete()


