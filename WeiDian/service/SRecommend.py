# *- coding:utf8 *-
import sys
import os

from SBase import SBase, close_session
from WeiDian.models.model import Recommend
sys.path.append(os.path.dirname(os.getcwd()))


class SRecommend(SBase):

    @close_session
    def get_recommend(self):
        """返回日推页商品区域所有信息"""
        recommend_list = self.session.query(Recommend).filter_by(REisdelete=False).order_by(Recommend.REcreatetime.desc()).all()
        return recommend_list

    @close_session
    def add_recommend(self, recommend):
        self.session.add(recommend)

    @close_session
    def update_recommend(self):
        pass

    @close_session
    def del_recommend(self):
        pass

