# -*- coding:utf8 -*-
import sys
import os
from flask import jsonify
from flask_restful import Resource
from WeiDian.config.response import APIS_WRONG
sys.path.append(os.path.dirname(os.getcwd()))


class AAdImage(Resource):
    def __init__(self):
        from WeiDian.control.CAdImage import CAdImage
        self.cadimage = CAdImage()

    def get(self, adimage):
        print adimage
        apis = {
            "get_myimg": "self.cadimage.get_image()",
            "get_image_by_aitype": "self.cadimage.get_image_by_aitype()"
        }
        res = eval(apis[adimage])
        return jsonify(res)

    def post(self, adimage):
        print adimage
        apis = {
            "add_image": "self.cadimage.add_image()",
        }
        if adimage not in apis:
            raise APIS_WRONG
        res = eval(apis[adimage])
        return jsonify(res)