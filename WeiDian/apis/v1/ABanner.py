# *- coding:utf8 *-
import sys
import os

from flask import jsonify

sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource

from WeiDian.control import CBanner


class ABanner(Resource):
    def __init__(self):
        self.cbanner = CBanner()

    def get(self, banner):
        print banner
        apis = {
            'get_all': 'self.cbanner.get_all()',
            'get_one': 'self.cbanner.get_one()'
        }
        res = eval(apis[banner])
        return jsonify(res)
    def post(self, banner):
        """添加首页轮播图"""
        print banner
        apis = {
            'add_one': 'self.cbanner.add_one()'
        }
        res = eval(apis[banner])
        return res
