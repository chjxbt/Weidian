# *- coding:utf8 *-
import sys
import os

from WeiDian.common.MakeToken import verify_token_decorator
from WeiDian.common.TransformToList import add_model
from WeiDian.common.import_status import import_status
from WeiDian.config.messages import delete_topnav_success
from WeiDian.config.response import PARAMS_MISS, AUTHORITY_ERROR, TOKEN_ERROR

sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import uuid


class CTopNav():
    def __init__(self):
        from WeiDian.service.STopNav import STopNav
        self.s_topnav = STopNav()

    def get_all(self):
        res = self.s_topnav.get_all()
        data = import_status('get_nav_list_success', "OK")
        data['data'] = res
        return data

    @verify_token_decorator
    def add_one(self):
        """添加一个首页上部导航, 需要管理员的登录状态"""
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if request.user.scope != 'SuperUser':
            return AUTHORITY_ERROR  # 权限不足
        data = request.json
        tnid = str(uuid.uuid1())
        tnname = data.get('tnname')
        tsort = data.get('tsort')
        tnurl = data.get('tnurl')
        if not tnid or not tnname:
            return PARAMS_MISS
        add_model('TopNav', **{
            'TNid': tnid,
            'TNname': tnname,
            'TSort': tsort,
            'TNurl': tnurl
        })
        response_make_topnav = import_status('add_topnav_success', 'OK')
        response_make_topnav['data'] = {'tnid': tnid}
        return response_make_topnav

    @verify_token_decorator
    def del_one(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if request.user.scope != 'SuperUser':
            return AUTHORITY_ERROR  # 权限不足
        data = request.json
        tnid = data.get('tnid')
        if not tnid:
            return PARAMS_MISS
        try:
            self.s_topnav.del_topnav(tnid)
            return delete_topnav_success
        except Exception as e:
            pass