# -*- coding:utf8 -*-
import sys
import os
from datetime import datetime

from WeiDian import logger
from WeiDian.common.timeformat import format_for_db
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
    def get_image(self):
        if is_tourist():
            return AUTHORITY_ERROR(u"未登录")
        args = request.args.to_dict()
        lasting = args.get('lasting', 'true')
        logger.info("get image args is %s", args)
        try:
            logger.debug("get my image list")
            adimage_list = self.sadimage.get_myimage()
            if lasting == 'true':
                now_time = datetime.strftime(datetime.now(), format_for_db)
                adimage_list = filter(lambda adimage: adimage.AIstarttime < now_time < adimage.AIendtime, adimage_list)
            for adimage in adimage_list:
                adimage.hide('AIurl')
            data = import_status("get_adimage_success", "OK")
            data['data'] = adimage_list
            return data
        except:
            logger.exception("get ad_image by aiid error")
            return SYSTEM_ERROR(u"无底部图片")



