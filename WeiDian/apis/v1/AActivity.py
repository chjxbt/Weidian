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
            "get_activity_list_by_actitle": "self.control_activity.get_activity_list_by_actitle()",
            "get_show_type": "self.control_activity.get_show_type()",
            "get_all_tags": "self.control_activity.get_exist_tags()"
        }
        res = eval(apis[activity])
        return jsonify(res)

    def post(self, activity):
        """添加活动"""
        print activity
        apis = {
            "add_one": "self.control_activity.add_one()",
            "del_one": "self.control_activity.delete_one()",
            "stop_one": "self.control_activity.stop_one()",
            "update_act": "self.control_activity.update_activity()",
            "upload_tags": "self.control_activity.upload_tags()",
            "share_qrcode": "self.control_activity.share_activity()",
            "set_show_type": "self.control_activity.set_show_type()",
            "del_exist_tags": "self.control_activity.del_exist_tags()",
            "generate_poster": "self.control_activity.generate_poster()",
            "upload_home_images": "self.control_activity.upload_home_images()",
        }
        res = eval(apis[activity])
        return jsonify(res)
