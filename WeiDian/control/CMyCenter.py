# -*- coding:utf8 -*-
import re
import sys
import os
import uuid

from WeiDian import logger
from WeiDian.common.import_status import import_status
from WeiDian.common.log import make_log, judge_keys
from WeiDian.common.params_require import parameter_required
from WeiDian.common.token_required import verify_token_decorator, is_tourist
from WeiDian.config.response import AUTHORITY_ERROR, SYSTEM_ERROR, TOKEN_ERROR, PARAMS_ERROR
from WeiDian.control.BaseControl import BaseMyCenterControl
from flask import request
sys.path.append(os.path.dirname(os.getcwd()))


class CMyCenter(BaseMyCenterControl):
    def __init__(self):
        from WeiDian.service.SProduct import SProduct
        self.sproduct = SProduct()
        from WeiDian.service.SUser import SUser
        self.suser = SUser()
        from WeiDian.service.SMyCenter import SMyCenter
        self.smycenter = SMyCenter()
        from WeiDian.service.SLevelRules import SLevelRules
        self.slevelrules = SLevelRules()
        from WeiDian.service.SUserAddress import SUserAddress
        self.suesraddress = SUserAddress()
        from WeiDian.service.SBankCard import SBankCard
        self.sbankcard = SBankCard()


    @verify_token_decorator
    def get_info(self):
        if is_tourist():
            return AUTHORITY_ERROR(u"未登录")
        try:
            my_info = self.smycenter.get_my_info_by_usid(request.user.id)
            my_info = self.fill_user_info(my_info)
            data = import_status("get_my_info_success", "OK")
            data["data"] = my_info
            return data
        except:
            logger.exception("get myinfo error")
            return SYSTEM_ERROR

    @verify_token_decorator
    def get_levelrules(self):
        if is_tourist():
            return AUTHORITY_ERROR(u"未登录")
        # try:
        #     with open('WeiDian/config/levelrules.cfg', 'r') as f:
        #         lr = f.read()
        #     lr = re.sub('\s', '', lr)
        #     data = import_status("get_levelrules_success", "OK")
        #     data["data"] = lr
        #     return data
        # except:
        #     logger.exception("get level rules error")
        #     return SYSTEM_ERROR
        try:
            lr_list = self.slevelrules.get_rule_list()
            map(lambda x: setattr(x, 'LRtext', re.sub('\s', '', x.LRtext)), lr_list)
            user = self.suser.get_user_by_user_id(request.user.id)
            if user.USlevel == 0:
                user.level = 'ordinary'
            if user.USlevel > 0:
                user.level = 'partner'
            user.add('level').hide('USid', 'USname', 'USheader')
            data = import_status("get_levelrules_success", "OK")
            data['data'] = lr_list
            data['userlevel'] = user.level
            return data
        except:
            logger.exception("get level rules error")
            return SYSTEM_ERROR

    @verify_token_decorator
    def get_accountinfo(self):
        if is_tourist():
            return AUTHORITY_ERROR(u"未登录")
        usid = request.user.id
        try:
            user = self.suser.get_user_by_user_id(usid)
            user.wxnum = '1234000暂取不到'
            # TODO 微信号暂时获取不到
            address = self.suesraddress.get_default_address_by_usid(usid)
            bankcard = self.sbankcard.get_bankcard_by_usid(usid)
            response = import_status("get_accountinfo_success", "OK")
            response['data'] = {
                "user": user.add('wxnum').hide('USid'),
                "address": address.UAtext,
                "bankcard": bankcard.BCnumber,
            }
            return response
        except:
            logger.exception("get account info error")
            return SYSTEM_ERROR

    @verify_token_decorator
    def get_useraddress(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR(u"未登录, 或token错误")
        try:
            adderss_list = self.suesraddress.get_address_list_by_usid(request.user.id)
            data = import_status("get_useraddress_success", "OK")
            data['data'] = adderss_list
            return data
        except:
            logger.exception("get useraddress by usid error")
            return SYSTEM_ERROR

    @verify_token_decorator
    def add_useraddress(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR(u"未登录, 或token错误")
        parameter_required("UAname", "UAphone", "UAtext")
        data = request.json
        try:
            logger.debug("get default address by usid")
            uaid = str(uuid.uuid1())
            exist_default = self.suesraddress.get_default_address_by_usid(request.user.id)
            uadefault = 1 if not exist_default else data.get("UAdefault")
            if str(uadefault) not in ['0', '1']:
                raise PARAMS_ERROR(u'uadefault参数不合法')
            if uadefault == 1 and exist_default:
                self.suesraddress.change_default_address_status(exist_default.UAid, {'UAdefault': False})
            self.suesraddress.add_model("UserAddress", **{
                "UAid": uaid,
                "USid": request.user.id,
                "UAname": data.get("UAname"),
                "UAphone": data.get("UAphone"),
                "UAtext": data.get("UAtext"),
                "UAdefault": uadefault
            })
            response = import_status("add_address_success", "OK")
            response['data'] = {
                "UAid": uaid
            }
            return response
        except:
            logger.exception("add user address error")
            return SYSTEM_ERROR

    @verify_token_decorator
    def update_address(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR(u"未登录, 或token错误")
        args = request.args.to_dict()
        make_log("args", args)
        data = request.json
        try:
            exist_default = self.suesraddress.get_default_address_by_usid(request.user.id)
            true_data = ["UAname", "UAphone", "UAtext", "UAdefault"]
            if judge_keys(true_data, data.keys()) != 200:
                return judge_keys(true_data, data.keys())
            if data.get("UAdefault") == 1 and exist_default:
                self.suesraddress.change_default_address_status(exist_default.UAid, {'UAdefault': False})
            update_address = self.suesraddress.update_address(args["uaid"], data)
            make_log("update_news", update_address)
            if not update_address:
                return SYSTEM_ERROR
            response = import_status("update_useraddress_success", "OK")
            response['data'] = {"uaid": args["uaid"]}
            return response
        except:
            logger.exception("update address error")
            return SYSTEM_ERROR

    @verify_token_decorator
    def del_address(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR(u"未登录, 或token错误")
        data = request.json
        true_data = ["UAid"]
        if judge_keys(true_data, data.keys()) != 200:
            return judge_keys(true_data, data.keys())
        del_address = self.suesraddress.delete_address(data.get("UAid"))
        if not del_address:
            return SYSTEM_ERROR
        response = import_status("delete_useraddress_success", "OK")
        response['data'] = {"uaid": data.get("UAid")}
        return response









