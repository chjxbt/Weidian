# *- coding:utf8 *-
import sys
import os
from datetime import datetime

from sqlalchemy.orm import Session

from WeiDian.common.import_status import import_status
from WeiDian.common.timeformat import format_for_db
from WeiDian.config.response import PARAMS_MISS
from WeiDian.control.BaseControl import BaseActivityControl

sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import json
import uuid


class CActivity(BaseActivityControl):
    def __init__(self):
        from WeiDian.service.SActivity import SActivity
        self.sactivity = SActivity()
        from WeiDian.service.SActivityComment import SActivityComment
        self.sacomment = SActivityComment()
        from WeiDian.service.SActivityLike import SActivityLike
        self.salike = SActivityLike()
        from WeiDian.service.SSuperUser import SSuperUser
        self.ssuperuser = SSuperUser()
        from WeiDian.service.SActivityMedia import SActivityMedia
        self.smedia = SActivityMedia()
        from WeiDian.service.SActivityTag import SActivityTag
        self.stags = SActivityTag()
        from WeiDian.service.SActivityFoward import SActivityFoward
        self.foward = SActivityFoward()
        # from WeiDian.service.SProduct import SProduct
        # self.sproduct = SProduct()
        self.session = Session()

    def get_all(self):
        """获取条件下的所有活动
        http://127.0.0.1:5000/activity/get_all?navid=q&lasting=true
        """
        args = request.args.to_dict()
        navid = args.get('navid')  # 导航id
        usid = args.get('usid')  # 用户id
        lasting = args.get('lasting', 'true')  # 是否正在进行的活动
        start = args.get('start', 0)  # 起始位置
        count = args.get('count', 15)  # 取出活动条数
        if not (navid or usid):
            return PARAMS_MISS
        if navid:
            activity_list = self.sactivity.get_activity_by_topnavid(navid)
        if usid:
            activity_list = self.sactivity.get_activity_by_usid(usid)
        if lasting == 'true':
            now_time = datetime.strftime(datetime.now(), format_for_db)
            activity_list = filter(lambda act: act.ACstarttime < now_time < act.ACendtime and not act.ACisended, activity_list)
        len_aclist = len(activity_list)
        if count > 30:
            count = 30
        end = start + count
        if end > len_aclist:
            end = len_aclist
        activity_list = map(self.fill_detail, activity_list)
        activity_list = activity_list[start:end]
        data = import_status("get_activity_list_success", "OK")
        data["data"] = activity_list
        return data

    def get_one(self):
        """通过acid获取活动及活动下的评论
        http://127.0.0.1:5000/activity/get_one?acid=2
        """
        args = request.args.to_dict()
        acid = args.get('acid')  # 活动id
        if not acid:
            return PARAMS_MISS
        activity = self.sactivity.get_activity_by_acid(acid)
        activity = self.fill_detail(activity)
        activity = self.fill_comment(activity)
        data = import_status("get_activity_info_success", "OK")
        data["data"] = activity
        return data

    def delete_one(self):
        """删除一个活动, 需要用户模块"""
        data = request.json
        acid = data.get('acid')
        if not acid:
            return PARAMS_MISS
        try:
            self.sactivity.delete_activity(acid)
        except Exception, e:
            pass
        return

    def end_one(self):
        """手动截止活动"""
        pass

    def add_one(self):
        data = request.json
        pass


