# *- coding:utf8 *-
from flask import jsonify
from flask_restful import Resource
from WeiDian.control.CRecommendLike import CRecommendLike


class ARecommendLike(Resource):
    def __init__(self):
        self.crecommendlike = CRecommendLike()

    def post(self, recommendlike):
        print recommendlike
        apis = {
            "re_like": self.crecommendlike.like_or_cancel
        }
        return jsonify(apis[recommendlike]())
