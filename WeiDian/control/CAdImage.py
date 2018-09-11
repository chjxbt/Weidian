# -*- coding:utf8 -*-
import sys
import os
from WeiDian import logger
from WeiDian.common.log import make_log
from flask import request
from WeiDian.config.response import AUTHORITY_ERROR, SYSTEM_ERROR, PARAMS_MISS
from WeiDian.common.import_status import import_status
from WeiDian.common.token_required import verify_token_decorator,is_tourist
sys.path.append(os.path.dirname(os.getcwd()))


class CAdImage():

    def __init__(self):
        from WeiDian.service.SAdImage import SAdImage
        self.sadimage = SAdImage()
        from WeiDian.service.SActivity import SActivity
        self.sactivity = SActivity()

    @verify_token_decorator
    def get_image_by_aiid(self):
        if is_tourist():
            return AUTHORITY_ERROR(u"未登录")
        args = request.args.to_dict()
        make_log("args", args)
        aiid = args.get('aiid')
        if not aiid:
            return PARAMS_MISS
        try:
            adimage = self.sadimage.get_image_by_aiid(aiid)
            data = import_status("get_adimage_success", "OK")
            data['data'] = adimage
            return data
        except:
            logger.exception("get ad_image by aiid error")
            return SYSTEM_ERROR



