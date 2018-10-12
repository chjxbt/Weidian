# *- coding:utf8 *-
import sys
import os
from flask import jsonify
from flask_restful import Resource
from WeiDian.control import CTopNav
sys.path.append(os.path.dirname(os.getcwd()))


class ATopNav(Resource):
    def __init__(self):
        self.ctopnav = CTopNav()

    def get(self, topnav):
        print topnav
        apis = {
            'get_all_topnav': 'self.ctopnav.get_all_topnav()',
            'get_home': 'self.ctopnav.get_home()',
            'get_dp': 'self.ctopnav.get_dp()'
        }
        res = eval(apis[topnav])
        return jsonify(res)

    def post(self, topnav):
        """添加首页上部导航"""
        print topnav
        apis = {
            "add_one": "self.ctopnav.add_one()",
            "del_one": "self.ctopnav.del_one()"

        }
        res = eval(apis[topnav])
        return jsonify(res)
