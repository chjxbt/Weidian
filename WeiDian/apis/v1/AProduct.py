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
        return res