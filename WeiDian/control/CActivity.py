import sys
import os

from WeiDian.common.get_model_return_list import get_model_return_list

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

    def get_all(self):
        args = request.args.to_dict()
        navid = args.get('navid')
        if navid:
            activity_list_without_user = self.sactivity.get_activity_by_topnavid(navid)
            activity_list_fill_user = map(self.fill_user, activity_list_without_user)
            activity_list = get_model_return_list(activity_list_fill_user)
        else:
            pass
        return activity_list

    def fill_user(self, act):
        if 'USid' in act:
            act['user'] = self.suser.get_user_by_activity_id(act['ACid'])






