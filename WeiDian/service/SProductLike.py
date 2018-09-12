# *- coding:utf8 *-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import ProductLike
from sqlalchemy import or_
sys.path.append(os.path.dirname(os.getcwd()))


class SProductLike(SBase):
    @close_session
    def get_product_like_num_by_prid(self, prid):
        """获取商品的收藏数"""
        return self.session.query(ProductLike).filter_by(PRid=prid).count()

    @close_session
    def get_productlike_list_by_usid(self, usid, page_num, page_size):
        """获取用户的收藏列表"""
        return self.session.query(ProductLike).filter_by(USid=usid).order_by(ProductLike.PLcreatetime.desc()).offset(page_size * (page_num - 1)).limit(page_size).all()

    @close_session
    def get_prlike_count_by_usid(self, usid):
        """获取用户收藏的总条数"""
        return self.session.query(ProductLike).filter_by(USid=usid).count()

    @close_session
    def get_productlike_by_usidprid(self, usid, prid):
        return self.session.query(ProductLike).filter_by(
            USid=usid, PRid=prid).first()

    @close_session
    def batch_delete_prlike(self, plidlist):
        """批量删除收藏"""
        # return self.session.query(ProductLike).filter(ProductLike.PLid.in_(plidlist)).delete()
        return self.session.query(ProductLike).filter(or_(ProductLike.PLid == plid for plid in (plidlist))).delete()

    @close_session
    def del_productlike_usidprid(self, usid, prid):
        """删除单条收藏"""
        return self.session.query(ProductLike).filter_by(
            USid=usid, PRid=prid).delete()
