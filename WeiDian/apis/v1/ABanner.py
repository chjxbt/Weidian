# *- coding:utf8 *-
import sys
import os
from flask import jsonify
from flask_restful import Resource
from WeiDian.control import CBanner
sys.path.append(os.path.dirname(os.getcwd()))


class ABanner(Resource):
    def __init__(self):
        self.cbanner = CBanner()

    def get(self, banner):
        print banner
        apis = {
            "get_all": "self.cbanner.get_all()",
            "get_one": "self.cbanner.get_one()"
        }
        res = eval(apis[banner])
        return jsonify(res)

    def post(self, banner):
        """添加首页轮播图"""
        print banner
        apis = {
            "add_one": "self.cbanner.add_one()",
            "del_one": "self.cbanner.del_one()"
        }
        res = eval(apis[banner])
        return res
