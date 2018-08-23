# *- coding:utf8 *-
import sys
import os

from flask import jsonify
from flask_restful import Resource

from WeiDian.control.CProduct import CProduct


class AProduct(Resource):
    def __init__(self):
        self.cproduct = CProduct()

    def post(self, product):
        print product
        apis = {
            'add_list': 'self.cproduct.add_product_list()',
        }
        res = eval(apis[product])
        return jsonify(res)

    def get(self, product):
        print product
        apis = {
            "get_all": 'self.cproduct.get_product_list()',
            'get_one': 'self.cproduct.get_product_one()'
        }
        res = eval(apis[product])
        return jsonify(res)