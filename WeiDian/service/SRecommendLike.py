# *- coding:utf8 *-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import RecommendLike
sys.path.append(os.path.dirname(os.getcwd()))


class SRecommendLike(SBase):

    @close_session
    def get_recommend_like_num_by_reid(self, reid):
        """获取推荐区域点赞数"""
        return self.session.query(RecommendLike).filter_by(REid=reid).count()

    @close_session
    def get_recommend_like_by_usidreid(self, usid, reid):
        return self.session.query(RecommendLike).filter_by(
            USid=usid, REid=reid).first()

    @close_session
    def del_like(self, usid, reid):
        """取消点赞"""
        return self.session.query(RecommendLike).filter_by(USid=usid, REid=reid).delete()
