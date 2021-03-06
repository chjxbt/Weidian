# *- coding:utf8 *-
import sys
import os
from flask import jsonify
from flask_restful import Resource
from WeiDian.control.CShoppingCart import CShoppingCart
sys.path.append(os.path.dirname(os.getcwd()))


class AShoppingCart(Resource):
    def __init__(self):
        self.cshoppingcart = CShoppingCart()

    def post(self, shoppingcart):
        print shoppingcart
        apis = {
            'update': 'self.cshoppingcart.update_shoppingcart()',
            'delete': 'self.cshoppingcart.delete_one()',
        }
        res = eval(apis[shoppingcart])
        return jsonify(res)

    def get(self, shoppingcart):
        print shoppingcart
        apis = {
            'get_list': 'self.cshoppingcart.get_shopingcart_all()'
        }
        res = eval(apis[shoppingcart])
        return jsonify(res)

