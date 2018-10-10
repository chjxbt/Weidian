# *- coding:utf8 *-
import sys
import os
from flask import jsonify
from flask_restful import Resource
from WeiDian.control.CSuperUser import CSuperUser
sys.path.append(os.path.dirname(os.getcwd()))


class ASuperUser(Resource):

    def __init__(self):
        self.csuperuser = CSuperUser()

    def get(self, super):
        print super
        apis = {
            'get_all_suser': "self.csuperuser.get_all_admin_by_filter()"
        }
        res = eval(apis[super])
        return jsonify(res)

    def post(self, super):
        print super
        apis = {
            'login': 'self.csuperuser.login()',
            'update_info': 'self.csuperuser.update_suerinfo()',
            'add_admin': "self.csuperuser.add_admin_by_superadmin()",
            'update_other_admin': "self.csuperuser.superadmin_to_update_others()"
        }
        res = eval(apis[super])
        return jsonify(res)
