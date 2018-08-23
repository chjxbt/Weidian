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
            'update_cart': 'self.cshoppingcart.update_shoppingcart()'
        }
        return eval(apis[shoppingcart])


