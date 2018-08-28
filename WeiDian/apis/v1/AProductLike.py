# *- coding:utf8 *-
from flask import jsonify
from flask_restful import Resource
from WeiDian.control.CProductLike import CProductLike


class AProductLike(Resource):
    def __init__(self):
        self.cproductlike = CProductLike()

    def post(self, productlike):
        print productlike
        apis = {
            'add_one': self.cproductlike.add_like
        }
        return jsonify(apis[productlike]())