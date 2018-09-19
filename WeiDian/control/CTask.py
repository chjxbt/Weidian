# -*- coding:utf8 -*-
import json
import re
import sys
import os
import uuid

from WeiDian import logger
from WeiDian.common.import_status import import_status
from WeiDian.common.params_require import parameter_required
from WeiDian.common.token_required import verify_token_decorator, is_tourist, is_admin
from WeiDian.config.enums import BANK_MAP
from WeiDian.config.response import AUTHORITY_ERROR, SYSTEM_ERROR, TOKEN_ERROR, PARAMS_ERROR
from WeiDian.control.BaseControl import BaseMyCenterControl
from flask import request

sys.path.append(os.path.dirname(os.getcwd()))


class CTask(BaseMyCenterControl):
    add_task_params = ['TAname', "TAtype", "TAhead", "TAlevel", "TArole", "TAcomplateNotifications"]

    def __init__(self):
        from WeiDian.service.SProduct import SProduct
        self.sproduct = SProduct()
        from WeiDian.service.SUser import SUser
        self.suser = SUser()
        from WeiDian.service.SMyCenter import SMyCenter
        self.smycenter = SMyCenter()
        from WeiDian.service.SLevelRules import SLevelRules
        self.slevelrules = SLevelRules()
        from WeiDian.service.SUserAddress import SUserAddress
        self.suesraddress = SUserAddress()
        from WeiDian.service.SBankCard import SBankCard
        self.sbankcard = SBankCard()

    @verify_token_decorator
    def add_task(self):
        if not is_admin():
            return AUTHORITY_ERROR(u"权限不足")

