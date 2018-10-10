# -*- coding:utf8 -*-
import sys
import os

from WeiDian import logger
from WeiDian.common.params_require import parameter_required
from flask import request
from WeiDian.common.token_required import usid_to_token, verify_token_decorator, is_admin
from WeiDian.common.import_status import import_status
from WeiDian.service.SSuperUser import SSuperUser
from WeiDian.config.response import PARAMS_MISS, SYSTEM_ERROR, AUTHORITY_ERROR, PARAMS_ERROR
from werkzeug.security import generate_password_hash

sys.path.append(os.path.dirname(os.getcwd()))


class CSuperUser():
    def __init__(self):
        self.ssuperuser = SSuperUser()
        self.empty = ['', None, [], {}]


    def login(self):
        """超级用户登录"""
        json_data = request.json
        suname = json_data.get('suname').encode('utf8')
        supassword = json_data.get('supassword')
        logger.debug("super user login data is %s", json_data)
        # if not suname or not supassword:
        #     return PARAMS_MISS
        parameter_required('suname', 'supassword')
        try:
            suuser = self.ssuperuser.verify_super(suname, supassword)
            # if not suuser:
            #     return SYSTEM_ERROR
            if suuser.SUlevel == 0:
                level = 'customerservice'
            if suuser.SUlevel == 1:
                level = 'ordinaryadmin'
            if suuser.SUlevel == 2:
                level = 'superadmin'
            token = usid_to_token(suuser.SUid, 'SuperUser')
            token_data = {
                'token': token,
                'level': level,
                'head': suuser.SUheader
            }
            data = import_status('generic_token_success', 'OK')
            data['data'] = token_data
            return data
        except:
            logger.exception('super user login in error')
            raise SYSTEM_ERROR(u'用户名或密码错误')

    @verify_token_decorator
    def update_suerinfo(self):
        if not is_admin():
            raise AUTHORITY_ERROR(u'当前非管理员权限')
        data = request.json
        suid = request.user.SUid
        old_suname = request.user.SUname
        new_suname = data.get('suname')
        if new_suname:
            new_suname = new_suname.encode('utf8')
        old_password = data.get('oldpassword')
        new_password = data.get('newpassword')
        avatar = data.get('head')
        logger.debug("update info is %s", data)
        # parameter_required('suname', 'head')
        if old_password and new_password:
            suuser = self.ssuperuser.verify_super(old_suname, old_password)
            if not suuser:
                raise PARAMS_ERROR(u'原密码错误')
            password = generate_password_hash(new_password)
            info = {'SUname': new_suname,
                    'SUpassword': password,
                    'SUheader': avatar
                    }
            info = {k: v for k, v in info.items() if v not in self.empty}
            update_info = self.ssuperuser.update_info(suid, info)
            if not update_info:
                raise SYSTEM_ERROR()
        else:
            info = {
                'SUname': new_suname,
                'SUheader': avatar
            }
            info = {k: v for k, v in info.items() if v not in self.empty}
            update_info = self.ssuperuser.update_info(suid, info)
            if not update_info:
                raise SYSTEM_ERROR(u"修改信息错误")
        response = import_status("update_superinfo_success", "OK")
        response['data'] = {'suid': suid}
        return response





