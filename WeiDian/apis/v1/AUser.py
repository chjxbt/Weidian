# *- coding:utf8 *-
import sys
import os
from flask import jsonify
from flask_restful import Resource
from WeiDian.control.Cuser import CUser
sys.path.append(os.path.dirname(os.getcwd()))


class AUser(Resource):
    def __init__(self):
        self.cuser = CUser()

    def post(self, user):
        print user
        apis = {
            'login': 'self.cuser.login()',
            # 'get_wx_config': 'self.cuser.get_wx_config()'
        }
        res = eval(apis[user])
        return jsonify(res)

    def get(self, user):
        print user
        apis = {
            'get_accesstoken': 'self.cuser.get_accesstoken()',
            'get_wx_config': 'self.cuser.get_wx_config()'
        }
        res = eval(apis[user])
        return jsonify(res)
