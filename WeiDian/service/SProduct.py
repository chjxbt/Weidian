# *- coding:utf8 *-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import Product, RecommendProduct, ProductTarget, ProductBigActivity, ProductOperationRecord
from sqlalchemy import or_

sys.path.append(os.path.dirname(os.getcwd()))


class SProduct(SBase):

    @close_session
    def get_product_by_prid(self, prid):
        """根据商品id获取商品"""
        return self.session.query(Product).filter_by(PRid=prid).first()

    @close_session
    def get_prmainpic_by_prid(self, prid):
        """根据商品id获取商品主图"""
        product = self.session.query(Product.PRmainpic).filter_by(PRid=prid).first()
        return product

    @close_session
    def get_all(self):
        """获取所有商品"""
        product_list = self.session.query(Product).filter_by(
            PRstatus=1, PReditstate=1).all()
        return product_list

    @close_session
    def update_product_info_by_filter(self, prfilter, prinfo):
        """根据条件更新商品信息"""
        return self.session.query(Product).filter_by(**prfilter).update(prinfo)

    @close_session
    def get_product_filter(self, kw=None, time_start=None, time_end=None, isdelete=False, status=None, page=None, count=None):
        """模糊搜索商品名字"""
        if kw == None:
            return self.session.query(Product).filter_without_none(
                Product.PReditstate == 1,
                Product.PRstatus == status,
                Product.PRisdelete == isdelete
            ).gt(Product.PRcreatetime == time_start).lt(Product.PRcreatetime == time_end).all_with_page(page, count)
        else:
            return self.session.query(Product).filter_without_none(
                Product.PReditstate == 1,
                Product.PRstatus == status,
                Product.PRisdelete == isdelete,
            ).filter(or_(Product.PRname.like("%{0}%".format(kw)),
                         Product.PRtitle.like("%{0}%".format(kw)),
                         Product.PRoductId.like("%{0}%".format(kw)),
                         Product.SUmodifyid.like("%{0}%".format(kw)))
            ).gt(Product.PRcreatetime == time_start).lt(Product.PRcreatetime == time_end).all_with_page(page, count)

    @close_session
    def get_product_list_by_reid(self, reid):
        return self.session.query(Product).join(
            RecommendProduct, Product.PRid == RecommendProduct.PRid).filter(
            RecommendProduct.REid == reid).order_by(RecommendProduct.RPsort.asc()).all()

    @close_session
    def update_prsalesvolume(self, prid, num=1):
        """下单时更新商品销量"""
        product = self.session.query(Product).filter(Product.PRid == prid).first()
        product.PRsalesvolume = product.PRsalesvolume + num
        if product.PRsalefakenum:
            product.PRsalefakenum = product.PRsalefakenum + num
        self.session.add(product)

    @close_session
    def update_view_num(self, prid):
        """增加浏览数"""
        product = self.session.query(Product).filter_by(PRid=prid).first()
        product.PRviewnum = product.PRviewnum + 1
        if product.PRfakeviewnum:
            product.PRfakeviewnum = product.PRfakeviewnum + 1
        self.session.add(product)

    @close_session
    def update_like_num(self, prid, num=1):
        # product = self.session.query(Product).filter_by(PRid=prid).first()
        # if product and product.PRfakelikenum:
        #     product.PRfakelikenum = product.PRfakelikenum + num
        #     self.session.add(product)
        return self.session.query(Product).filter(Product.PRid == prid).update({'PRfakelikenum': Product.PRfakelikenum + num})

    @close_session
    def get_products_by_prname(self, prname):
        return self.session.query(Product).filter(Product.PRtitle.like("%{0}%".format(prname))).all()

    @close_session
    def update_product_by_productid(self, productid, data):
        return self.session.query(Product).filter(Product.PRoductId == productid).update(data)

    @close_session
    def get_product_by_productid(self, productid):
        return self.session.query(Product).filter(
            Product.PRoductId == productid, Product.PRstatus == 1, Product.PRisdelete == False).first()

    @close_session
    def get_product_target_by_prid(self, prid):
        return self.session.query(ProductTarget).filter(ProductTarget.PRid == prid).all()

    @close_session
    def del_product_target_by_filter(self, ptfilter):
        """删除商品与模块的单条关联"""
        return self.session.query(ProductTarget).filter_by(**ptfilter).delete()

    @close_session
    def update_product_target_by_filter(self, ptfilter, ptinfo):
        """修改商品与专题的单条关联"""
        return self.session.query(ProductTarget).filter_by(**ptfilter).update(ptinfo)

    @close_session
    def get_product_baid_by_prid(self, prid):
        """通过prid获取商品关联的所有专题"""
        return self.session.query(ProductBigActivity).filter(ProductBigActivity.PRid == prid).all()

    @close_session
    def get_single_productbigactivity_by_filter(self, pbfilter):
        """获取商品与专题的单条关联"""
        return self.session.query(ProductBigActivity).filter_by(**pbfilter).first()

    @close_session
    def update_productbigactivity_by_filter(self, pbfilter, pbinfo):
        """修改商品与专题的单条关联"""
        return self.session.query(ProductBigActivity).filter_by(**pbfilter).update(pbinfo)

    @close_session
    def del_productbigactivity_by_filter(self, pbfilter):
        """删除商品与专题的单条关联"""
        return self.session.query(ProductBigActivity).filter_by(**pbfilter).delete()

    @close_session
    def get_product_operation_record(self, page_num, page_size, prid=None):
        """获取商品操作记录"""
        return self.session.query(ProductOperationRecord).filter_without_none(
            ProductOperationRecord.PRid == prid).order_by(
            ProductOperationRecord.PORcreatetime.desc()).all_with_page(page_num, page_size)

    @close_session
    def get_singel_record_by_filter(self, prfilter):
        """根据条件获取单条记录"""
        return self.session.query(ProductOperationRecord).filter_by(**prfilter).first()


if __name__ == '__main__':
    productid = '914'
    sp = SProduct()
    from WeiDian.models import model
    product = sp.session.query(Product).filter(Product.PRoductId==productid).first()
    sp.session.query(model.ProductSkuKey).filter(model.ProductSkuKey.PRid == product.PRid).delete()
    sp.session.query(model.ProductSkuValue).filter(model.ProductSkuValue.PRid == product.PRid).delete()
    sp.session.query(model.Product).filter(model.Product.PRid == product.PRid).delete()
    sp.session.query(model.ProductImage).filter(model.ProductImage.PRid == product.PRid).delete()
    sp.session.query(model.ProductTarget).filter(model.ProductTarget.PRid == product.PRid).delete()
    sp.session.commit()


