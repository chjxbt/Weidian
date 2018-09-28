# -*- coding:utf8 -*-
import sys
import os
import uuid
from datetime import datetime, timedelta

from WeiDian import logger
from WeiDian.common.params_require import parameter_required
from flask import request
from WeiDian.common.import_status import import_status
from WeiDian.common.timeformat import format_for_db, get_db_time_str
from WeiDian.common.token_required import verify_token_decorator, is_admin
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
        self.hotmessage_type = ['0', '1', '2', '3']
        # self.hostmessage_update_key = ['HMtext', "HMcontent", "HMstarttime", 'HMendtime', "HMsort"]

    def get_all(self):
        """活动所有热文"""
        args = request.args.to_dict()
        logger.info("get hotmessage args is %s", args)
        lasting = args.get('lasting', 'true')
        # hot_list = self.s_hotmessage.get_all_hot()
        try:
            hot_list = self.s_hotmessage.get_hotmessage()
            if lasting == 'true':
                hot_list = filter(lambda hot: hot.HMstarttime < get_db_time_str() < hot.HMendtime, hot_list)
            data = import_status("get_hotmessage_list_success", "OK")
            data['data'] = hot_list
            return data
        except:
            logger.exception("get hotmessage error")
            return SYSTEM_ERROR(u'服务器繁忙')
    
    @verify_token_decorator
    def add_one(self):
        """添加活动热文, 需要管理员登录"""
        if not is_admin():
            return AUTHORITY_ERROR  # 权限不足
        data = request.json
        logger.info("add hotmessage data is ", data)
        parameter_required('HMtext', 'HMsort', 'HMSkipType')
        now_time = datetime.strftime(datetime.now(), format_for_db)
        HMstarttime = data.get('HMstarttime', now_time)  # 热文开始时间
        hmstarttime_str_to_time = datetime.strptime(HMstarttime, format_for_db)
        # 7天以后
        seven_days_later = datetime.strftime(hmstarttime_str_to_time + timedelta(days=7), format_for_db)
        HMendtime = data.get('HMendtime', seven_days_later)  # 热文结束时间, 默认7天以后
        # if not self.sproduct.get_product_by_prid(prid):
        #     return SYSTEM_ERROR
        HMSkipType = data.get('HMSkipType')
        if str(HMSkipType) not in self.hotmessage_type:
            raise SYSTEM_ERROR(u'参数错误')
        # elif str(HMSkipType) == '1':
        #     PRid = data.get('PRid')
        #     BAid = ''
        # else:
        #     PRid = ''
        #     BAid = data.get('BAid')
        try:
            HMid = str(uuid.uuid1())
            self.s_hotmessage.add_model('HotMessage', **{
                'HMid': HMid,
                'HMtext': data.get('HMtext'),
                'HMstarttime': HMstarttime,
                'HMendtime': HMendtime,
                'HMsort': data.get('HMsort'),
                'HMSkipType': HMSkipType,
                # 'PRid': data.get('PRid', '0'),
                # 'BAid': data.get('BAid', '0')
                "HMcontent": data.get("HMcontent")
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
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if not is_admin():
            return AUTHORITY_ERROR  # 权限不足
        data = request.json
        if 'hmid'not in data.keys():
            return PARAMS_MISS
        hmid = data.get('hmid')
        hot = {}
        hot['HMid'] = data['hmid']
        from WeiDian.models.model import HotMessage
        filter_change = {HotMessage.HMid == hmid}
        hostmessage_change = self.s_hotmessage.get_hotmessage_by_filter(filter_change)
        if not hostmessage_change:
            raise SYSTEM_ERROR(u'热文不存在')

        if 'hmtext' in data.keys():
            hot['HMtext'] = data['hmtext']
        if 'hmcontent' in data.keys():
            hot['HMcontent'] = data['hmcontent']
        if 'hmstarttime' in data.keys():
            hot['HMstarttime'] = get_db_time_str(data['hmstarttime'])
        if 'hmendtime' in data.keys():
            hot['HMendtime'] = get_db_time_str(data['hmendtime'])
        if 'hmsort' in data:
            hot['HMsort'] = data['hmsort']
        update_info = self.s_hotmessage.update_hot_by_hmid(hmid, hot)
        if not update_info:
            return SYSTEM_ERROR(u'热文不存在')
        filter_changed = {HotMessage.HMsort == hostmessage_change.HMsort}
        hostmessage_changeed = self.s_hotmessage.get_hotmessage_by_filter(filter_changed)
        if hostmessage_changeed:
            self.s_hotmessage.update_hot_by_hmid(hostmessage_changeed.HMid, {"HMsort": hostmessage_change.HMsort})
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






