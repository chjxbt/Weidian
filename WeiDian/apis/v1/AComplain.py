# *- coding:utf8 *-
import sys
import os
from flask import jsonify
from flask_restful import Resource
from WeiDian.control.CComplain import CComplain
sys.path.append(os.path.dirname(os.getcwd()))


class AComplain(Resource):
    def __init__(self):
        self.control_complain = CComplain()

    def get(self, complain):
        print complain
        apis = {
            "get_all": "self.control_complain.get_complain_by_usid()",
        }
        res = eval(apis[complain])
        return jsonify(res)

    def post(self, complain):
        """添加活动"""
        print complain
        apis = {
            "add_one": "self.control_complain.add_complain()",
            "update_status": "self.control_complain.update_status()",
        }
        res = eval(apis[complain])
        return jsonify(res)
