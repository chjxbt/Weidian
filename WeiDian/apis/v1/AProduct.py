# *- coding:utf8 *-
import sys
import os
from flask import jsonify
from flask_restful import Resource
from WeiDian.control.CProduct import CProduct
sys.path.append(os.path.dirname(os.getcwd()))


class AProduct(Resource):
    def __init__(self):
        self.cproduct = CProduct()

    def post(self, product):
        print product
        apis = {
            'add_list': 'self.cproduct.add_product_list()',
            'delete_product': 'self.cproduct.delete_product()',
            'shelves_product': 'self.cproduct.shelves_product()',
            'update_sku': 'self.cproduct.update_sku()',
            'update_product': 'self.cproduct.update_product()',
            'update_product_image': 'self.cproduct.update_product_image()',
            'update_product_bigactivity': 'self.cproduct.update_product_relate_bigactivity()',
            'update_product_prtarget': 'self.cproduct.update_product_relate_prtarget()',
            'shelf_product_or_claim_act': 'self.cproduct.shelf_product_and_claim_act()',
            'update_sku_price': 'self.cproduct.update_sku_price()',
        }
        res = eval(apis[product])
        return jsonify(res)

    def get(self, product):
        print product
        apis = {
            "get_all": 'self.cproduct.get_product_list()',
            'get_one': 'self.cproduct.get_product_one()',
            "get_one_by_productid": "self.cproduct.get_one_by_productid()",
            "get_list": "self.cproduct.get_product_pools()",
            "get_product_bigactivity": "self.cproduct.get_product_relate_bigactivity()",
            "get_product_prtarget": "self.cproduct.get_product_relate_prtarget()",
            "get_product_record": "self.cproduct.get_product_operation_record()",
        }
        res = eval(apis[product])
        return jsonify(res)