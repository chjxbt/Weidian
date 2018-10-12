# *- coding:utf8 *-
import sys
import os
import uuid
from flask import request
from datetime import datetime, timedelta

from WeiDian.common.loggers import generic_log
from WeiDian.common.params_require import parameter_required
from WeiDian.common.timeformat import format_for_db
from WeiDian.config.messages import delete_activity_success, stop_activity_success
from sqlalchemy.orm import Session
from WeiDian.common.token_required import verify_token_decorator, is_admin, is_tourist
from WeiDian.common.TransformToList import dict_add_models
from WeiDian.common.import_status import import_status
from WeiDian.config.response import PARAMS_MISS, TOKEN_ERROR, AUTHORITY_ERROR, SYSTEM_ERROR, NOT_FOUND
from WeiDian.control.BaseControl import BaseActivityCommentControl
sys.path.append(os.path.dirname(os.getcwd()))


class CActivityComment(BaseActivityCommentControl):
    def __init__(self):
        from WeiDian.service.SActivityComment import SActivityComment
        self.sactivitycomment = SActivityComment()
        from WeiDian.service.SActivity import SActivity
        self.sactivity = SActivity()
        from WeiDian.service.SUser import SUser
        self.suser = SUser()
        from WeiDian.service.SSuperUser import SSuperUser
        self.ssuperuser = SSuperUser()

    @verify_token_decorator
    def add_comment(self):
        """添加评论数据"""
        if is_tourist():
            return AUTHORITY_ERROR(u'未登录')
        data = parameter_required(u'ACtext')
        acid = data.get('acid')
        acoid = data.get('acoid')
        usid = request.user.id
        actext = data.get('ACtext')
        # 添加评论
        if acid:
            activity = self.sactivity.get_activity_by_acid(acid)
            if not activity:
                raise NOT_FOUND(u'推文不存在')
            model_data = {
                'ACOid': str(uuid.uuid4()),
                'ACid': acid,
                'USid': usid,
                'ACtext': actext,
                'ACOcreatetime': datetime.strftime(datetime.now(), format_for_db)
            }
        # 如果是添加回复
        elif acoid:
            if not is_admin():
                raise TOKEN_ERROR(u'请使用管理员回复')
            comment = self.sactivitycomment.get_comment_by_acoid(acoid)
            if not comment:
                raise NOT_FOUND(u'不存在的评论')
            acid = comment.ACid
            model_data = {
                'ACOid': str(uuid.uuid4()),
                'ACid': acid,
                'ACOparentid': acoid,
                'USid': request.user.id,
                'ACtext': actext,
                'ACOcreatetime': datetime.strftime(datetime.now(), format_for_db)
            }
        else:
            raise PARAMS_MISS(u'请指定回复类型')
        self.sactivity.add_model('ActivityComment', **model_data)
        data = import_status('add_activity_comment_success', 'OK')
        data['data'] = {
            'acoid': model_data['ACOid']
        }
        return data

    def get_comment_list(self):
        """获取评论列表"""
        try:
            args = request.args.to_dict()
            acid = args.get('acid')
            if not acid:
                raise PARAMS_MISS(u'必要的参数缺失: acid;')
            reply = True if args.get('reply') else False
            page = int(args.get('page', 1))  # 页码
            # start = int(args.get('start', 0))  # 起始位置
            count = int(args.get('count', 15))  # 取出条数
            # if not start:
            #     start = (page -1) * count
            comment_list = self.sactivitycomment.get_comment_by_activity_id(acid, page, count, reply)
            # end = start + count
            # len_comment_list = len(comment_list)
            # if end > len_comment_list:
            #     end = len_comment_list
            # comment_list = comment_list[start: end]
            map(self.fill_user, comment_list)
            map(self.fill_comment_apply_for, comment_list)
            data = import_status('get_acvity_comment_list_success', 'OK')
            data['data'] = comment_list
            return data
        except Exception as e:
            generic_log(e)
            raise e

    def get_comment_with_apply(self):
        """获取推文的评论列表(评论回复嵌套)"""
        try:
            args = request.args.to_dict()
            acid = args.get('acid')
            if not acid:
                raise PARAMS_MISS(u'必要的参数缺失: acid;')
            page = int(args.get('page', 1))  # 页码
            count = int(args.get('count', 15))  # 取出条数
            comment_list = self.sactivitycomment.get_comment_by_activity_id(acid, page, count)
            for comment in comment_list:
                self.fill_user(comment)
                reply = self.sactivitycomment.get_apply_by_acoid(comment.ACOid)
                if reply:
                    comment.fill(reply, 'reply')
                    # 改: 所有的回复都是管理员回复
                    admin_user = self.ssuperuser.get_one_super_by_suid(reply.USid)
                    if admin_user:
                        user = admin_user
                        admin_user.fill(0, 'robot')
                    else:
                        user = {
                            'name': u'运营人员',
                            'robot': 1
                        }
                    reply.fill(user, 'user')
            data = import_status('get_acvity_comment_list_success', 'OK')
            data['data'] = comment_list
            data["count"] = request.all_count
            data["page_count"] = request.page_count
            return data
        except Exception as e:
            generic_log(e)
            raise e

