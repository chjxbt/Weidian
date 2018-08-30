# *- coding:utf8 *-
import sys
import os
import uuid
from flask import request
from datetime import datetime, timedelta
from WeiDian.common.TransformToList import add_model
from WeiDian.common.import_status import import_status
from WeiDian.common.timeformat import format_for_db
from WeiDian.common.token_required import verify_token_decorator, is_partner, is_admin
from WeiDian.config.response import AUTHORITY_ERROR, TOKEN_ERROR, PARAMS_MISS, SYSTEM_ERROR
from WeiDian.control.BaseControl import BaseProductControl
from WeiDian.service.SProduct import SProduct
from WeiDian.service.SSuperUser import SSuperUser
from WeiDian.service.SRecommend import SRecommend
sys.path.append(os.path.dirname(os.getcwd()))


class CRecommend(BaseProductControl):

    def __init__(self):
        self.srecommend = SRecommend()
        self.sproduct = SProduct()
        self.ssuperuser = SSuperUser()

    @verify_token_decorator
    def get_list(self):
        args = request.args.to_dict()
        if not is_partner():
            return AUTHORITY_ERROR
        print '是合伙人'
        recommend = self.srecommend.get_recommend_list()
        lasting = args.get('lasting', 'true')  # 是否正在展示
        if lasting == 'true':
            now_time = datetime.strftime(datetime.now(), format_for_db)
            recommend = filter(lambda re: re.REstarttime <
                               now_time < re.REendtime, recommend)
        map(self.fill_recommend_product, recommend)
        map(self.fill_recommend_nums, recommend)
        map(self.fill_super, recommend)
        data = import_status('get_recommend_success', 'OK')
        data['data'] = recommend
        return data

    @verify_token_decorator
    def add_one(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if not is_admin():
            return AUTHORITY_ERROR  # 权限不足
        data = request.json
        now_time = datetime.strftime(datetime.now(), format_for_db)
        restarttime = data.get('restarttime', now_time)  # 上线时间, 默认当前时间
        restarttime_str_to_time = datetime.strptime(restarttime, format_for_db)
        # 1天以后
        one_days_later = datetime.strftime(
            restarttime_str_to_time +
            timedelta(
                days=7),
            format_for_db)
        reendtime = data.get('reendtime', one_days_later)  # 推荐下线时间, 默认1天以后
        relikefakenum = data.get('relikenum', 0)  # 喜欢数
        refakeviewnum = data.get('reviewnum', 0)  # 浏览数
        prid_list = data.get('prid_list')
        reid = str(uuid.uuid4())
        add_model('Recommend', **{
            'REid': reid,
            'SUid': request.user.id,
            'RElikefakenum': relikefakenum,
            'REfakeviewnum': refakeviewnum,
            'REstarttime': restarttime,
            'REendtime': reendtime,
        })
        for item in prid_list:
            add_model('RecommendProduct', **{
                'REid': reid,
                'PRid': item.get('prid'),
                'RPid': str(uuid.uuid4()),
                'RPsort': item.get('rpsort')
            })
        response_make_recommend = import_status('add_recommend_success', 'OK')
        response_make_recommend['data'] = {}
        response_make_recommend['data']['reid'] = reid
        return response_make_recommend

    @verify_token_decorator
    def update_recommend(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if not is_admin():
            return AUTHORITY_ERROR  # 权限不足
        data = request.json
        if 'reid' not in data.keys():
            return PARAMS_MISS
        reid = data.pop('reid')
        res = self.srecommend.update_recommend(reid, **data)
        if not res:
            return SYSTEM_ERROR("reid错误，要修改的内容不存在")
        prid_list = data.get('prid_list')
        for item in prid_list:
            add_model('RecommendProduct', **{
                'REid': reid,
                'PRid': item.get('prid'),
                'RPid': str(uuid.uuid4()),
                'RPsort': item.get('rpsort')
            })
        response_update_recommend = import_status(
            'update_recommend_success', 'OK')
        response_update_recommend['data'] = {'reid': reid}
        return response_update_recommend

    @verify_token_decorator
    def del_one(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if not is_admin():
            return AUTHORITY_ERROR  # 权限不足
        data = request.json
        reid = data.get('reid')
        if not reid:
            return PARAMS_MISS
        self.srecommend.del_recommend(reid)
        response_del_recommend = import_status('del_recommend_success', 'OK')
        response_del_recommend['data'] = {}
        response_del_recommend['data']['reid'] = reid
        return response_del_recommend
