# *- coding:utf8 *-
import sys
import os
from WeiDian.control.CRecommendBanner import CRecommendBanner
from flask import jsonify
from flask_restful import Resource
sys.path.append(os.path.dirname(os.getcwd()))


class ARecommendBanner(Resource):
    def __init__(self):
        self.control_banner = CRecommendBanner()

    def get(self, recommendbanner):
        print recommendbanner
        apis = {
            "get_all": "self.control_banner.get_all()",
            "get_one": "self.control_banner.get_one()"
        }
        res = eval(apis[recommendbanner])
        return jsonify(res)

    def post(self, recommendbanner):
        """添加十荐页轮播图"""
        print recommendbanner
        apis = {
            "add_one": "self.control_banner.add_one()",
            "del_one": "self.control_banner.del_one()"
        }
        res = eval(apis[recommendbanner])
        return jsonify(res)
