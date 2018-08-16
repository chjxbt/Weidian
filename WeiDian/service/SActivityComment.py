# *- coding:utf8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
from SBase import SBase, close_session
from WeiDian.models.model import ActivityComment


class SActivityComment(SBase):

    @close_session
    def get_comment_by_activity_id(self, acid):
        """通过活动id获取下面的评论"""
        # return self.session.query(
        #     ActivityComment.ACOid,
        #     ActivityComment.ACid,
        #     ActivityComment.USid,
        #     ActivityComment.ACOcreatetime,
        #     ActivityComment.ACOparentid,
        #     ActivityComment.ACtext,
        # ).filter_by(ACid=acid).all()

        return self.session.query(
            ActivityComment
        ).filter_by(ACid=acid).all()


    @close_session
    def delete_comment_by_acoid(self, acoid):
        """删除单条评论"""
        cur_comment = self.session.query(ActivityComment).filter_by(ACOid=acoid)
        cur_comment.ACisdelete = True
        self.session.add(cur_comment)

    @close_session
    def add_comment(self, comment):
        """添加评论"""
        self.session.add(comment)
