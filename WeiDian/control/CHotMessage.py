# *- coding:utf8 *-
import uuid
from datetime import datetime, timedelta

from flask import request

from WeiDian.common.import_status import import_status
from WeiDian.common.timeformat import format_for_db
from WeiDian.common.token_required import verify_token_decorator, is_admin
from WeiDian.config.messages import update_hotmessage_success, delete_hotmessage_success
from WeiDian.config.response import PARAMS_MISS, TOKEN_ERROR, AUTHORITY_ERROR, SYSTEM_ERROR
from WeiDian.common.TransformToList import add_model


class CHotMessage():
    def __init__(self):
        from WeiDian.service.SHotMessage import SHotMessage
        self.s_hotmessage = SHotMessage()
        from WeiDian.service.SProduct import SProduct
        self.sproduct = SProduct()

    def get_all(self):
        """活动所有热文"""
        args = request.args.to_dict()
        lasting = args.get('lasting', 'true')
        hot_list = self.s_hotmessage.get_all_hot()
        if lasting == 'true':
            hot_list = self.s_hotmessage.get_lasting_hot()
        data = import_status("get_hotmessage_list_success", "OK")
        data['data'] = hot_list
        return data
    
    @verify_token_decorator
    def add_one(self):
        """添加活动热文, 需要管理员登录"""
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if not is_admin():
            return AUTHORITY_ERROR  # 权限不足
        data = request.json
        now_time = datetime.strftime(datetime.now(), format_for_db)
        hmstarttime = data.get('hmstarttime', now_time)  # 热文开始时间
        hmstarttime_str_to_time = datetime.strptime(hmstarttime, format_for_db)
        # 7天以后
        seven_days_later = datetime.strftime(hmstarttime_str_to_time + timedelta(days=7), format_for_db)
        hmendtime = data.get('hmendtime', seven_days_later)  # 热文结束时间, 默认7天以后
        hmtext = data.get('hmtext') 
        prid = data.get('prid')
        hmsort = data.get('hmsort')
        if not hmtext or not prid:
            return PARAMS_MISS
        if not self.sproduct.get_product_by_prid(prid):
            return SYSTEM_ERROR
        hmid = str(uuid.uuid1())
        add_model('HotMessage', **{
            'HMid': hmid,
            'HMtext': hmtext,
            'PRid': prid,
            'HMstarttime': hmstarttime,
            'HMendtime': hmendtime,
            'HMsort': hmsort
        }) 
        response_make_hotmesasge = import_status('add_hotmessage_success', 'OK')
        response_make_hotmesasge['data'] = {'hmid': hmid}
        return response_make_hotmesasge

    @verify_token_decorator
    def update_one(self):
        """热文修改"""

        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if not is_admin():
            return AUTHORITY_ERROR  # 权限不足
        data = request.json
        if not 'hmid' in data.keys():
            return PARAMS_MISS
        hmid = data.pop('hmid')
        res = self.s_hotmessage.update_one_hot(hmid, **data)
        if not res:
            return SYSTEM_ERROR
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






