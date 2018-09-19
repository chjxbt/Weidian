# -*- coding:utf8 -*-
import json
import re
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))

import uuid
import datetime
from flask import request
from WeiDian import logger
from WeiDian.common.import_status import import_status
from WeiDian.common.params_require import parameter_required
from WeiDian.common.timeformat import get_db_time_str
from WeiDian.common.token_required import verify_token_decorator, is_tourist, is_admin
from WeiDian.config.enums import TASK_STATUS, TASK_TYPE
from WeiDian.config.response import AUTHORITY_ERROR, SYSTEM_ERROR, TOKEN_ERROR, PARAMS_ERROR
from WeiDian.control.BaseControl import BaseMyCenterControl


class CTask(BaseMyCenterControl):
    add_task_params = [
        'TAname', "TAtype", "TAhead", "TAlevel",
        "TArole", "TAcomplateNotifications", "RAid"]

    def __init__(self):
        from WeiDian.service.SProduct import SProduct
        self.sproduct = SProduct()
        from WeiDian.service.SUser import SUser
        self.suser = SUser()
        from WeiDian.service.STask import STask
        self.stask = STask()
        from WeiDian.service.SLevelRules import SLevelRules
        self.slevelrules = SLevelRules()
        from WeiDian.service.SUserAddress import SUserAddress
        self.suesraddress = SUserAddress()
        from WeiDian.service.SBankCard import SBankCard
        self.sbankcard = SBankCard()

    def get_all_task_type(self):
        return TASK_TYPE

    @verify_token_decorator
    def add_task(self):
        if not is_admin():
            raise AUTHORITY_ERROR(u"权限不足")
        data = request.json
        logger.info("add task body %s", data)
        parameter_required(*self.add_task_params)
        task = {k: data.get(k) for k in self.add_task_params}
        task_id = str(uuid.uuid1())
        logger.debug('get tatype is %s and type of tatype is %s', task.get("TAtype"), type(task.get("TAtype")))
        tatype = int(task.get("TAtype"))
        if tatype == 0 and "TAurl" not in data:
            raise PARAMS_ERROR("参数TAurl缺失")
        task['TAstartTime'] = get_db_time_str(data.get("TAstartTime"))
        if data.get("TAendTime"):
            task['TAendTime'] = get_db_time_str(data.get("TAendTime"))
        if data.get("TAduration"):
            task['TAduration'] = get_db_time_str(data.get("TAduration"))
        task['TAstatus'] = data.get("TAstatus", 0)
        task['TAmessage'] = data.get("TAmessage")
        task['TAid'] = task_id
        task['TAtype'] = tatype
        logger.debug('add task : task is %s', task)
        try:
            self.stask.add_model("Task", **task)
        except:
            logger.exception("add task error")
        return import_status("add_task_success", "OK")

    def

