# *- coding:utf8 *-
import sys
import os

from flask import jsonify

sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource

from WeiDian.control.CSearchField import CSearchField

class ASearchField(Resource):
    def __init__(self):
        self.control_searchfield = CSearchField()

    def get(self, searchfield):
        print searchfield
        apis = {
            'get_all': 'self.control_searchfield.get_all()'
        }
        res = eval(apis[searchfield])
        return jsonify(res)

    def post(self, searchfield):
        pass
