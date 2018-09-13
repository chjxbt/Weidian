# -*- coding:utf8 -*-
import re
import sys
import os

from WeiDian import logger
from WeiDian.common.import_status import import_status
from WeiDian.common.token_required import verify_token_decorator, is_tourist
from WeiDian.config.response import AUTHORITY_ERROR, SYSTEM_ERROR
from WeiDian.control.BaseControl import BaseMyCenterControl
from flask import request
sys.path.append(os.path.dirname(os.getcwd()))


class CMyCenter(BaseMyCenterControl):
    def __init__(self):
        from WeiDian.service.SProduct import SProduct
        self.sproduct = SProduct()
        from WeiDian.service.SUser import SUser
        self.suser = SUser()
        from WeiDian.service.SMyCenter import SMyCenter
        self.smycenter = SMyCenter()
        from WeiDian.service.SLevelRules import SLevelRules
        self.slevelrules = SLevelRules()


    @verify_token_decorator
    def get_info(self):
        if is_tourist():
            return AUTHORITY_ERROR(u"未登录")
        try:
            my_info = self.smycenter.get_my_info_by_usid(request.user.id)
            my_info = self.fill_user_info(my_info)
            data = import_status("get_my_info_success", "OK")
            data["data"] = my_info
            return data
        except:
            logger.exception("get myinfo error")
            return SYSTEM_ERROR

    @verify_token_decorator
    def get_levelrules(self):
        if is_tourist():
            return AUTHORITY_ERROR(u"未登录")
        # try:
        #     with open('WeiDian/config/levelrules.cfg', 'r') as f:
        #         lr = f.read()
        #     lr = re.sub('\s', '', lr)
        #     data = import_status("get_levelrules_success", "OK")
        #     data["data"] = lr
        #     return data
        # except:
        #     logger.exception("get level rules error")
        #     return SYSTEM_ERROR
        try:
            lr_list = self.slevelrules.get_rule_list()
            map(lambda x: setattr(x, 'LRtext', re.sub('\s', '', x.LRtext)), lr_list)
            user = self.suser.get_user_by_user_id(request.user.id)
            if user.USlevel == 0:
                user.level = 'ordinary'
            if user.USlevel > 0:
                user.level = 'partner'
            user.add('level').hide('USid', 'USname', 'USheader')
            data = import_status("get_levelrules_success", "OK")
            data['data'] = lr_list
            data['userlevel'] = user.level
            return data
        except:
            logger.exception("get level rules error")
            return SYSTEM_ERROR



