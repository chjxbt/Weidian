# -*- coding:utf8 -*-
import sys
import os
import uuid
from flask import request
from datetime import datetime, timedelta

from WeiDian import logger
from WeiDian.common.TransformToList import add_model
from WeiDian.common.import_status import import_status
from WeiDian.common.params_require import parameter_required
from WeiDian.common.timeformat import format_for_db
from WeiDian.common.token_required import verify_token_decorator, is_partner, is_admin
from WeiDian.config.response import AUTHORITY_ERROR, TOKEN_ERROR, PARAMS_MISS, SYSTEM_ERROR
from WeiDian.control.BaseControl import BaseProductControl
from WeiDian.service.SProduct import SProduct
from WeiDian.service.SSuperUser import SSuperUser
from WeiDian.service.SRecommend import SRecommend
from WeiDian.service.SRecommendLike import SRecommendLike
sys.path.append(os.path.dirname(os.getcwd()))


class CRecommend(BaseProductControl):

    def __init__(self):
        self.srecommend = SRecommend()
        self.sproduct = SProduct()
        self.ssuperuser = SSuperUser()
        self.srecommendlike = SRecommendLike()

    @verify_token_decorator
    def get_one(self):
        # args = request.args.to_dict()
        if not is_partner():
            return AUTHORITY_ERROR
        print '是合伙人'
        recommend = self.srecommend.get_one_recommend()
        self.srecommend.update_view_num(recommend.REid)
        recommend_list = [recommend]
        map(self.fill_recommend_product, recommend_list)
        map(self.fill_recommend_nums, recommend_list)
        map(self.fill_super, recommend_list)
        data = import_status('get_recommend_success', 'OK')
        data['data'] = recommend_list
        return data

    @verify_token_decorator
    def add_one(self):
        """添加推荐"""
        # todo 此处无需添加图片, 关联商品id即可
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if not is_admin():
            return AUTHORITY_ERROR  # 权限不足
        data = parameter_required('REstarttime', 'REendtime', 'RElikenum', 'REviewnum', 'PRid_list')
        # data = request.json
        now_time = datetime.strftime(datetime.now(), format_for_db)
        restarttime = data.get('REstarttime', now_time)  # 上线时间, 默认当前时间
        restarttime_str_to_time = datetime.strptime(restarttime, format_for_db)
        # 7天以后
        one_days_later = datetime.strftime(
            restarttime_str_to_time +
            timedelta(
                days=7),
            format_for_db)
        reendtime = data.get('REendtime', one_days_later)  # 推荐下线时间, 默认1天以后
        relikefakenum = data.get('RElikenum', 0)  # 喜欢数
        refakeviewnum = data.get('REviewnum', 0)  # 浏览数
        prid_list = data.get('PRid_list')
        if not prid_list:
            raise PARAMS_MISS('缺失PRid_list')
        reid = str(uuid.uuid4())
        try:
            add_model('Recommend', **{
                'REid': reid,
                'SUid': request.user.id,
                'RElikefakenum': relikefakenum,
                'REfakeviewnum': refakeviewnum,
                'REstarttime': restarttime,
                'REendtime': reendtime,
            })
        except Exception as e:
            logger.debug("add Recommend error")
            raise SYSTEM_ERROR(u'添加Recommend错误')
        try:
            for item in prid_list:
                add_model('RecommendProduct', **{
                    'REid': reid,
                    'PRid': item.get('PRid'),
                    'RPid': str(uuid.uuid4()),
                    'RPsort': item.get('RPsort')
                })
        except Exception as e:
            logger.debug("add recommondproduct list error")
            raise SYSTEM_ERROR(u'添加每日推荐商品RecommendProduct内容出错')
        response_make_recommend = import_status('add_recommend_success', 'OK')
        response_make_recommend['data'] = {}
        response_make_recommend['data']['reid'] = reid
        return response_make_recommend

    # @verify_token_decorator
    # def update_recommend(self):
    #     if not hasattr(request, 'user'):
    #         return TOKEN_ERROR  # 未登录, 或token错误
    #     if not is_admin():
    #         return AUTHORITY_ERROR  # 权限不足
    #     data = request.json
    #     if 'reid' not in data.keys():
    #         return PARAMS_MISS
    #     reid = data.pop('reid')
    #     res = self.srecommend.update_recommend(reid, **data)
    #     if not res:
    #         return SYSTEM_ERROR("reid错误，要修改的内容不存在")
    #     prid_list = data.get('prid_list')
    #     for item in prid_list:
    #         add_model('RecommendProduct', **{
    #             'REid': reid,
    #             'PRid': item.get('prid'),
    #             'RPid': str(uuid.uuid4()),
    #             'RPsort': item.get('rpsort')
    #         })
    #     response_update_recommend = import_status(
    #         'update_recommend_success', 'OK')
    #     response_update_recommend['data'] = {'reid': reid}
    #     return response_update_recommend

    @verify_token_decorator
    def update_recommend_by_reid(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if not is_admin():
            return AUTHORITY_ERROR  # 权限不足
        data = parameter_required(u'REid')
        reid = data.get('REid')
        recommend = {
            'REstarttime': data.get('REstarttime'),
            'REendtime': data.get('REendtime'),
            'REfakeviewnum': data.get('REfakeviewnum'),
            'RElikefakenum': data.get('RElikefakenum')
        }
        recommend = {k: v for k, v in recommend.items() if v is not None}
        res = self.srecommend.update_recommend_by_reid(reid, recommend)
        if not res:
            return SYSTEM_ERROR(u"REid错误，要修改的内容不存在")
        prid_list = data.get('PRid_list')
        for item in prid_list:
            add_model('RecommendProduct', **{
                'REid': reid,
                'PRid': item.get('PRid'),
                'RPid': str(uuid.uuid4()),
                'RPsort': item.get('RPsort')
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
        reid = data.get('REid')
        if not reid:
            return PARAMS_MISS
        self.srecommend.del_recommend(reid)
        response_del_recommend = import_status('del_recommend_success', 'OK')
        response_del_recommend['data'] = {}
        response_del_recommend['data']['reid'] = reid
        return response_del_recommend
