# *- coding:utf8 *-
import sys
import os

from SBase import SBase, close_session
from WeiDian.models.model import Recommend
sys.path.append(os.path.dirname(os.getcwd()))


class SRecommend(SBase):

    @close_session
    def get_recommend_by_reid(self, reid):
        """返回日推页商品区域信息"""
        # recommend_list = self.session.query(Recommend).filter_by(REid=reid, REisdelete=False).order_by(Recommend.REcreatetime.desc()).all()
        recommend = self.session.query(Recommend).filter_by(REid=reid, REisdelete=False).all()
        return recommend

    @close_session
    def update_view_num(self, reid):
        recommend = self.session.query(Recommend).filter_by(REid=reid).first()
        recommend.REviewnum = recommend.REviewnum + 1
        if recommend.REfakeviewnum:
            recommend.REfakeviewnum = recommend.REfakeviewnum + 1
        self.session.add(recommend)
        self.session.commit()

    @close_session
    def add_recommend(self, recommend):
        self.session.add(recommend)

    @close_session
    def update_recommend(self):
        pass

    @close_session
    def del_recommend(self):
        pass

