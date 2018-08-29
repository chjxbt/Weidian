# *- coding:utf8 *-
import sys
import os

from SBase import SBase, close_session
from WeiDian.models.model import Recommend, RecommendProduct

sys.path.append(os.path.dirname(os.getcwd()))


class SRecommend(SBase):

    @close_session
    def get_recommend_list(self):
        """返回日推页商品区域信息, 列表"""
        recommend_list = self.session.query(Recommend).filter_by(REisdelete=False).order_by(Recommend.REcreatetime.desc()).all()
        # recommend = self.session.query(Recommend).filter_by(REisdelete=False).all()
        return recommend_list

    @close_session
    def get_recommend_by_reid(self, reid):
        recommend = self.session.query(Recommend).filter_by(REid=reid).first()
        return recommend

    @close_session
    def add_recommend(self, recommend):
        self.session.add(recommend)

    @close_session
    def del_recommend(self, reid):
        recommend = self.session.query(Recommend).filter_by(REid=reid).first()
        recommend.REisdelete = True
        self.session.add(recommend)

    @close_session
    def update_recommend(self, reid, **kwargs):
        recommend = self.session.query(Recommend).filter_by(REid=reid).first()
        self.session.query(RecommendProduct).filter_by(REid=reid).delete
        if recommend:
            if 'restarttime' in kwargs.keys():
                recommend.REstarttime = kwargs['restarttime']
            if 'reendtime' in kwargs.keys():
                recommend.REendtime = kwargs['reendtime']
            if 'reviewnum' in kwargs.keys():
                recommend.REfakeviewnum = kwargs['reviewnum']
            if 'relikenum' in kwargs.keys():
                recommend.RElikefakenum = kwargs['relikenum']
            self.session.add(recommend)
            return True


    @close_session
    def update_view_num(self, reid):
        recommend = self.session.query(Recommend).filter_by(REid=reid).first()
        recommend.REviewnum = recommend.REviewnum + 1
        if recommend.REfakeviewnum:
            recommend.REfakeviewnum = recommend.REfakeviewnum + 1
        self.session.add(recommend)
        self.session.commit()

    @close_session
    def add_like_num(self, reid):
        recommend = self.session.query(Recommend).filter_by(REid=reid).first()
        recommend.RElikenum = recommend.RElikenum + 1
        if recommend.RElikefakenum:
            recommend.RElikefakenum = recommend.RElikefakenum + 1
        self.session.add(recommend)
        self.session.commit()

    @close_session
    def del_like_num(self, reid):
        recommend = self.session.query(Recommend).filter_by(REid=reid).first()
        recommend.RElikenum = recommend.RElikenum - 1
        if recommend.RElikefakenum:
            recommend.RElikefakenum = recommend.RElikefakenum - 1
        self.session.add(recommend)
        self.session.commit()


    # @close_session
    # def update_like_num(self, reid):
    #     recommend = self.session.query(Recommend).filter_by(REid=reid).first()
    #     user_like_num = self.session.query(RecommendLike).count()
    #     recommend.RElikenum = recommend.RElikenum + 1
    #     if recommend.RElikefakenum:
    #         recommend.RElikefakenum = recommend.RElikefakenum + 1
    #     self.session.add(recommend)
    #     self.session.commit()

    # @close_session
    # def add_recommend(self, recommend):
    #     self.session.add(recommend)
    #
    # @close_session
    # def update_recommend(self):
    #     pass
    #
    # @close_session
    # def del_recommend(self):
    #     pass

