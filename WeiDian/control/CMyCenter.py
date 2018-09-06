# -*- coding:utf8 -*-
import sys
import os

from WeiDian.common.import_status import import_status
from WeiDian.common.token_required import verify_token_decorator, is_tourist
from WeiDian.config.response import AUTHORITY_ERROR
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

    @verify_token_decorator
    def get_info(self):
        if is_tourist():
            return AUTHORITY_ERROR(u"未登录")
        print '已登录'
        my_info = self.smycenter.get_my_info_by_usid(request.user.id)
        my_info = self.fill_user_info(my_info)
        data = import_status("get_my_info_success", "OK")
        data["data"] = my_info
        return data




