# *- coding:utf8 *-
import sys
import os
from flask import jsonify
from flask_restful import Resource
from WeiDian.control.CSearchField import CSearchField
sys.path.append(os.path.dirname(os.getcwd()))


class ASearchField(Resource):
    def __init__(self):
        self.control_searchfield = CSearchField()

    def get(self, searchfield):
        print searchfield
        apis = {
            "get_all": "self.control_searchfield.get_all()"
        }
        res = eval(apis[searchfield])
        return jsonify(res)

    def post(self, searchfield):
        print searchfield
        apis = {
            "add_one": "self.control_searchfield.add_one()",
            "update": "self.control_searchfield.update_searchfield()",
            "del_one": "self.control_searchfield.del_one()"
        }
        res = eval(apis[searchfield])
        return jsonify(res)
