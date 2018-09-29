# -*- coding:utf8 -*-
import json
import sys
import os
from flask import jsonify
from flask_restful import Resource
from WeiDian.control import CActivity
sys.path.append(os.path.dirname(os.getcwd()))


class AActivity(Resource):
    def __init__(self):
        self.control_activity = CActivity()

    def get(self, activity):
        print activity
        apis = {
            "get_all": "self.control_activity.get_all()",
            "get_one": "self.control_activity.get_one()",
            "get_activity_list_by_actitle": "self.control_activity.get_activity_list_by_actitle()"
        }
        res = eval(apis[activity])
        # res = {7777:"666"}
        return jsonify(res)

    def post(self, activity):
        """添加活动"""
        print activity
        apis = {
            "add_one": "self.control_activity.add_one()",
            "del_one": "self.control_activity.delete_one()",
            "stop_one": "self.control_activity.stop_one()",
            "update_act": "self.control_activity.update_activity()",
            "share_qrcode": "self.control_activity.share_activity()",
            "generate_poster": "self.control_activity.generate_poster()"
        }
        res = eval(apis[activity])
        return jsonify(res)
