# -*- coding:utf8 -*-
import sys
import os
import uuid
from datetime import datetime, timedelta

from WeiDian import logger
from WeiDian.common.params_require import parameter_required
from flask import request
from WeiDian.common.import_status import import_status
from WeiDian.common.timeformat import format_for_db, get_db_time_str, get_web_time_str
from WeiDian.common.token_required import verify_token_decorator, is_admin, is_tourist, is_partner
from WeiDian.config.response import PARAMS_MISS, TOKEN_ERROR, AUTHORITY_ERROR, SYSTEM_ERROR
from WeiDian.common.TransformToList import add_model
import json

sys.path.append(os.path.dirname(os.getcwd()))


class CHotMessage():
    def __init__(self):
        from WeiDian.service.SHotMessage import SHotMessage
        self.s_hotmessage = SHotMessage()
        from WeiDian.service.SProduct import SProduct
        self.sproduct = SProduct()
        self.hotmessage_type = ['0', '1', '2', '3', '4']
        self.hotmessage_display_type = ['0', '1']
        self.empty = ['', None, [], {}]
        # self.hostmessage_update_key = ['HMtext', "HMcontent", "HMstarttime", 'HMendtime', "HMsort"]

    @verify_token_decorator
    def get_all(self):
        """活动所有热文"""
        if is_tourist():
            raise TOKEN_ERROR(u'未登录')
        args = request.args.to_dict()
        logger.debug("get hotmessage args is %s", args)
        lasting = args.get('lasting', 'true')
        htfilter = 1 if is_partner() else 0
        if is_admin():
            htfilter = [0, 1]
        try:
            hot_list = self.s_hotmessage.get_hotmsg_list_by_filter(htfilter)
            if str(lasting) == 'true':
                hot_list = filter(lambda hot: hot.HMstarttime < get_db_time_str() < hot.HMendtime, hot_list)
            for hotmsg in hot_list:
                hotmsg.HMstarttime = get_web_time_str(hotmsg.HMstarttime)
                hotmsg.HMendtime = get_web_time_str(hotmsg.HMendtime)

            data = import_status("get_hotmessage_list_success", "OK")
            data['data'] = hot_list
            return data
        except:
            logger.exception("get hotmessage error")
            raise SYSTEM_ERROR(u'服务器繁忙')
    
    @verify_token_decorator
    def add_one(self):
        """添加活动热文, 需要管理员登录"""
        if not is_admin():
            return AUTHORITY_ERROR  # 权限不足
        data = request.json
        logger.debug("add hotmessage data is ", data)
        parameter_required('HMtext', 'HMsort', 'HMSkipType')
        now_time = datetime.strftime(datetime.now(), format_for_db)
        HMstarttime = get_db_time_str(data.get('HMstarttime', now_time))  # 热文开始时间
        hmstarttime_str_to_time = datetime.strptime(HMstarttime, format_for_db)
        # 7天以后
        seven_days_later = datetime.strftime(hmstarttime_str_to_time + timedelta(days=7), format_for_db)
        HMendtime = get_db_time_str(data.get('HMendtime', seven_days_later))  # 热文结束时间, 默认7天以后
        # if not self.sproduct.get_product_by_prid(prid):
        #     return SYSTEM_ERROR
        HMSkipType = data.get('HMSkipType')
        if str(HMSkipType) not in self.hotmessage_type:
            raise SYSTEM_ERROR(u'HMSkipType参数错误')
        HMdisplaytype = data.get("HMdisplaytype")
        if str(HMdisplaytype) not in self.hotmessage_display_type:
            raise SYSTEM_ERROR(u'HMdisplaytype参数错误')
        try:
            HMid = str(uuid.uuid1())
            self.s_hotmessage.add_model('HotMessage', **{
                'HMid': HMid,
                'HMtext': data.get('HMtext'),
                'HMstarttime': HMstarttime,
                'HMendtime': HMendtime,
                'HMsort': data.get('HMsort'),
                'HMSkipType': HMSkipType,
                "HMcontent": data.get("HMcontent"),
                "HMdisplaytype": HMdisplaytype

            })
            response_make_hotmesasge = import_status('add_hotmessage_success', 'OK')
            response_make_hotmesasge['data'] = {'HMid': HMid}
            return response_make_hotmesasge
        except:
            logger.exception("create hotmessage error")
            return SYSTEM_ERROR(u'服务器繁忙')

    @verify_token_decorator
    def update_hot(self):
        """修改热文"""
        if not is_admin():
            return AUTHORITY_ERROR  # 权限不足
        data = request.json
        if 'hmid'not in data.keys():
            return PARAMS_MISS
        logger.debug("update hotmessage data is %s", data)
        hmid = data.get('hmid')
        # HMSkipType = data.get('hmskiptype')
        # HMdisplaytype = data.get("hmdisplaytype")
        # if str(HMdisplaytype) not in self.hotmessage_display_type:
        #     raise SYSTEM_ERROR(u'HMdisplaytype参数错误')
        hot = {
            "HMid": data.get("hmid"),
            "HMtext": data.get("hmtext"),
            # "HMcontent": data.get("hmcontent"),
            "HMstarttime": get_db_time_str(data.get("hmstarttime")),
            "HMsort": data.get("hmsort"),
            # "HMSkipType": HMSkipType
            # "HMdisplaytype": HMdisplaytype
        }
        hot = {k: v for k, v in hot.items() if v not in self.empty}
        if data.get("hmendtime"):
            hot["HMendtime"] = get_db_time_str(data.get("hmendtime"))
        if data.get('HMisdelete'):
            hot['HMisdelete'] = True

        from WeiDian.models.model import HotMessage
        filter_change = {HotMessage.HMid == hmid}
        hostmessage_change = self.s_hotmessage.get_hotmessage_by_filter(filter_change)
        if not hostmessage_change:
            raise SYSTEM_ERROR(u'热文不存在')

        # for key in self.hostmessage_update_key:
        #     if data.get(str(key).lower()):
        #         hot[key] = data.get(str(key))

        if data.get("hmsort"):
            filter_changed = {HotMessage.HMsort == data.get("hmsort")}
            hostmessage_changeed = self.s_hotmessage.get_hotmessage_by_filter(filter_changed)
            if hostmessage_changeed:
                self.s_hotmessage.update_hot_by_hmid(hostmessage_changeed.HMid, {"HMsort": hostmessage_change.HMsort})

        update_info = self.s_hotmessage.update_hot_by_hmid(hmid, hot)
        if not update_info:
            return SYSTEM_ERROR(u'热文不存在')
        response_update_hotmessage = import_status('update_hotmessage_success', 'OK')
        response_update_hotmessage['data'] = {'hmid': hmid}
        return response_update_hotmessage

    @verify_token_decorator
    def del_one(self):
        """删除一条热文, 需要管理员的登录状态"""
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if not is_admin():
            return AUTHORITY_ERROR  # 权限不足
        data = request.json
        hmid = data.get('hmid')
        if not hmid:
            return PARAMS_MISS
        res = self.s_hotmessage.del_one_hot(hmid)
        if not res:
            return SYSTEM_ERROR
        response_update_hotmessage = import_status('delete_hotmessage_success', 'OK')
        response_update_hotmessage['data'] = {'hmid': hmid}
        return response_update_hotmessage






