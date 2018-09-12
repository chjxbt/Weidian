# -*- coding:utf8 -*-
import sys
import os
from flask import jsonify
from flask_restful import Resource
sys.path.append(os.path.dirname(os.getcwd()))


class AAdImage(Resource):
    def __init__(self):
        from WeiDian.control.CAdImage import CAdImage
        self.cadimage = CAdImage()

    def get(self, adimage):
        print adimage
        apis = {
            "get_myimg": "self.cadimage.get_image()"
        }
        res = eval(apis[adimage])
        return jsonify(res)
