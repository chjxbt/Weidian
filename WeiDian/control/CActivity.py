# *- coding:utf8 *-
import sys
import os

from sqlalchemy.orm import Session


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
        self.session = Session()

    def get_all(self):
        args = request.args.to_dict()
        navid = args.get('navid')  # 导航id
        usid = args.get('usid')  # 用户id
        if navid:
            activity_list = self.sactivity.get_activity_by_topnavid(navid)
        if usid:
            activity_list = self.sactivity.get_activity_by_usid(usid)
        else:
            activity_list = {'data': 'data'}
        activity_list = map(dict, activity_list)
        activity_list_fill_detail = map(self.fill_detail, activity_list)
        return activity_list_fill_detail

    def fill_detail(self, act):
        acid = act['ACid']
        act['user'] = self.suser.get_user_by_user_id(act['USid'])
        act['media'] = self.smedia.get_media_by_acid(acid)
        act['tags'] = self.stags.get_tags_by_acid(acid)
        act['foward'] = self.foward.get_fowardnum_by_acid(acid)
        # act.remove('USid')
        return act






