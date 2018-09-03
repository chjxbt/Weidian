# *- coding:utf8 *-
import sys
import os
from flask import jsonify
from flask_restful import Resource
from WeiDian.control.CActivityLike import CActivityLike
sys.path.append(os.path.dirname(os.getcwd()))


class AActivityLike(Resource):
    def __init__(self):
        self.cactivitylike = CActivityLike()

    def post(self, activitylike):
        print activitylike
        apis = {
            "ac_like": self.cactivitylike.like_or_cancel
        }
        return jsonify(apis[activitylike]())
