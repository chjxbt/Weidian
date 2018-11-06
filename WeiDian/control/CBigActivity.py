# -*- coding:utf8 -*-
import sys
import os
import uuid
from datetime import datetime, timedelta

from WeiDian import logger
from WeiDian.common.get_model_return_list import get_model_return_dict
from WeiDian.common.import_status import import_status
from WeiDian.common.params_require import parameter_required
from WeiDian.common.timeformat import get_db_time_str, format_for_db, get_web_time_str, format_for_web_second
from WeiDian.common.token_required import verify_token_decorator, is_admin
from WeiDian.config.response import TOKEN_ERROR, SYSTEM_ERROR, AUTHORITY_ERROR, PARAMS_ERROR, NOT_FOUND
from WeiDian.control.BaseControl import BaseActivityControl
from WeiDian.models.model import BigActivity
from flask import request
sys.path.append(os.path.dirname(os.getcwd()))


class CBigActivity(BaseActivityControl):
    def __init__(self):
        from WeiDian.service.SActivity import SActivity
        self.sactivity = SActivity()
        from WeiDian.service.SBigActivity import SBigActivity
        self.sbigactivity = SBigActivity()
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
        from WeiDian.service.SUser import SUser
        self.suser = SUser()
        self.empty = ['', None, [], {}]

    @verify_token_decorator
    def get_bigactivity(self):
        """获取专题内容"""
        if not hasattr(request, 'user'):
            raise TOKEN_ERROR(u"未登录/token错误")
        args = request.args.to_dict()
        logger.debug("get bigactivity content args is %s", args)
        parameter_required('baid', 'page_num', 'page_size')
        baid = args.get('baid')
        page_num = args.get('page_num')
        page_size = args.get('page_size')
        page_num = 1 if not page_num else int(page_num)
        page_size = 5 if not page_size else int(page_size)
        try:
            activity_list = self.sactivity.get_bigactivity_by_baid(baid, page_num, page_size)
            for activity in activity_list:
                self.sactivity.update_view_num(activity.ACid)
                self.fill_detail(activity)
                self.fill_like_num(activity)
                self.fill_type(activity)
                activity.fill(activity.AClinkvalue, 'aclinkvalue')

                if activity.ACSkipType == 2:
                    self.fill_soldnum(activity)
                    self.fill_product(activity)
                    activity.fill('product', 'skip_type')
                    activity.fill('商品', 'zh_skip_type')
                activity.ACstarttime = get_web_time_str(activity.ACstarttime)
                activity.ACendtime = get_web_time_str(activity.ACendtime)

            total_count = self.sactivity.get_bigactivity_count_by_baid(baid)
            banner = get_model_return_dict(self.sbigactivity.get_bigactivity_banner_by_baid(baid))['BAimage']
            batype = get_model_return_dict(self.sbigactivity.get_bigactivity_banner_by_baid(baid))['BAtype']
            response = import_status("get_bigactivity_success", "OK")
            response['data'] = {
                'activity': activity_list,
                'banner': banner,
                'batype': batype,
                'total_count': total_count
            }
            return response
        except Exception as e:
            logger.exception("get bigactivity error")
            raise SYSTEM_ERROR()

    @verify_token_decorator
    def get_bigactivity_list(self):
        """后台获取专题列表"""
        if not is_admin():
            raise TOKEN_ERROR(u"请使用管理员账号重新登录")
        args = request.args.to_dict()
        logger.debug("get bigactivitys args is %s", args)
        BAtype = args.get('type')  # 0 图片, 1 非图片
        try:
            big_act_list = self.sbigactivity.get_big_act_list(BAtype)
            # map(lambda x: x.clean.add('BAid', 'BAtext'), big_act_list)
            for big_act in big_act_list:
                big_act.BAstarttime = get_web_time_str(big_act.BAstarttime)
                big_act.BAendtime = get_web_time_str(big_act.BAendtime)
            response = import_status("get_bigactivity_success", "OK")
            response['data'] = big_act_list
            return response
        except Exception as e:
            logger.exception("get bigactivity list error")
            raise SYSTEM_ERROR(u'专题列表失败')

    @verify_token_decorator
    def get_one_bigact(self):
        """获取单个专题内容"""
        if not is_admin():
            raise AUTHORITY_ERROR(u'非管理员权限')
        args = request.args.to_dict()
        parameter_required('baid')
        logger.info("args is %s", args)
        try:
            big_act = self.sbigactivity.get_one_big_act(args["baid"])
            logger.debug("get one big act")
            response = import_status("get_bigactivity_success", "OK")
            response["data"] = big_act
            return response
        except:
            logger.exception("get one big act error")
            return SYSTEM_ERROR(u"服务器繁忙")

    @verify_token_decorator
    def add_activities_to_bigact(self):
        if not is_admin():
            raise TOKEN_ERROR(u'请使用管理员登陆')
        args = parameter_required(u'ACid_list', u'BAid')
        acid_list = args.get('ACid_list')
        baid = args.get('BAid')
        success_acvity = []  # 不是跳转到商品的推文将会忽略
        for acid in acid_list:
            activity = self.sactivity.get_activity_by_acid(acid)
            if not activity or activity.ACSkipType != 2:
                continue
            self.sactivity.update_activity_by_acid(acid, {
                'BAid': baid
            })
            success_acvity.append(acid)
        big_activity = self.sbigactivity.get_one_big_act(baid)
        if not big_activity:
            raise NOT_FOUND(u'该专题不存在')
        if big_activity.BAtype == 0:
            raise NOT_FOUND(u'该专题为大图')
        msg = u'成功{}条'.format(len(success_acvity))
        return {"message": msg, "status": 200}

    @verify_token_decorator
    def get_home_banner(self):
        """获取首页轮播图"""
        if not hasattr(request, 'user'):
            raise TOKEN_ERROR(u"未登录, 或token错误")
        args = request.args.to_dict()
        lasting = args.get('lasting', 'true')
        logger.info("get home banner args is %s", args)
        try:
            baimages = self.sbigactivity.get_home_banner_by_said()
            logger.info("get baimages is %s", baimages)
            # if not baimages:
                # raise SYSTEM_ERROR(u"系统繁忙")
            if lasting == 'true':
                baimages = filter(lambda img: img.BAstarttime < get_db_time_str() < img.BAendtime, baimages)
            for img in baimages:
                img.BAstarttime = get_web_time_str(img.BAstarttime)
                img.BAendtime = get_web_time_str(img.BAendtime)
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
            # if not baimages:
            #     raise SYSTEM_ERROR(u"系统繁忙")
            if lasting == 'true':
                baimages = filter(lambda img: img.BAstarttime < get_db_time_str() < img.BAendtime, baimages)
            for img in baimages:
                img.BAstarttime = get_web_time_str(img.BAstarttime)
                img.BAendtime = get_web_time_str(img.BAendtime)
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
        now_time = datetime.strftime(datetime.now(), format_for_web_second)
        BAstarttime = get_db_time_str(data.get('BAstarttime', now_time))
        BAstarttime_str_to_time = datetime.strptime(BAstarttime, format_for_db)
        seven_days_later = datetime.strftime(BAstarttime_str_to_time + timedelta(days=365), format_for_db)  # 七天以后
        BAendtime = get_db_time_str(data.get('BAendtime', seven_days_later))
        BAisdisplay = True if data.get('BAisdisplay') == 1 else False
        model_dict = {
            "BAid": BAid,
            "BAtext": data.get('BAtext'),
            "BAimage": BAimage,
            "BAstarttime": BAstarttime,
            "BAendtime": BAendtime,
            "BAsort": data.get('BAsort', 0),
            "BAposition": 0,
        }
        try:
            batype = int(data.get('BAtype', 1))  #  0 图片,1 非图片
            if batype not in [0, 1]:
                raise TypeError()
            model_dict['BAtype'] = batype
        except TypeError as e:
            raise PARAMS_ERROR(u'batype参数错误')
        if batype == 0:   # 0 图片
            BAlongimg = data.get('BAlongimg')
            if not BAlongimg:
                raise PARAMS_ERROR(u'缺少参数BAlongimg')
            model_dict['BAlongimg'] = BAlongimg
            model_dict['BAisdisplay'] = False
        else:
            model_dict['BAisdisplay'] = BAisdisplay
        try:
            self.sbigactivity.add_model("BigActivity", **model_dict)
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
        BAstarttime = get_db_time_str(data.get('BAstarttime', now_time))
        BAstarttime_str_to_time = datetime.strptime(BAstarttime, format_for_db)
        seven_days_later = datetime.strftime(BAstarttime_str_to_time + timedelta(days=365), format_for_db)  # 七天以后
        BAendtime = get_db_time_str(data.get('BAendtime', seven_days_later))
        try:
            self.sbigactivity.add_model("BigActivity", **{
                "BAid": BAid,
                "BAtext": data.get('BAtext'),
                "BAimage": BAimage,
                "BAstarttime": BAstarttime,
                "BAendtime": BAendtime,
                "BAsort": data.get('BAsort', 0),
                "BAposition": 1,
                "BAisdisplay": data.get('BAisdisplay', 1)
            })

            response = import_status("create_discover_bigactivity", "OK")
            response["data"] = {
                "BAid": BAid
            }
            return response
        except:
            logger.exception("create bigactivity error")
            return SYSTEM_ERROR(u'数据错误')

    @verify_token_decorator
    def update_bigactivity(self):
        """后台修改专题"""
        if not is_admin():
            raise AUTHORITY_ERROR(u'请使用管理员账号重新登录')
        args = request.args.to_dict()
        logger.info("update big act args is %s", args)
        data = request.json
        logger.info("update big act data is %s", data)
        parameter_required('baid')
        baid = args.get('baid')
        update_act = self.sbigactivity.get_one_big_act(baid)
        if not update_act:
            raise NOT_FOUND(u'该专题不存在或已被删除')
        upinfo = {
            "BAtext": data.get('batext'),
            "BAimage": data.get('baimage'),
            "BAstarttime": get_db_time_str(data.get("bastarttime")),
            "BAendtime": get_db_time_str(data.get("baendtime")),
            "BAsort": data.get('basort'),
            "BAisdisplay": data.get('baisdisplay'),
            "BAisdelete": data.get('baisdelete')
        }
        upinfo = {k: v for k, v in upinfo.items() if v not in self.empty}
        if data.get('basort'):
            bact_changed = self.sbigactivity.get_big_act_by_filter({BigActivity.BAsort == data.get('basort')})
            if bact_changed:
                print str(bact_changed.BAid)
                print str(update_act.BAsort)
                self.sbigactivity.update_bigact(bact_changed.BAid, {"BAsort": update_act.BAsort})

        up_info = self.sbigactivity.update_bigact(baid, upinfo)
        if not up_info:
            raise SYSTEM_ERROR(u'更新数据错误')
        response = import_status("update_bigact_success", "OK")
        response["data"] = {
            "baid": baid
        }
        return response







