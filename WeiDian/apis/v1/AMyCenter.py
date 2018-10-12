# -*- coding:utf8 -*-
import sys
import os
from flask import jsonify
from flask_restful import Resource
from WeiDian.control import CMyCenter
sys.path.append(os.path.dirname(os.getcwd()))


class AMyCenter(Resource):
    def __init__(self):
        self.control_mycenter = CMyCenter()

    def get(self, myinfo):
        print (myinfo)
        apis = {
            "get_info": "self.control_mycenter.get_info_top()",
            "get_rule": "self.control_mycenter.get_levelrules()",
            "get_account_info": "self.control_mycenter.get_accountinfo()",
            "get_address": "self.control_mycenter.get_useraddress()",
            "get_bank_list": "self.control_mycenter.get_bankname_list()",
            "get_mybankcard": "self.control_mycenter.get_bankcard()",
            "get_province": "self.control_mycenter.get_province()",
            "get_city": "self.control_mycenter.get_city_by_provincenum()",
            "get_area": "self.control_mycenter.get_area_by_citynum()",
            "get_today_total": "self.control_mycenter.get_today_total()",
            "get_schedual_show": "self.control_mycenter.get_schedual_show()",  # 获取显示或隐藏
            "get_share_params": "self.control_mycenter.get_share_params()"
        }
        res = eval(apis[myinfo])
        return jsonify(res)

    def post(self, myinfo):
        print (myinfo)
        apis = {
            "add_address": "self.control_mycenter.add_useraddress()",
            "update_address": "self.control_mycenter.update_address()",
            "del_address": "self.control_mycenter.del_address()",
            "add_bankcard": "self.control_mycenter.add_bankcard()",
            "del_bankcard": "self.control_mycenter.del_bankcard()",
            "update_bankcard": "self.control_mycenter.update_bankcard()",
            "get_inforcode": "self.control_mycenter.get_inforcode()",
            "verify_inforcode": "self.control_mycenter.verify_inforcode()",
            "set_schedual_show": "self.control_mycenter.set_schedual_show()",
            "set_share_params": "self.control_mycenter.set_share_params()",

        }
        res = eval(apis[myinfo])
        return jsonify(res)