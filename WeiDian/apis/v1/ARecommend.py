# *- coding:utf8 *-
import sys
import os
from WeiDian.control.CRecommend import CRecommend
from flask import jsonify
from flask_restful import Resource
sys.path.append(os.path.dirname(os.getcwd()))


class ARecommend(Resource):
    def __init__(self):
        self.control_recommend = CRecommend()

    def get(self, recommend):
        print recommend
        apis = {
            "get_info": "self.control_recommend.get_one()"
        }
        res = eval(apis[recommend])
        return jsonify(res)

    def post(self, recommend):
        print recommend
        apis = {
            "add_one": "self.control_recommend.add_one()",
            "update": "self.control_recommend.update_recommend()",
            "del_one": "self.control_recommend.del_one()"
        }
        res = eval(apis[recommend])
        return jsonify(res)
