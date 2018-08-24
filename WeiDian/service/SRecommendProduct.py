# *- coding:utf8 *-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import RecommendProduct
sys.path.append(os.path.dirname(os.getcwd()))


class SRecommendProduct(SBase):
    @close_session
    def get_recommend_product_by_reid(self, reid):
        return self.session.query(RecommendProduct).filter_by(REid=reid).order_by(RecommendProduct.RPsort).all()
