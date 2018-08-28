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
            "get_info": "self.control_recommend.get_list()"
        }
        res = eval(apis[recommend])
        return jsonify(res)
