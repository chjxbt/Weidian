# -*- coding:utf8 -*-
import sys
import os
import re
sys.path.append(os.path.dirname(os.getcwd()))

import uuid
import datetime
from flask import request
from WeiDian import logger
from WeiDian.common.import_status import import_status
from WeiDian.common.params_require import parameter_required
from WeiDian.common.timeformat import get_db_time_str, format_for_db
from WeiDian.common.token_required import verify_token_decorator, is_tourist, is_admin
from WeiDian.config.enums import TASK_TYPE
from WeiDian.config.setting import QRCODEHOSTNAME
from WeiDian.config.response import AUTHORITY_ERROR, SYSTEM_ERROR, TOKEN_ERROR, PARAMS_ERROR
from WeiDian.control.BaseControl import BaseTask
import platform

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
            "TAlevel", "TArole", "TAcomplateNotifications", "reward"
        ]

    def get_all_task_type(self):
        response = import_status("get_task_success", "OK")
        task_type = []
        for tatype in TASK_TYPE:
            task_type.insert(int(tatype), TASK_TYPE.get(tatype))
        response['data'] = task_type
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
            raise PARAMS_ERROR(u"参数TAurl缺失")
        task['TAstartTime'] = get_db_time_str(data.get("TAstartTime"))
        if data.get("TAendTime"):
            task['TAendTime'] = get_db_time_str(data.get("TAendTime"))
        if data.get("TAduration"):
            task['TAduration'] = data.get("TAduration")
        task['TAstatus'] = data.get("TAstatus", 0)
        task['TAmessage'] = data.get("TAmessage")
        task['TAurl'] = data.get("TAurl", 1)
        task['TAtype'] = tatype
        logger.debug('add task : task is %s', task)
        try:
            if data.get("TAid"):
                update_result = self.stask.update_task(data.get("TAid"), task)
                if not update_result:
                    raise SYSTEM_ERROR(u"数据库异常")
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
        if not raward.get("raid") or not raward.get("ranumber"):
            return
        self.sraward.add_model("TaskRaward", **{
            "TRid": str(uuid.uuid1()),
            "TLid": tlid,
            "RAid": raward.get("raid"),
            "RAnumber": raward.get("ranumber")
        })

    @verify_token_decorator
    def get_user_task(self):
        if is_tourist():
            raise AUTHORITY_ERROR(u"未登录")
        task_list = self.stask.get_user_task_by_userid(request.user.id)
        if not task_list:
            return SYSTEM_ERROR(u'当前没有任务')

        # task_list = self.fill_task_detail(task) for task in task_list
        task_detail_list, task_list = task_list, []
        for task in task_detail_list:
            task_detail = self.fill_task_detail(task)
            if task_detail:
                task_list.append(task_detail)
        if not task_list:
            return SYSTEM_ERROR(u'当前没有任务')

        task_level = self.stask.get_task_level_by_tlid(task_list[0].TLid)
        if not task_level:
            raise SYSTEM_ERROR(u'任务正在更新，请稍后查看')
        logger.debug('get task list %s', dict(task_level))
        # from WeiDian.common.divide import Partner
        # pa = Partner()
        # role = pa.cf.get(task_level, 'role')
        # cn = pa.cf.get(task_level, 'access')

        # map(self.fill_reward, task_list)
        is_complate = not  bool(len([task.TUstatus for task in task_list if task.TUstatus == 0]))
        # logger.debug(len(is_complate))
        # logger.debug(request.user.id)
        # logger.debug(len(task_list))
        response = import_status("get_task_success", "OK")
        if is_complate:
            # 更新任务状态为已失效，发放奖励。并且添加新的任务内容
            self.stask.update_user_tasks(request.user.id, {"TUstatus": 4})
            self.add_user_task_raward(request.user.id, task_level.TLid)
            if task_level.TAlevel < 3:
                self.add_user_task(request.user.id, task_level.TAlevel)
        response['RAward'] = self.fill_reward(task_level)
        response['data'] = task_list
        response['TArole'] = task_level.TArole
        response['TAcomplateNotifications'] = task_level.TAcomplateNotifications
        response['is_complate'] = is_complate

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
        logger.info('get task : %s', dict(task))

        if str(task.TAtype) == '0':
            logger.debug('start update task')
            # self.add_user_task_raward(request.user.id, task.TLid)
            update_result = self.stask.update_user_task(user_task.TUid, {"TUstatus": 1, "TUnumber": 1})
            logger.debug('get update result %s', update_result)
        else:
            # todo 其他类型任务执行
            pass
        # todo_task = self.stask.get_todo_user_task_by_user_id(request.user.id)
        # is_complate = False
        # if not todo_task:
        #     is_complate = True
        #     # 更新任务状态为已失效，发放奖励。并且添加新的任务内容
        #     self.stask.update_user_tasks(request.user.id, {"TUstatus": 4})
        #     if task.TAlevel < 3:
        #         self.add_user_task(request.user.id, task.TAlevel)
        # response = import_status("do_task_success", 'OK')
        # response['data'] = {
        #     "is_complate": is_complate
        # }
        return import_status("do_task_success", 'OK')

    # @verify_token_decorator
    # def get_reward(self):
    #     if is_tourist():
    #         return AUTHORITY_ERROR(u'未登录')

    def add_user_task_raward(self, usid, tlid):
        taskraward_list = self.sraward.get_raward_by_tlid(tlid)
        for taskraward in taskraward_list:
            self.sraward.add_model("UserRaward", **{
                "URid": str(uuid.uuid1()),
                "RAid": taskraward.RAid,
                "USid": usid,
                "RAnumber": taskraward.RAnumber,
            })

    def add_user_task(self, usid, task_level):
        task_level_after = self.stask.get_tasklevel_by_level(int(task_level) + 1)
        task_list = self.stask.get_task_by_tlid(task_level_after.TLid)
        self.add_user_task_detail(usid, task_list)

        if int(task_level) == 1:
            tlid = self.stask.get_tasklevel_by_level(4)
            task_list = self.stask.get_task_by_tlid(tlid.TLid)
            self.add_user_task_detail(usid, task_list)

    def add_user_task_detail(self, usid, task_list):
        for task in task_list:
            duration = task.TAduration
            duration_end = None
            if duration:
                duration_end = (datetime.datetime.now() + datetime.timedelta(days=int(duration))).strftime(format_for_db)

            endtime = None
            if duration_end and task.TAendTime:
                endtime = min(task.TAendTime, duration_end)
            elif duration_end:
                endtime = duration_end
            elif task.TAendTime:
                endtime = task.TAendTime

            self.stask.add_model("TaskUser", **{
                "TUid": str(uuid.uuid1()),
                "USid": usid,
                "TAid": task.TAid,
                "TUendtime": endtime,
                "TUstatus": 0,
                "TUnumber": 0
            })

    @verify_token_decorator
    def get_all_task(self):
        if not is_admin():
            raise AUTHORITY_ERROR(u"权限不足")

        task_list = self.stask.get_task_all()
        map(self.fill_reward, task_list)
        # map(self.fill_task_params, task_list)
        task_list = [self.fill_task_params(_task) for _task in task_list]
        task_list = [_task for _task in task_list if _task]
        response = import_status("get_task_success", "OK")
        response['data'] = task_list
        return response

    @verify_token_decorator
    def get_all_raward(self):
        if not is_admin():
            raise AUTHORITY_ERROR(u"权限不足")

        raward_list = self.sraward.get_all_reward()
        raward_list = self.fill_reward_detail(raward_list)
        res = import_status('get_task_success', 'OK')
        res['data'] = raward_list
        return res

    @verify_token_decorator
    def get_all_task_level(self):
        if not is_admin():
            raise AUTHORITY_ERROR(u"未登录")
        try:
            task_level_list = self.stask.get_task_level_all()
            map(self.fill_reward, task_level_list)
            response = import_status('get_task_success', 'OK')
            response['data'] = task_level_list
        except:
            logger.exception('get all task level error')
            raise SYSTEM_ERROR(u"服务器繁忙")
        return response

    @verify_token_decorator
    def upload_task_img(self):
        if not is_admin():
            raise AUTHORITY_ERROR(u"权限不足")
        formdata = request.form
        logger.info("formdata is %s", formdata)
        files = request.files.get("file")

        if platform.system() == "Windows":
            rootdir = "D:/task"
        else:
            rootdir = "/opt/WeiDian/imgs/task/"
        if not os.path.isdir(rootdir):
            os.mkdir(rootdir)
        # if "FileType" not in formdata:
        #     return
        filessuffix = str(files.filename).split(".")[-1]
        # index = formdata.get("index", 1)
        filename = request.user.id + get_db_time_str() + "." + filessuffix
        filepath = os.path.join(rootdir, filename)
        print(filepath)
        files.save(filepath)
        response = import_status("save_photo_success", "OK")
        # url = Inforcode.ip + Inforcode.LinuxImgs + "/" + filename
        url = QRCODEHOSTNAME + "/imgs/task/" + filename
        # print(url)
        logger.info("this url is %s", url)
        response["data"] = url
        return response

    @verify_token_decorator
    def get_all_user_task(self):
        if not is_admin():
            raise AUTHORITY_ERROR(u'权限不足')
        user_task = self.stask.get_all_user_task()
        user_task = [self.fill_task_detail(_task) for _task in user_task]
        user_task = [_task for _task in user_task if _task]
        return user_task

    @verify_token_decorator
    def del_task(self):
        if not is_admin():
            raise AUTHORITY_ERROR(u'权限不足')
        data = request.json
        parameter_required("TAid")
        logger.debug('get del task data, %s', data)
        update_result = self.stask.update_task(data.get("TAid"), {"TAstatus": 4})
        if not update_result:
            raise SYSTEM_ERROR(u'数据库异常')
        return import_status("delete_success", "OK")

    @verify_token_decorator
    def del_task_level(self):
        if not is_admin():
            raise AUTHORITY_ERROR(u'权限不足')
        data = request.json
        parameter_required("tlid")
        logger.debug('get del task level data, %s', data)
        tasklevel = self.stask.get_task_level_by_tlid(data.get("tlid"))
        if not tasklevel:
            return SYSTEM_ERROR(u'该任务等级不存在或已删除')
        self.stask.update_task_by_tlid(tasklevel.TLid, {"TAstatus": 4})
        self.stask.update_task_level(data.get("tlid"), {"TLisdelete": True})

        return import_status("delete_success", "OK")