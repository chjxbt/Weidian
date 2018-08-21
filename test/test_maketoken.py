# *- coding:utf8 *-
import uuid
from datetime import datetime, timedelta

from flask import Blueprint, request, jsonify
from flask.views import MethodView

from WeiDian.common.MakeToken import verify_token_decorator
from WeiDian.common.timeformat import format_for_db
from WeiDian.common.base_error import BaseError
from WeiDian.config.response import TOKEN_ERROR, PARAMS_MISS, SYSTEM_ERROR


class TestToken(MethodView):
    def post(self):
        """generic token test"""
        usid = '6882ad09-bf5f-4607-8ad1-1cd46b6158e0'
        raise BaseError()

    @verify_token_decorator
    def get(self):
        """verfity token test"""
        from flask import request
        raise BaseError

    @verify_token_decorator
    def put(self):
        """add activity_list test"""
        from WeiDian.common.TransformToList import add_models
        if not hasattr(request, 'user'):
            print '1'
        if request.user.scope != 'SuperUser':
            pass
        data = request.json
        # datas = json_data.get('data')
        add_data_list = []
        now_time = datetime.strftime(datetime.now(), format_for_db)
        acstarttime = data.get('acstarttime', now_time)  # 活动开始时间, 默认当前时间
        asstarttime_str_to_time = datetime.strptime(acstarttime, format_for_db)
        # 7天以后
        seven_days_later = datetime.strftime(asstarttime_str_to_time + timedelta(days=7), format_for_db)
        acendtime = data.get('acendtime', seven_days_later)  # 活动结束时间, 默认7天以后
        actext = data.get('actext')  # 文字内容
        actype = data.get('actype')  # 类型
        forwardnum = data.get('fowardnum', 0)  # 转发数量
        likenum = data.get('likenum', 0)  # 喜欢数
        acbrowenum = data.get('browsenum', 0)  # 浏览数
        soldfakenum = data.get('soldnum', 0)  # 商品的销售量
        istop = data.get('acistop')
        prid = data.get('prid')  # 商品id
        media = data.get('media')  # 多媒体
        tags = data.get('tags')  # 右上角tag标签
        topnavid = data.get('topnavid')
        # if not media or not actext or not prid or not topnavid:
        #     return PARAMS_MISS
        # relation_product = self.sproduct.get_product_by_prid(prid)  # 关联的商品
        # if not relation_product:  # 如果没有该商品
        #     return SYSTEM_ERROR
        # 创建活动
        acid = str(uuid.uuid1())
        add_models('Activity', **{
        'data': [
            {
                'ACid': acid,
                'PRid': '关联商品id',
                'SUid': request.user.id,
                'ACtype': actype,
                'TopnavId': topnavid,
                'ACtext': actext,
                'AClikeFakeNum': likenum,
                'ACbrowsenum': acbrowenum,
                'ACforwardFakenum': forwardnum,
                'ACProductsSoldFakeNum': soldfakenum,
                'ACstarttime': acstarttime,
                'ACendtime': acendtime,
                'ACistop': istop,
            },
            {
                'ACid': acid+str(1),
                'PRid': '关联商品ids',
                'SUid': request.user.id,
                'ACtype': actype,
                'TopnavId': topnavid,
                'ACtext': actext,
                'AClikeFakeNum': likenum,
                'ACbrowsenum': acbrowenum,
                'ACforwardFakenum': forwardnum,
                'ACProductsSoldFakeNum': soldfakenum,
                'ACstarttime': acstarttime,
                'ACendtime': acendtime,
                'ACistop': istop,
            }
        ]
        })
        return jsonify({"data": 'success'})


def create_test_url(app):
    app.add_url_rule('/test', view_func=TestToken.as_view('test'))