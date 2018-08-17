# *- coding:utf8 *-
import sys
import os

from flask import jsonify

sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource

from WeiDian.control.CHotMessage import CHotMessage


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





