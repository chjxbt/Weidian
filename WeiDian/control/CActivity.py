import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import json
import uuid


class CActivity():
    def __init__(self):
        from WeiDian.service.SActivity import SActivity
        self.sactivity = SActivity()
        from WeiDian.service.SActivityComment import SActivityComment
        self.sacomment = SActivityComment()
        from WeiDian.service.SActivityLike import SActivityLike
        self.salike = SActivityLike()
        from WeiDian.service.SUser import SUser
        self.suser = SUser()

    def get_activity_by_navid(self, navid):
        args = request.args.to_dict()
        navid = args.get(navid)
        activity_list = get_model_return_list(
            self.sactivity.get_activity_by_topnavid(navid))
