# *- coding:utf8 *-
import sys
import os
import uuid
from flask import request
from datetime import datetime
from WeiDian.common.TransformToList import add_model
from WeiDian.common.timeformat import format_for_db
from WeiDian.common.token_required import is_admin, verify_token_decorator
from WeiDian.config.response import TOKEN_ERROR, AUTHORITY_ERROR, PARAMS_MISS, SYSTEM_ERROR
from WeiDian.common.import_status import import_status
sys.path.append(os.path.dirname(os.getcwd()))


class CSearchField():
    def __init__(self):
        from WeiDian.service.SSearchField import SSearchField
        self.s_searchfield = SSearchField()

    def get_all(self):
        """首页搜索框商品字段"""
        args = request.args.to_dict()
        lasting = args.get('lasting', 'true')
        sf_list = self.s_searchfield.get_all_searchfield()
        if lasting == 'true':
            sf_list = self.s_searchfield.get_lasting_searchfield()
        data = import_status("get_serachfield_success", "OK")
        data['data'] = sf_list
        return data

    @verify_token_decorator
    def add_one(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if not is_admin():
            return AUTHORITY_ERROR  # 权限不足
        data = request.json
        now_time = datetime.strftime(datetime.now(), format_for_db)
        sfid = str(uuid.uuid1())
        sfstarttime = data.get('sfstarttime', now_time)  # 上线时间默认当前时间
        sfendtime = data.get('sfendtime')
        sftext = data.get('sftext')
        sfsort = data.get('sfsort')
        if not sftext:
            return PARAMS_MISS
        add_model('SearchField', **{
            'SFid': sfid,
            'SFtext': sftext,
            'SFstarttime': sfstarttime,
            'SFendtime': sfendtime,
            'SFsort': sfsort
        })
        response_make_searchfield = import_status('add_searchfield_success', 'OK')
        response_make_searchfield['data'] = {'sfid': sfid}
        return response_make_searchfield

    @verify_token_decorator
    def update_searchfield(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if not is_admin():
            return AUTHORITY_ERROR  # 权限不足
        data = request.json
        if not 'sfid' in data.keys():
            return PARAMS_MISS
        sfid = data.pop('sfid')
        res = self.s_searchfield.update_searchfield(sfid, **data)
        if not res:
            return SYSTEM_ERROR('字段不存在')
        response_update_searchfield = import_status('update_searchfield_success', 'OK')
        response_update_searchfield['data'] = {'sfid': sfid}
        return response_update_searchfield

    @verify_token_decorator
    def del_one(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if not is_admin():
            return AUTHORITY_ERROR  # 权限不足
        data = request.json
        sfid = data.get('sfid')
        if not sfid:
            return PARAMS_MISS
        res = self.s_searchfield.del_searchfield(sfid)
        if not res:
            return SYSTEM_ERROR
        response_del_searchfield = import_status('delete_searchfield_success', 'OK')
        response_del_searchfield['data'] = {'sfid': sfid}
        return response_del_searchfield


    @verify_token_decorator
    def get_content_by_seach(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        
        args = request.args.to_dict()
        # lasting = args.get('lasting', 'true')  # 是否正在进行的活动
        page = int(args.get('page', 1))  # 页码
        start = int(args.get('start', 0))  # 起始位置
        count = int(args.get('count', 15))  # 取出条数
        if not start:
            start = (page -1) * count
        from WeiDian.service.SProduct import SProduct
        from WeiDian.service.SActivity import SActivity
        from WeiDian.control.CActivity import CActivity

        prid_list = SProduct().get_products_by_prname(args.get("PRname"))
        sactivity = SActivity()
        activity_list = [sactivity.get_activity_by_prid(prid) for prid in prid_list]
        if count > 30:
            count = 30
        end = start + count
        len_aclist = len(activity_list)
        if end > len_aclist:
            end = len_aclist
        activity_list = map(CActivity.fill_detail, activity_list)
        for activity in activity_list:
            sactivity.update_view_num(activity.ACid)
        cactivity = CActivity()
        activity_list = activity_list[start:end]
        map(cactivity.fill_comment_two, activity_list)
        map(cactivity.fill_like_num, activity_list)

        map(cactivity.fill_type, activity_list)
        map(cactivity.fill_product, activity_list)
        data = import_status("get_activity_list_success", "OK")
        data["data"] = activity_list
        return data
