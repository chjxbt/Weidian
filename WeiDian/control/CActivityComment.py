# *- coding:utf8 *-
import sys
import os
import uuid
from datetime import datetime, timedelta

from flask import request

from WeiDian.config.messages import delete_activity_success, stop_activity_success
from sqlalchemy.orm import Session

from WeiDian.common.token_required import verify_token_decorator, is_admin, is_tourist
from WeiDian.common.TransformToList import dict_add_models
from WeiDian.common.import_status import import_status
from WeiDian.config.response import PARAMS_MISS, TOKEN_ERROR, AUTHORITY_ERROR, SYSTEM_ERROR


class CActivityComment():
    def __init__(self):
        from WeiDian.service.SActivityComment import SActivityComment
        self.sactivitycomment = SActivityComment()
        from WeiDian.service.SActivity import SActivity
        self.sactivity = SActivity()
        from WeiDian.service.SUser import SUser
        self.suser = SUser()

    @verify_token_decorator
    def add_comment(self):
        """添加评论数据"""
        comment = request.json
        if not comment:
            return PARAMS_MISS
        if is_tourist():
            return AUTHORITY_ERROR('未登录')
        comment['usid'] = request.user.id
        comment['acoid'] = str(uuid.uuid4())
        dict_add_models('ActivityComment', comment)
        data = import_status('add_activity_comment_success', 'OK')
        data['data'] = {
            'acoid': comment['acoid']
        }
        return data

    def get_comment_list(self):
        args = request.args.to_dict()
        acid = args.get('acid')
        if not acid:
            return PARAMS_MISS
        comment_list = self.sactivitycomment.get_comment_by_activity_id(acid)
        map(self.fill_user, comment_list)
        map(self.fill_comment_apply_for, comment_list)
        return comment_list

    def fill_user(self, comment):
        """给对象添加一个用户字段"""
        usid = comment.USid
        comment.user = self.suser.get_user_by_user_id(usid)  # 对象的用户
        comment.add('user').hide('USid')
        return comment

    def fill_comment_apply_for(self, comment):
        """"如果既是评论又是回复则添加一个'所回复用户'属性"""
        acoid = comment.ACOid
        if not comment.ACOparentid:
            return comment  # 如果ACOid没有值, 说明这不是回复的内容
        comment.parent_apply_user = self.sactivitycomment.get_apply_for_by_acoid(acoid)
        comment.add('parent_apply_user')
        return comment







