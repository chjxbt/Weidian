# -*- coding:utf8 -*-
import sys
import os
from WeiDian import logger
from WeiDian.common.get_model_return_list import get_model_return_dict
from WeiDian.common.import_status import import_status
from WeiDian.common.params_require import parameter_required
from WeiDian.common.timeformat import get_db_time_str
from WeiDian.common.token_required import verify_token_decorator
from WeiDian.config.response import TOKEN_ERROR, SYSTEM_ERROR
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
        lasting = args.get('lasting', True)
        logger.info("get home banner args is %s", args)
        try:
            baimages = self.sbigactivity.get_home_banner_by_said()
            logger.info("get baimages is %s", baimages)
            if not baimages:
                raise SYSTEM_ERROR(u"系统繁忙")
            if lasting is True:
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
        lasting = args.get('lasting', True)
        logger.info("get discover banner args is %s", args)
        try:
            baimages = self.sbigactivity.get_discover_banner_by_said()
            logger.info("get baimages is %s", baimages)
            if not baimages:
                raise SYSTEM_ERROR(u"系统繁忙")
            if lasting is True:
                # now_time = datetime.strftime(datetime.now(), format_for_db)
                baimages = filter(lambda img: img.BAstarttime < get_db_time_str() < img.BAendtime, baimages)
            data = import_status("get_banner_success", "OK")
            data["data"] = baimages
            return data
        except:
            logger.exception("get home banner error")
            return SYSTEM_ERROR



