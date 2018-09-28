# *- coding:utf8 *-
import sys
import os
from flask import jsonify
from flask_restful import Resource
from WeiDian.config.response import APIS_WRONG
from WeiDian.control.CTask import CTask

sys.path.append(os.path.dirname(os.getcwd()))


class ATask(Resource):
    def __init__(self):
        self.ctask = CTask()

    def get(self, task):
        print(task)
        apis = {
            "get_user_task": "self.ctask.get_user_task()",
            "get_all_task": "self.ctask.get_all_task()",
            "get_all_task_type": "self.ctask.get_all_task_type()",
            "get_all_task_level": "self.ctask.get_all_task_level()",
            "get_all_raward": "self.ctask.get_all_raward()",
        }
        res = eval(apis[task])
        return jsonify(res)

    def post(self, task):
        print(task)
        apis = {
            "do_task": "self.ctask.do_task()",
            "add_task": "self.ctask.add_task()",
            "add_or_update_task_level": "self.ctask.add_or_update_task_level()",
            "upload_task_img": "self.ctask.upload_task_img()",
        }
        if task not in apis:
            raise APIS_WRONG(' %s is not found' % task)
        res = eval(apis[task])
        return jsonify(res)