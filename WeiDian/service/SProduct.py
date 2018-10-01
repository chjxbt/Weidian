# *- coding:utf8 *-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import Product, ProductLike, Recommend, RecommendProduct, Activity
sys.path.append(os.path.dirname(os.getcwd()))


class SProduct(SBase):

    @close_session
    def get_soldnum_by_pid(self, prid):
        """获取销售总量, 真实的"""
        product = self.session.query(Product).filter_by(PRid=prid).first()
        return product.PRsalesvolume

    @close_session
    def get_product_by_prid(self, prid):
        """根据商品id获取商品"""
        product = self.session.query(Product).filter_by(PRid=prid).first()
        return product

    @close_session
    def get_all(self):
        """获取所有商品"""
        product_list = self.session.query(Product).filter_by(
            PRstatus=1, PReditstate=1).all()
        return product_list

    @close_session
    def get_product_list_contail_title(self, kw):
        """模糊搜索商品名字"""
        product_list = self.session.query(Product).filter_by(
            PRstatus=1, PReditstate=1).filter(Product.PRtitle.contains(kw)).all()
        return product_list

    @close_session
    def get_all_by_filter(self, pagenum, pagesize):
        pass

    @close_session
    def get_product_list_by_reid(self, reid):
        return self.session.query(Product).join(
            RecommendProduct, Product.PRid == RecommendProduct.PRid).filter(
            RecommendProduct.REid == reid).order_by(RecommendProduct.RPsort.asc()).all()

    @close_session
    def update_view_num(self, prid):
        """增加浏览数"""
        product = self.session.query(Product).filter_by(PRid=prid).first()
        product.PRviewnum = product.PRviewnum + 1
        if product.PRfakeviewnum:
            product.PRfakeviewnum = product.PRfakeviewnum + 1
        self.session.add(product)
        self.session.commit()

    @close_session
    def update_like_num(self, prid, num=1):
        product = self.session.query(Product).filter_by(PRid=prid).first()
        if product and product.PRfakelikenum:
            product.PRfakelikenum = product.PRfakelikenum + num
            self.session.add(product)

    @close_session
    def get_products_by_prname(self, prname):
        return self.session.query(Product).filter(Product.PRname.like("%{0}%".format(prname))).all()

    @close_session
    def get_product_relation_act_by_prid(self, prid):
        return self.session.query(Activity).filter(Activity.PRid == prid, Activity.ACisdelete == False).all()