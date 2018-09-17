# -*- coding:utf8 -*-
import json
import re
import sys
import os
import uuid

from WeiDian import logger
from WeiDian.common.import_status import import_status
from WeiDian.common.params_require import parameter_required
from WeiDian.common.token_required import verify_token_decorator, is_tourist
from WeiDian.config.enums import BANK_MAP
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
            logger.debug("get my info by usid")
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
            logger.debug("get level rules")
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
            logger.debug("get user info by usid")
            user.wxnum = '1234000暂取不到'
            # TODO 微信号暂时获取不到
            address = self.suesraddress.get_default_address_by_usid(usid)
            logger.debug("get address info by usid")
            bankcard = self.sbankcard.get_bankcard_by_usid(usid)
            logger.debug("get bankcard info by usid")
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

    """用户地址信息"""
    @verify_token_decorator
    def get_useraddress(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR(u"未登录, 或token错误")
        try:
            adderss_list = self.suesraddress.get_address_list_by_usid(request.user.id)
            logger.debug("get address list")
            data = import_status("get_useraddress_success", "OK")
            data['data'] = adderss_list
            return data
        except:
            logger.exception("get useraddress by usid error ")
            return SYSTEM_ERROR

    @verify_token_decorator
    def add_useraddress(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR(u"未登录, 或token错误")
        parameter_required("UAname", "UAphone", "UAtext")
        data = request.json
        logger.info("this is useraddress data %s", data)
        try:
            uaid = str(uuid.uuid1())
            logger.debug("get default address by usid")
            exist_default = self.suesraddress.get_default_address_by_usid(request.user.id)
            uadefault = True if not exist_default else data.get("UAdefault")
            if str(uadefault) not in ['True', 'False']:
                raise PARAMS_ERROR(u'uadefault参数不合法')
            if uadefault is True and exist_default:
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
        logger.info("this is address args %s", args)
        data = request.json
        logger.info("this is address data %s", data)
        try:
            exist_default = self.suesraddress.get_default_address_by_usid(request.user.id)
            parameter_required("UAname", "UAphone", "UAtext", "UAdefault")
            if data.get("UAdefault") == 1 and exist_default:
                self.suesraddress.change_default_address_status(exist_default.UAid, {'UAdefault': False})
            update_address = self.suesraddress.update_address(args["uaid"], data)
            logger.debug("update address accress ")
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
        logger.info("this is del address data %s", data)
        parameter_required("UAid")
        try:
            logger.debug("del address")
            del_address = self.suesraddress.delete_address(data.get("UAid"))
            if not del_address:
                return SYSTEM_ERROR
            response = import_status("delete_useraddress_success", "OK")
            response['data'] = {"uaid": data.get("UAid")}
            return response
        except:
            logger.exception("del address error")
            return SYSTEM_ERROR

    """省市区地址"""
    def get_province(self):
        try:
            province_list = self.sbankcard.get_province()
            logger.debug("get province")
            map(lambda x: x.hide('_id'), province_list)
            res = import_status("get_province_list_success", "OK")
            res["data"] = province_list
            return res
        except:
            logger.exception("get province error")
            return SYSTEM_ERROR

    def get_city_by_provincenum(self):
        args = request.args.to_dict()
        logger.info("get city list args is %s", args)
        parameter_required("province_id")
        province_id = args["province_id"]
        try:
            logger.debug("get citylist by province_id")
            city_list = self.sbankcard.get_citylist_by_provinceid(province_id)
            map(lambda x: x.hide('_id'), city_list)
            res = import_status("get_city_list_success", "OK")
            res["data"] = city_list
            return res
        except:
            logger.exception("get city list error")
            return SYSTEM_ERROR

    def get_area_by_citynum(self):
        args = request.args.to_dict()
        logger.info("get area args is %s", args)
        parameter_required('city_id')
        city_id = args['city_id']
        try:
            logger.debug("get arealist by cityid")
            area_list = self.sbankcard.get_arealist_by_cityid(city_id)
            map(lambda x: x.hide('_id'), area_list)
            res = import_status("get_area_list_success", "OK")
            res["data"] = area_list
            return res
        except:
            logger.exception("get area list error")
            return SYSTEM_ERROR





    """银行卡部分"""
    @verify_token_decorator
    def add_bankcard(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR(u"未登录, 或token错误")
        data = request.json
        logger.info("this add bankcard info %s", data)
        parameter_required('BCusername', 'BCnumber', 'BCbankname', 'BCaddress')
        try:
            bankcardcount = self.sbankcard.get_bankcard_count(request.user.id)
            logger.debug("bankcard count is %s", bankcardcount)
            if bankcardcount >= 1:
                return SYSTEM_ERROR(u'已有绑定银行卡')
            bcid = str(uuid.uuid1())
            self.sbankcard.add_model("BankCard", **{
                "BCid": bcid,
                "USid": request.user.id,
                "BCusername": data.get("BCusername"),
                "BCnumber": data.get("BCnumber"),
                "BCbankname": data.get("BCbankname"),
                "BCaddress": data.get("BCaddress")
            })
            response = import_status("add_bank_card_success", "OK")
            response['data'] = {"BCid": bcid}
            return response
        except:
            logger.exception("add bankcard error")
            return SYSTEM_ERROR

    @verify_token_decorator
    def get_bankcard(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR(u"未登录, 或token错误")
        args = request.args.to_dict()
        logger.info("get bankcard this is args %s", args)
        try:
            logger.debug("get bankcard")
            my_bankcard = self.sbankcard.get_bankcard_by_usid(request.user.id)
            response = import_status("get_bankcard_success", "OK")
            response['data'] = my_bankcard
            return response
        except:
            logger.exception("get bankcard error")
            return SYSTEM_ERROR



    @verify_token_decorator
    def get_bankname_list(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR(u"未登录, 或token错误")
        data = import_status("get_useraddress_success", "OK")
        data['data'] = BANK_MAP
        return data






