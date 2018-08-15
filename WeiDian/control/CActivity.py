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
        from WeiDian.service.SActivityMedia import SActivityMedia
        self.smedia = SActivityMedia()
        from WeiDian.service.SActivityTag import SActivityTag
        self.stags = SActivityTag()
        from WeiDian.service.SActivityFoward import SActivityFoward
        self.foward = SActivityFoward()

    def get_all(self):
        args = request.args.to_dict()
        navid = args.get('navid')
        if navid:
            activity_list = self.sactivity.get_activity_by_topnavid(navid)
            activity_list_fill_detail = map(self.fill_detail, activity_list)
            # activity_list = get_model_return_list(activity_list_fill_detail)
            return activity_list_fill_detail
        else:
            return 'pass'

    def fill_detail(self, act):
        import ipdb
        # ipdb.set_trace()
        acid = act.ACid
        act.user = self.suser.get_user_by_user_id(act.USid)
        del act.USid
        act.media = self.smedia.get_media_by_acid(acid)
        act.stags = self.stags.get_tags_by_acid(acid)
        act.foward_num = self.foward.get_fowardnum_by_acid(acid)
        return act






