# *- coding:utf8 *-
from flask import jsonify

from flask_restful import Resource

from WeiDian.control.COrder import COrder


class AOrder(Resource):
    def __init__(self):
        self.corder = COrder()

    def post(self, order):
        print order
        apis = {
            'create': 'self.corder.add_one()',
         }
        res = eval(apis[order])
        return jsonify(res)

    def get(self, order):
        print order
        apis = {
            'get_list': 'self.corder.get_order_list()'
        }
        res = eval(apis[order])
        return jsonify(res)
