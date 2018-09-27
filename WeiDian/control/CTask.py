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
from WeiDian.control.BaseControl import BaseTask


class CTask(BaseTask):

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
        from WeiDian.service.SRaward import SRaward
        self.sraward = SRaward()
        self.add_task_params = [
            'TAname', "TAtype", "TAhead", "TLid"]
        self.do_task_params = [
            "TUid"
        ]
        self.add_task_level = [
            "TLevel", "TArole", "TAcomplateNotifications", "raward"
        ]

    def get_all_task_type(self):
        response = import_status("get_task_success", "OK")
        response['data'] = TASK_TYPE
        return response

    @verify_token_decorator
    def add_task(self):
        if not is_admin():
            raise AUTHORITY_ERROR(u"权限不足")
        data = request.json
        logger.info("add task body %s", data)
        parameter_required(*self.add_task_params)
        task = {k: data.get(k) for k in self.add_task_params}

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
        task['TAurl'] = data.get("TAurl", 1)
        task['TAtype'] = tatype
        logger.debug('add task : task is %s', task)
        try:
            if data.get("TAid"):
                update_result = self.stask.update_task(data.get("TAid"), task)
                if not update_result:
                    raise SYSTEM_ERROR("数据库异常")
                task["TAid"] = data.get("TAid")
            else:
                task['TAid'] = str(uuid.uuid1())
                self.stask.add_model("Task", **task)
            # self.add_or_update_task_raward(task['TAid'], task['RAid'], task.get("RAnumber", 1))
        except:
            logger.exception("add task error")
            return SYSTEM_ERROR(u'服务器繁忙')
        return import_status("add_task_success", "OK")

    @verify_token_decorator
    def add_or_update_task_level(self):
        if not is_admin():
            raise AUTHORITY_ERROR(u"权限不足")
        parameter_required(*self.add_task_level)
        data = request.json
        logger.debug('get request data : %s', data)
        reward_list = data.get("reward")
        try:
            tasklevel = self.stask.get_tasklevel_by_level(int(data.get("TAlevel")))

            if not tasklevel:
                tlid = str(uuid.uuid1())
                self.stask.add_model("TaskLevel", **{
                    "TLid": tlid,
                    "TAlevel": data.get("TAlevel"),
                    "TArole": data.get("TArole"),
                    "TAcomplateNotifications": data.get("TAcomplateNotifications"),
                })
                for reward in reward_list:
                    self.add_task_raward(tlid, reward)

            else:
                update_result = self.stask.update_task_level(tasklevel.TLid, {
                    "TAlevel": data.get("TAlevel", 0),
                    "TArole": data.get("TArole"),
                    "TAcomplateNotifications": data.get("TAcomplateNotifications")})
                if not update_result:
                    return import_status("update_data_error", "WEIDIAN_ERROR", "error_update_data")
                self.sraward.delte_task_raward_by_tlid(tasklevel.TLid)
                for reward in reward_list:
                    self.add_task_raward(tasklevel.TLid, reward)
            return import_status('add_task_success', 'OK')
        except:
            logger.exception('add or update task level error')
            return SYSTEM_ERROR(u"服务器繁忙")

    # def add_or_update_task_raward(self, taid, raid, ranumber):
    #     self.sraward.delte_task_raward_by_taid(taid)
    #     self.sraward.add_model("TaskRaward", **{
    #         "TRid": str(uuid.uuid1()),
    #         "TAid": taid,
    #         "RAid": raid,
    #         "RAnumber": ranumber
    #     })

    def add_task_raward(self, tlid, raward):
        if not raward.get("RAid") or not raward.get("RAnumber"):
            return
        self.sraward.add_model("TaskRaward", **{
            "TRid": str(uuid.uuid1()),
            "TLid": tlid,
            "RAid": raward.get("RAid"),
            "RAnumber": raward.get("RAnumber")
        })

    @verify_token_decorator
    def get_user_task(self):
        if is_tourist():
            raise AUTHORITY_ERROR(u"未登录")
        task_list = self.stask.get_user_task_by_userid(request.user.id)
        if not task_list:
            return SYSTEM_ERROR(u'r当前没有任务')

        map(self.fill_task_detail, task_list)
        task_level = self.stask.get_task_level_by_tlid(task_list[0].TLid)
        # from WeiDian.common.divide import Partner
        # pa = Partner()
        # role = pa.cf.get(task_level, 'role')
        # cn = pa.cf.get(task_level, 'access')

        map(self.fill_reward, task_list)
        is_complate = [task.TUstatus for task in task_list if task.TUstatus > 0]
        # logger.debug(len(is_complate))
        # logger.debug(request.user.id)
        # logger.debug(len(task_list))
        response = import_status("get_task_success", "OK")

        response['data'] = task_list
        response['TArole'] = task_level.TArole
        response['TAcomplateNotifications'] = task_level.TAcomplateNotifications
        response['is_complate'] = bool(len(is_complate) == len(task_list))

        return response

    @verify_token_decorator
    def do_task(self):
        if is_tourist():
            raise AUTHORITY_ERROR(u"未登录")
        parameter_required(*self.do_task_params)
        data = request.json
        logger.debug("get data %s", data)
        user_task = self.stask.get_user_task_by_id(data.get("TUid"))
        logger.info('get user task %s', user_task)
        if not user_task:
            raise SYSTEM_ERROR(u"服务器繁忙")
        task = self.stask.get_task_by_taid(user_task.TAid)
        logger.info('get task : %s', task)

        if task.TAtype == '0':
            self.add_user_task_raward(request.user.id, task.TAid)
            self.stask.update_user_task(user_task.TUid, {"TUstatus": 1})
        else:
            # todo 其他类型任务执行
            pass
        todo_task = self.stask.get_todo_user_task_by_user_id(request.user.id)
        if not todo_task:
            # 更新任务状态为已失效。并且添加新的任务内容
            self.stask.update_user_tasks(request.user.id, {"TUstatus": 4})
            if task.TAlevel < 3:
                self.add_user_task(request.user.id, task.TAlevel)

        return import_status("do_task_success", 'OK')

    def add_user_task_raward(self, usid, taid):
        taskraward = self.sraward.get_raward_by_taid(taid)
        self.sraward.add_model("UserRaward",**{
            "URid": str(uuid.uuid1()),
            "RAid": taskraward.RAid,
            "USid": usid,
            "RAnumber": taskraward.RAnumber,
        })

    def add_user_task(self, usid, task_level):
        task_list = self.stask.get_task_by_level(int(task_level) + 1)
        for task in task_list:
            # todo 结束时间计算
            # endtime = min(task.TAendTime, )
            self.stask.add_model("TaskUser", **{
                "TUid": str(uuid.uuid1()),
                "USid": usid,
                "TAid": task.TAid,
                "TUendtime": task.TAendTime,
                "TUstatus": 0,
                "TUnumber": 0
            })

    @verify_token_decorator
    def get_all_task(self):
        if not is_admin():
            raise AUTHORITY_ERROR(u"权限不足")

        task_list = self.stask.get_task_all()
        map(self.fill_reward, task_list)
        map(self.fill_task_params, task_list)
        response = import_status("get_task_success", "OK")
        response['data'] = task_list
        return response

    @verify_token_decorator
    def get_all_raward(self):
        if not is_admin():
            raise AUTHORITY_ERROR(u"权限不足")

        raward_list = self.sraward.get_raward_by_taid

