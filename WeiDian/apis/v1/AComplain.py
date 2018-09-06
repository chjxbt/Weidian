# *- coding:utf8 *-
import sys
import os
from flask import jsonify
from flask_restful import Resource
from WeiDian.control import CComplain
sys.path.append(os.path.dirname(os.getcwd()))


class AComplain(Resource):
    def __init__(self):
        self.control_complain = CComplain()

    def get(self, complain):
        print complain
        apis = {
            "get_all": "self.control_complain.get_all()",
            "get_one": "self.control_complain.get_one()",
        }
        res = eval(apis[complain])
        return jsonify(res)

    def post(self, complain):
        """添加活动"""
        print complain
        apis = {
            "add_one": "self.control_complain.add_one()",
            "del_one": "self.control_complain.delete_one()",
            "stop_one": "self.control_complain.stop_one()",
            "update_act": "self.control_complain.update_complain()"
        }
        res = eval(apis[complain])
        return jsonify(res)
