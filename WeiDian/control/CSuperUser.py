# -*- coding:utf8 -*-
import sys
import os
import uuid

from WeiDian import logger
from WeiDian.common.params_require import parameter_required
from flask import request
from WeiDian.common.token_required import usid_to_token, verify_token_decorator, is_admin, is_superadmin
from WeiDian.common.import_status import import_status
from WeiDian.service.SSuperUser import SSuperUser
from WeiDian.config.response import PARAMS_MISS, SYSTEM_ERROR, AUTHORITY_ERROR, PARAMS_ERROR, NOT_FOUND
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
    def add_admin_by_superadmin(self):
        """超级管理员添加普通管理"""
        if not is_superadmin():
            raise AUTHORITY_ERROR(u'当前非超管权限')
        data = request.json
        logger.debug("add admin data is %s", data)
        parameter_required('suname', 'password', 'suheader')
        suid = str(uuid.uuid1())
        password = data.get('password')
        suname = data.get('suname')
        sulevel = data.get('sulevel')
        sulevel = 1 if not sulevel else int(sulevel)
        if sulevel not in [0, 1]:
            raise PARAMS_ERROR(u'sulevel参数错误')
        sufilter = {
            'SUisdelete': False,
            'SUname': suname
        }
        suexist = self.ssuperuser.get_existuser_by_name(sufilter)
        if suexist:
            raise SYSTEM_ERROR(u'用户名已存在')
        try:
            self.ssuperuser.add_model('SuperUser', **{
                'SUid': suid,
                'SUname': suname,
                'SUpassword': generate_password_hash(password),
                'SUheader': data.get('suheader'),
                'SUlevel': sulevel,
            })
            response = import_status("add_admin_success", "OK")
            response["data"] = {'suid': suid}
            return response
        except Exception as e:
            logger.exception("add admin error")
            raise SYSTEM_ERROR(u'添加管理员信息错误')

    @verify_token_decorator
    def get_all_admin_by_filter(self):
        """获取所有管理员"""
        if not is_admin():
            raise AUTHORITY_ERROR(u'当前非管理员账户')
        args = request.args.to_dict()
        logger.debug("get admin args is %s", args)
        parameter_required('sutype')
        sutype = args.get('sutype')
        if not sutype:
            sutype = 'normal'
        if str(sutype) not in ['all', 'normal', 'freeze']:
            raise PARAMS_ERROR('sutype error')
        if str(sutype) == 'normal':
            sufilter = {'SUisdelete': False,
                        'SUidfreeze': False
                        }
        elif str(sutype) == 'freeze':
            sufilter = {'SUisdelete': False,
                        'SUidfreeze': True
                        }
        else:
            sufilter = {'SUisdelete': False}
        logger.debug("query sutype is %s", sutype)
        suser_list = self.ssuperuser.get_all_super_by_sufilter(sufilter)

        for suser in suser_list:
            suser.fill(suser.SUlevel, 'sulevel')
            suser.fill(suser.SUid, 'suid')
            if suser.SUlevel == 0:
                suser.level = 'customerservice'
            if suser.SUlevel == 1:
                suser.level = 'ordinaryadmin'
            if suser.SUlevel == 2:
                suser.level = 'superadmin'
            suser.fill(suser.level, 'levelmeaning')
            if suser.SUidfreeze is True:
                suser.sustatus = 'freeze'
            else:
                suser.sustatus = 'normal'
            suser.fill(suser.sustatus, 'sustatus')
        response = import_status("messages_get_item_ok", "OK")
        response['data'] = suser_list
        return response

    @verify_token_decorator
    def superadmin_to_update_others(self):
        if not is_superadmin():
            raise AUTHORITY_ERROR(u'当前非超管权限')
        data = request.json
        logger.debug("update admin data is %s", data)
        parameter_required('suid')
        suid = data.get('suid')
        password = data.get('password')
        sulevel = data.get("sulevel")
        sulevel = 1 if not sulevel else int(sulevel)
        if sulevel not in [0, 1]:
            raise PARAMS_ERROR(u'sulevel参数错误')
        change_suser = self.ssuperuser.get_one_super_by_suid(suid)
        if not change_suser:
            raise NOT_FOUND(u'要修改的信息不存在')
        upinfo = {
            "SUid": suid,
            "SUpassword": generate_password_hash(password),
            "SUname": data.get("suname"),
            "SUheader": data.get("suheader"),
            "SUlevel": sulevel,
            "SUidfreeze": data.get("suisfreeze"),
            "SUisdelete": data.get("suisdelete")
        }
        upinfo = {k: v for k, v in upinfo.items() if v not in self.empty}
        changed = self.ssuperuser.update_info(suid, upinfo)
        if not changed:
            raise SYSTEM_ERROR(u"修改信息不存在")
        response = import_status("update_superinfo_success", "OK")
        response['data'] = {'suid': suid}
        return response

    @verify_token_decorator
    def update_suerinfo(self):
        """管理员修改自身账户信息"""
        if not is_admin():
            raise AUTHORITY_ERROR(u'当前非管理员账户')
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





