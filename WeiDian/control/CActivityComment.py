# *- coding:utf8 *-
import uuid
from datetime import datetime, timedelta

from flask import request

from WeiDian.config.messages import delete_activity_success, stop_activity_success
from sqlalchemy.orm import Session

from WeiDian.common.token_required import verify_token_decorator, is_admin, is_tourist
from WeiDian.common.TransformToList import dict_add_models
from WeiDian.common.import_status import import_status
from WeiDian.config.response import PARAMS_MISS, TOKEN_ERROR, AUTHORITY_ERROR, SYSTEM_ERROR
from WeiDian.control.BaseControl import BaseActivityCommentControl


class CActivityComment(BaseActivityCommentControl):
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
        if 'acoid' not in comment and not 'acoparentid' not in comment:
            return PARAMS_MISS('请指定回复或评论')
        if 'acid' not in comment:  # 如果传来的数据不存在acid, 存数据库的使用要填充上
            comment['acid'] = self.sactivitycomment.get_comment_by_acoid(comment['acoparentid']).ACid
        dict_add_models('ActivityComment', comment)
        data = import_status('add_activity_comment_success', 'OK')
        data['data'] = {
            'acoid': comment['acoid']
        }
        return data

    def get_comment_list(self):
        """获取评论列表"""
        args = request.args.to_dict()
        acid = args.get('acid')
        if not acid:
            return PARAMS_MISS
        page = int(args.get('page', 1))  # 页码
        start = int(args.get('start', 0))  # 起始位置
        count = int(args.get('count', 15))  # 取出条数
        if not start:
            start = (page -1) * count
        comment_list = self.sactivitycomment.get_comment_by_activity_id(acid)
        end = start + count
        len_comment_list = len(comment_list)
        if end > len_comment_list:
            end = len_comment_list
        comment_list = comment_list[start: end]
        map(self.fill_user, comment_list)
        map(self.fill_comment_apply_for, comment_list)
        data = import_status('get_acvity_comment_list_success', 'OK')
        data['data'] = comment_list
        return data

