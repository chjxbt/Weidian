# *- coding:utf8 *-
import sys
import os
import uuid
from datetime import datetime, timedelta

from WeiDian.config.response import TOKEN_ERROR, PARAMS_MISS, AUTHORITY_ERROR, SYSTEM_ERROR
from WeiDian.common.import_status import import_status
from WeiDian.config.messages import delete_banner_success
from WeiDian.common.MakeToken import verify_token_decorator
from WeiDian.common.TransformToList import add_model

from sqlalchemy.orm import Session

from WeiDian.common.timeformat import format_for_db
from test.errors import ApiException

sys.path.append(os.path.dirname(os.getcwd()))
from flask import request


class CBanner():
    def __init__(self):
        from WeiDian.service.SBanner import SBnner
        self.sbanner = SBnner()
        from WeiDian.service.SActivity import SActivity
        self.sactivity = SActivity()

    def get_all(self):
        args = request.args.to_dict()
        lasting = args.get('lasting', 'true')  # 有效时间内的轮播
        if lasting == 'true':
            banner_list = self.sbanner.get_all_lasting_banner()
        else:
            banner_list = self.sbanner.get_all_banner()
        data = import_status("get_banner_success", "OK")
        data['data'] = banner_list
        return data

    def get_one(self):
        args = request.args.to_dict()
        baid = args.get('baid')
        if baid:
            banner = self.sbanner.get_one_by_baid(baid)
            if banner:
                banner = self.fill_activity(banner)
                data = import_status("get_banner_success", "OK")
                data['data'] = banner
                return data
            else:
                pass

    @verify_token_decorator
    def add_one(self):
        """添加一个轮播图, 需要管理员的登录状态"""
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if request.user.scope != 'SuperUser':
            return AUTHORITY_ERROR  # 权限不足
        data = request.json
        now_time = datetime.strftime(datetime.now(), format_for_db)
        bastarttime = data.get('bastarttime', now_time)  # 轮播 开始时间
        bastarttime_str_to_time = datetime.strptime(bastarttime, format_for_db)
        # 7天以后
        seven_days_later = datetime.strftime(bastarttime_str_to_time + timedelta(days=7), format_for_db)
        baentime = data.get('baendtime', seven_days_later)  # 轮播结束时间, 默认7天以后
        baid = str(uuid.uuid1())
        baimage = data.get('baimage')
        basort = data.get('basort')
        acid = data.get('acid')
        if not baimage or not acid:
            return PARAMS_MISS
        if not self.sactivity.get_activity_by_acid(acid):
            return SYSTEM_ERROR
        add_model('Banner', **{
            'BAid': baid,
            'BAimage': baimage,
            'ACid': acid,
            'BAstarttime': bastarttime,
            'BAendtime': baentime,
            'BAsort': basort
        })
        response_make_banner = import_status('add_banner_success', 'OK')
        response_make_banner['data'] = {'baid': baid}
        return response_make_banner

    @verify_token_decorator
    def del_one(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if request.user.scope != 'SuperUser':
            return AUTHORITY_ERROR  # 权限不足
        data = request.json
        baid = data.get('baid')
        if not baid:
            return PARAMS_MISS
        res = self.sbanner.del_banner(baid)
        if not res:
            return SYSTEM_ERROR
        response_make_banner = import_status('delete_banner_success', 'OK')
        response_make_banner['data'] = {'baid': baid}
        return response_make_banner


    def fill_activity(self, banner):
        acid = banner.ACid
        activity = self.sactivity.get_activity_by_acid(acid)
        banner.activity = activity
        banner.add('activity')
        return banner




