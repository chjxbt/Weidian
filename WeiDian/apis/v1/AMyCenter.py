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
            "get_info": "self.control_mycenter.get_info()",
            "get_rule": "self.control_mycenter.get_levelrules()",
            "get_account_info": "self.control_mycenter.get_accountinfo()",
            "get_address": "self.control_mycenter.get_useraddress()"
        }
        res = eval(apis[myinfo])
        return jsonify(res)

    def post(self, myinfo):
        print (myinfo)
        apis = {
            "add_address": "self.control_mycenter.add_useraddress()",
            "update_address": "self.control_mycenter.update_address()",
            "del_address": "self.control_mycenter.del_address()"
        }
        res = eval(apis[myinfo])
        return jsonify(res)