# *- coding:utf8 *-
import sys
import os
from datetime import datetime, timedelta

from WeiDian.config.messages import delete_activity_success, stop_activity_success
from sqlalchemy.orm import Session

from WeiDian.common.MakeToken import verify_token_decorator
from WeiDian.common.TransformToList import add_model
from WeiDian.common.import_status import import_status
from WeiDian.common.timeformat import format_for_db
from WeiDian.config.response import PARAMS_MISS, TOKEN_ERROR, AUTHORITY_ERROR, SYSTEM_ERROR
from WeiDian.config.activitytype import activity_type
from WeiDian.control.BaseControl import BaseActivityControl

sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import uuid


class CActivity(BaseActivityControl):
    def __init__(self):
        from WeiDian.service.SActivity import SActivity
        self.sactivity = SActivity()
        from WeiDian.service.SActivityComment import SActivityComment
        self.sacomment = SActivityComment()
        from WeiDian.service.SActivityLike import SActivityLike
        self.salike = SActivityLike()
        from WeiDian.service.SSuperUser import SSuperUser
        self.ssuperuser = SSuperUser()
        from WeiDian.service.SActivityMedia import SActivityMedia
        self.smedia = SActivityMedia()
        from WeiDian.service.SActivityTag import SActivityTag
        self.stags = SActivityTag()
        from WeiDian.service.SActivityFoward import SActivityFoward
        self.foward = SActivityFoward()
        from WeiDian.service.SProduct import SProduct
        self.sproduct = SProduct()
        self.session = Session()

    def get_all(self):
        """获取条件下的所有活动
        http://127.0.0.1:5000/activity/get_all?navid=q&lasting=true
        """
        args = request.args.to_dict()
        navid = args.get('navid')  # 导航id
        suid = args.get('suid')  # 管理员id
        lasting = args.get('lasting', 'true')  # 是否正在进行的活动
        start = int(args.get('start', 0))  # 起始位置
        count = int(args.get('count', 15))  # 取出活动条数
        if not (navid or suid):
            return PARAMS_MISS
        if navid:
            activity_list = self.sactivity.get_activity_by_topnavid(navid)
        if suid:
            activity_list = self.sactivity.get_activity_by_suid(suid)
        if lasting == 'true':
            now_time = datetime.strftime(datetime.now(), format_for_db)
            activity_list = filter(
                lambda act: act.ACstarttime < now_time < act.ACendtime and not act.ACisended,
                activity_list)
        len_aclist = len(activity_list)
        if count > 30:
            count = 30
        end = start + count
        if end > len_aclist:
            end = len_aclist
        activity_list = map(self.fill_detail, activity_list)
        map(self.fill_comment, activity_list)
        activity_list = activity_list[start:end]
        data = import_status("get_activity_list_success", "OK")
        data["data"] = activity_list
        return data

    def get_one(self):
        """通过acid获取活动及活动下的评论
        http://127.0.0.1:5000/activity/get_one?acid=2
        """
        args = request.args.to_dict()
        acid = args.get('acid')  # 活动id
        if not acid:
            return PARAMS_MISS
        activity = self.sactivity.get_activity_by_acid(acid)
        if not activity:
            return SYSTEM_ERROR
        activity = self.fill_detail(activity)
        activity = self.fill_comment(activity)
        data = import_status("get_activity_info_success", "OK")
        data["data"] = activity
        return data

    @verify_token_decorator
    def delete_one(self):
        """删除一个活动, 需要管理员的登录状态"""
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if request.user.scope != 'SuperUser':
            return AUTHORITY_ERROR  # 权限不足
        data = request.json
        acid = data.get('acid')
        if not acid:
            return PARAMS_MISS
        try:
            self.sactivity.delete_activity(acid)
            return delete_activity_success
        except Exception as e:
            pass

    @verify_token_decorator
    def stop_one(self):
        """手动截止活动"""
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if request.user.scope != 'SuperUser':
            return AUTHORITY_ERROR  # 权限不足
        data = request.json
        acid = data.get('acid')
        if not acid:
            return PARAMS_MISS
        try:
            self.sactivity.stop_activity(acid)
            return stop_activity_success
        except Exception as e:
            pass

    @verify_token_decorator
    def add_one(self):
        """添加一个活动, 需要管理员的登录状态"""
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if request.user.scope != 'SuperUser':
            return AUTHORITY_ERROR  # 权限不足
        data = request.json
        now_time = datetime.strftime(datetime.now(), format_for_db)
        acstarttime = data.get('acstarttime', now_time)  # 活动开始时间, 默认当前时间
        asstarttime_str_to_time = datetime.strptime(acstarttime, format_for_db)
        # 7天以后
        seven_days_later = datetime.strftime(
            asstarttime_str_to_time +
            timedelta(
                days=7),
            format_for_db)
        acendtime = data.get('acendtime', seven_days_later)  # 活动结束时间, 默认7天以后
        actext = data.get('actext')  # 文字内容
        actype = data.get('actype')  # 类型
        forwardnum = data.get('fowardnum', 0)  # 转发数量
        likenum = data.get('likenum', 0)  # 喜欢数
        acbrowenum = data.get('browsenum', 0)  # 浏览数
        soldfakenum = data.get('soldnum', 0)   # 商品的销售量
        istop = data.get('acistop')
        prid = data.get('prid')  # 商品id
        media = data.get('media')  # 多媒体
        tags = data.get('tags')  # 右上角tag标签
        topnavid = data.get('topnavid')
        if not media or not actext or not prid or not topnavid:
            return PARAMS_MISS
        relation_product = self.sproduct.get_product_by_prid(prid)  # 关联的商品
        if not relation_product:  # 如果没有该商品
            return SYSTEM_ERROR
        # 创建活动
        acid = str(uuid.uuid1())
        add_model('Activity', **{
            'ACid': acid,
            'PRid': relation_product.PRid,
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
        })
        # 创建media
        image_num = 0  # 标志用来限制图片或视频的数量
        for img_or_vido in media:
            img_or_vido_keys = img_or_vido.keys()
            if 'amimage' in img_or_vido_keys and 'amvideo' not in img_or_vido_keys:
                """图片"""
                add_model('ActivityMedia', **{
                    'AMid': str(uuid.uuid1()),
                    'ACid': acid,
                    'AMimage': img_or_vido.get('amimage'),
                    'AMsort': img_or_vido.get('amsort', 1)
                })
                image_num += 1
                if image_num >= 9:
                    break
            elif 'amimage' not in img_or_vido_keys and 'amvideo' in img_or_vido_keys:
                """视频"""
                if image_num < 1:
                    add_model('ActivityMedia', **{
                        'AMid': str(uuid.uuid1()),
                        'ACid': acid,
                        'AMvideo': media.get('amvideo')
                    })

        # 创建tag
        if tags:
            for tag in tags:
                add_model('ActivityTag', **{
                    'ATid': str(uuid.uuid1()),
                    'ACid': acid,
                    'ATname': tag.get('atname'),
                })
        response_make_activity = import_status('add_activity_success', 'OK')
        response_make_activity['data'] = {}
        response_make_activity['data']['acid'] = acid
        return response_make_activity

    @verify_token_decorator
    def update_act(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if request.user.scope != 'SuperUser':
            return AUTHORITY_ERROR  # 权限不足
        data = request.json
        acid = data.get('acid')
        if not 'acid' in data.keys():
            return PARAMS_MISS
        acid = data.pop('adid')
