# *- coding:utf8 *-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import ActivityComment, User
sys.path.append(os.path.dirname(os.getcwd()))


class SActivityComment(SBase):

    @close_session
    def get_comment_by_activity_id(self, acid):
        """通过活动id获取下面的评论和回复"""
        comment_list = self.session.query(ActivityComment).filter_by(ACid=acid, ACisdelete=False).order_by(ActivityComment.ACOcreatetime.desc()).all()
        return comment_list

    @close_session
    def get_comment_by_acoid(self, acoid):
        """通过acoid获取评论"""
        comment = self.session.query(ActivityComment).filter_by(ACOid=acoid, ACisdelete=False).first()
        return comment

    @close_session
    def get_apply_for_by_acoid(self, acoid):
        """通过评论id获取所回复的用户"""
        cur_apply = self.session.query(ActivityComment).filter_by(ACOid=acoid).first()
        if cur_apply:
            parent_apply = self.session.query(ActivityComment).filter_by(ACOid=cur_apply.ACOid).first()
            if parent_apply:
                parent_apply_user = self.session.query(User).filter_by(USid=parent_apply.USid).first()
                if parent_apply_user:
                    return parent_apply_user

    @close_session
    def delete_comment_by_acoid(self, acoid):
        """删除单条评论"""
        return self.session.query(ActivityComment).filter_by(ACOid=acoid).update({ActivityComment.ACisdelete: True})

    @close_session
    def add_comment(self, comment):
        """添加评论"""
        self.session.add(comment)
