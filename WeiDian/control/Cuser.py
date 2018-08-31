# *- coding:utf8 *-
import sys
import os
from flask import request
from WeiDian.common.token_required import verify_token_decorator, usid_to_token
from WeiDian.common.import_status import import_status
from WeiDian.service.SUser import SUser
from WeiDian.config.response import PARAMS_MISS, SYSTEM_ERROR
sys.path.append(os.path.dirname(os.getcwd()))


class CUser():

    def __init__(self):
        self.suser = SUser()

    def login(self):
        json_data = request.json
        if not json_data:
            return PARAMS_MISS
        usname = json_data.get('usname')
        uspassword = json_data.get('uspassword')
        if not usname or not uspassword:
            raise PARAMS_MISS('请输入用户名或密码')
        user = self.suser.verify_user(usname, uspassword)
        if not user:
            raise SYSTEM_ERROR('用户名或者密码错误')
        if user.USlevel == 0:
            level = 'ordinary'
        if user.USlevel > 0:
            level = 'partner'
        token = usid_to_token(user.USid)
        data = import_status('generic_token_success', "OK")
        data['data'] = {
            'token': token,
            'level': level,
        }
        return data
