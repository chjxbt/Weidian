# *- coding:utf8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
from SBase import SBase, close_session
from WeiDian.models.model import ActivityComment, User


class SActivityComment(SBase):

    @close_session
    def get_comment_by_activity_id(self, acid):
        """通过活动id获取下面的评论"""
        comment_list = self.session.query(ActivityComment).filter_by(ACid=acid, ACisdelete=False).order_by(ActivityComment.ACOcreatetime.desc())
        exists_comment = comment_list.first()
        if exists_comment:
            comment_list = comment_list.all()
            comment_list = filter(lambda x: x.ACid or x.ACOid, comment_list)
            map(lambda x: x.add('ACOparentid') if x.ACOparentid else x.add('ACid'), comment_list)
            return comment_list
        return []

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
        return '***'

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

