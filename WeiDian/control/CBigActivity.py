# -*- coding:utf8 -*-
import sys
import os
import uuid
from datetime import datetime, timedelta

from WeiDian import logger
from WeiDian.common.get_model_return_list import get_model_return_dict
from WeiDian.common.import_status import import_status
from WeiDian.common.params_require import parameter_required
from WeiDian.common.timeformat import get_db_time_str, format_for_db
from WeiDian.common.token_required import verify_token_decorator, is_admin
from WeiDian.config.response import TOKEN_ERROR, SYSTEM_ERROR, AUTHORITY_ERROR
from flask import request
sys.path.append(os.path.dirname(os.getcwd()))


class CBigActivity():
    def __init__(self):
        from WeiDian.service.SActivity import SActivity
        self.sactivity = SActivity()
        # from WeiDian.service.SBanner import SBnner
        # self.sbanner = SBnner()
        from WeiDian.service.SBigActivity import SBigActivity
        self.sbigactivity = SBigActivity()

    @verify_token_decorator
    def get_bigactivity(self):
        """获取专题内容"""
        if not hasattr(request, 'user'):
            raise TOKEN_ERROR(u"未登录/token错误")
        args = request.args.to_dict()
        logger.info("get sac args is %s", args)
        parameter_required('baid', 'page_num', 'page_size')
        baid = args.get('baid')
        page_num = args.get('page_num')
        page_size = args.get('page_size')
        try:
            activity_list = self.sactivity.get_bigactivity_by_baid(baid, page_num, page_size)
            banner = get_model_return_dict(self.sbigactivity.get_bigactivity_banner_by_baid(baid))['BAimage']
            response = import_status("get_bigactivity_success", "OK")
            response['data'] = {
                'activity': activity_list,
                'banner': banner
            }
            return response
        except:
            logger.debug("get bigactivity error")
            raise SYSTEM_ERROR()

    # @verify_token_decorator
    def get_home_banner(self):
        """获取首页轮播图"""
        args = request.args.to_dict()
        lasting = args.get('lasting', 'true')
        logger.info("get home banner args is %s", args)
        try:
            baimages = self.sbigactivity.get_home_banner_by_said()
            logger.info("get baimages is %s", baimages)
            if not baimages:
                raise SYSTEM_ERROR(u"系统繁忙")
            if lasting == 'true':
                baimages = filter(lambda img: img.BAstarttime < get_db_time_str() < img.BAendtime, baimages)
            data = import_status("get_banner_success", "OK")
            data["data"] = baimages
            return data
        except:
            logger.exception("get home banner error")
            return SYSTEM_ERROR

    @verify_token_decorator
    def get_discover_banner(self):
        """获取发现页轮播图"""
        if not hasattr(request, 'user'):
            raise TOKEN_ERROR(u"未登录, 或token错误")
        args = request.args.to_dict()
        lasting = args.get('lasting', 'true')
        logger.info("get discover banner args is %s", args)
        try:
            baimages = self.sbigactivity.get_discover_banner_by_said()
            logger.info("get baimages is %s", baimages)
            if not baimages:
                raise SYSTEM_ERROR(u"系统繁忙")
            if lasting == 'true':
                baimages = filter(lambda img: img.BAstarttime < get_db_time_str() < img.BAendtime, baimages)
            data = import_status("get_banner_success", "OK")
            data["data"] = baimages
            return data
        except:
            logger.exception("get home banner error")
            return SYSTEM_ERROR

    @verify_token_decorator
    def create_home_bigactivity(self):
        """添加首页专题"""
        if not is_admin():
            raise AUTHORITY_ERROR(u'非管理员权限')
        data = request.json
        logger.info("create home bigactivity data is %s", data)
        parameter_required('BAimage', 'BAsort', 'BAtext')
        BAid = str(uuid.uuid1())
        BAimage = data.get('BAimage')
        now_time = datetime.strftime(datetime.now(), format_for_db)
        BAstarttime = data.get('BAstarttime', now_time)
        BAstarttime_str_to_time = datetime.strptime(BAstarttime, format_for_db)
        seven_days_later = datetime.strftime(BAstarttime_str_to_time + timedelta(days=365), format_for_db)  # 七天以后
        BAendtime = data.get('BAendtime', seven_days_later)
        try:
            self.sbigactivity.add_model("BigActivity", **{
                "BAid": BAid,
                "BAtext": data.get('BAtext'),
                "BAimage": BAimage,
                "BAstarttime": BAstarttime,
                "BAendtime": BAendtime,
                "BAsort": data.get('BAsort', 0),
                "BAposition": 0,
            })
            response = import_status("create_home_bigactivity", "OK")
            response["data"] = {
                "BAid": BAid
            }
            return response
        except:
            logger.exception("create bigactivity error")
            return SYSTEM_ERROR(u'数据错误')

    @verify_token_decorator
    def create_discover_bigactivity(self):
        """添加发现页专题"""
        if not is_admin():
            raise AUTHORITY_ERROR(u'非管理员权限')
        data = request.json
        logger.info("create discover bigactivity data is %s", data)
        parameter_required('BAimage', 'BAsort', 'BAtext')
        BAid = str(uuid.uuid1())
        BAimage = data.get('BAimage')
        now_time = datetime.strftime(datetime.now(), format_for_db)
        BAstarttime = data.get('BAstarttime', now_time)
        BAstarttime_str_to_time = datetime.strptime(BAstarttime, format_for_db)
        seven_days_later = datetime.strftime(BAstarttime_str_to_time + timedelta(days=365), format_for_db)  # 七天以后
        BAendtime = data.get('BAendtime', seven_days_later)
        try:
            self.sbigactivity.add_model("BigActivity", **{
                "BAid": BAid,
                "BAtext": data.get('BAtext'),
                "BAimage": BAimage,
                "BAstarttime": BAstarttime,
                "BAendtime": BAendtime,
                "BAsort": data.get('BAsort', 0),
                "BAposition": 1,
            })

            response = import_status("create_discover_bigactivity", "OK")
            response["data"] = {
                "BAid": BAid
            }
            return response
        except:
            logger.exception("create bigactivity error")
            return SYSTEM_ERROR(u'数据错误')





