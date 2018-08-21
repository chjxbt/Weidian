# *- coding:utf8 *-
import sys
import os

from flask import jsonify

sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource

from WeiDian.control import CHotMessage


class AHotMessage(Resource):

    def __init__(self):
        self.control_hotmessage = CHotMessage()

    def get(self, hotmessage):
        print hotmessage
        apis = {
            'get_all': 'self.control_hotmessage.get_all()'
        }
        res = eval(apis[hotmessage])
        return jsonify(res)

    def post(self, hotmessage):
        print hotmessage
        apis = {
            "add_one": "self.control_hotmessage.add_one()",
            "update_one": "self.control_hotmessage.update_one()",
            "del_one": "self.control_hotmessage.del_one()"
        }
        return eval(apis[hotmessage])
