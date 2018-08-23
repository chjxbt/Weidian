# *- coding:utf8 *-
from flask import jsonify
from flask_restful import Resource

from WeiDian.control.CShoppingCart import CShoppingCart

class AShoppingCart(Resource):
    def __init__(self):
        self.cshoppingcart = CShoppingCart()

    def post(self, shoppingcart):
        print shoppingcart
        apis = {
            'update': 'self.cshoppingcart.update_shoppingcart()',
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

