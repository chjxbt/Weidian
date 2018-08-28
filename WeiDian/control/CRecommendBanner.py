# *- coding:utf8 *-
import sys
import os
import uuid
from flask import request
from datetime import datetime, timedelta
from WeiDian.common.TransformToList import add_model
from WeiDian.common.import_status import import_status
from WeiDian.common.timeformat import format_for_db
from WeiDian.common.token_required import verify_token_decorator, is_admin, is_partner
from WeiDian.config.response import SYSTEM_ERROR, AUTHORITY_ERROR, TOKEN_ERROR, PARAMS_MISS
sys.path.append(os.path.dirname(os.getcwd()))


class CRecommendBanner():
    def __init__(self):
        from WeiDian.service.SRecommendBanner import SRecommendBanner
        self.srecommendbanner = SRecommendBanner()
        from WeiDian.service.SProduct import SProduct
        self.sproduct = SProduct()

    def get_all(self):
        args = request.args.to_dict()
        if not is_partner():
            return AUTHORITY_ERROR
        print '是合伙人'
        lasting = args.get('lasting', 'true')  # 有效时间内的轮播
        if lasting == 'true':
            banner_list = self.srecommendbanner.get_all_lasting_banner()
        else:
            banner_list = self.srecommendbanner.get_all_banner()
        data = import_status("get_recommendbanner_success", "OK")
        data['data'] = banner_list
        return data

    def get_one(self):
        args = request.args.to_dict()
        if not is_partner():
            return AUTHORITY_ERROR
        print '是合伙人'
        rbid = args.get('rbid')
        if rbid:
            banner = self.srecommendbanner.get_one_by_rbid(rbid)
            if banner:
                banner = self.fill_product(banner)
                data = import_status("get_recommendbanner_success", "OK")
                data['data'] = banner
                return data
            else:
                return SYSTEM_ERROR

    @verify_token_decorator
    def add_one(self):
        """添加一个轮播图, 需要管理员的登录状态"""
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if not is_admin():
            return AUTHORITY_ERROR  # 权限不足
        data = request.json
        now_time = datetime.strftime(datetime.now(), format_for_db)
        rbstarttime = data.get('rbstarttime', now_time)  # 轮播 开始时间
        rbstarttime_str_to_time = datetime.strptime(rbstarttime, format_for_db)
        one_days_later = datetime.strftime(
            rbstarttime_str_to_time +
            timedelta(
                days=1),
            format_for_db)
        rbentime = data.get('rbendtime', one_days_later)  # 轮播结束时间, 默认1天以后
        rbid = str(uuid.uuid1())
        rbimage = data.get('rbimage')
        rbsort = data.get('rbsort')
        prid = data.get('prid')
        if not rbimage or not prid:
            return PARAMS_MISS
        if not self.sproduct.get_product_by_prid(prid):
            return SYSTEM_ERROR
        add_model('RecommendBanner', **{
            'RBid': rbid,
            'RBimage': rbimage,
            'RRid': prid,
            'RBstarttime': rbstarttime,
            'RBendtime': rbentime,
            'RBsort': rbsort
        })
        response_make_banner = import_status(
            'add_recommendbanner_success', 'OK')
        response_make_banner['data'] = {'rbid': rbid}
        return response_make_banner

    @verify_token_decorator
    def del_one(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if not is_admin():
            return AUTHORITY_ERROR  # 权限不足
        data = request.json
        rbid = data.get('rbid')
        if not rbid:
            return PARAMS_MISS
        if not self.srecommendbanner.del_banner(rbid):
            return SYSTEM_ERROR
        response_make_banner = import_status(
            'del_recommendbanner_success', 'OK')
        response_make_banner['data'] = {'rbid': rbid}
        return response_make_banner

    def fill_product(self, banner):
        prid = banner.PRid
        product = self.sproduct.get_product_by_prid(prid)
        banner.product = product
        banner.add('product')
        return banner
