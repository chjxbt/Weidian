# *- coding:utf8 *-
import sys
import os
from flask import jsonify
from flask_restful import Resource
from WeiDian.control import CBanner
sys.path.append(os.path.dirname(os.getcwd()))


class AActivityComment(Resource):
    def __init__(self):
        from WeiDian.control.CActivityComment import CActivityComment
        self.cactivitycomment = CActivityComment()

    def post(self, activitycomment):
        print activitycomment
        apis = {
            'add_comment': self.cactivitycomment.add_comment,
            'del_comment': self.cactivitycomment.del_comment_admin,
        }
        res = apis[activitycomment]()
        return jsonify(res)

    def get(self, activitycomment):
        print activitycomment
        apis = {
            'get_list': self.cactivitycomment.get_comment_list,  #
            'get_comment_with_apply': self.cactivitycomment.get_comment_with_apply,
        }
        res = apis[activitycomment]()
        return jsonify(res)

