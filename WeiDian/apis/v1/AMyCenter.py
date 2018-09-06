# -*- coding:utf8 -*-
import sys
import os
from flask import jsonify
from flask_restful import Resource
from WeiDian.control import CMyCenter
sys.path.append(os.path.dirname(os.getcwd()))


class AMyCenter(Resource):
    def __init__(self):
        self.control_mycenter = CMyCenter()

    def get(self, myinfo):
        print myinfo
        apis = {
            "get_info": "self.control_mycenter.get_info()"
        }
        res = eval(apis[myinfo])
        return jsonify(res)
