# -*- coding:utf8 -*-
import sys
import os
from datetime import datetime
import uuid
import re
from WeiDian import logger
from WeiDian.common.timeformat import format_for_db
from flask import request
from WeiDian.config.response import AUTHORITY_ERROR, SYSTEM_ERROR, PARAMS_MISS
from WeiDian.common.import_status import import_status
from WeiDian.common.timeformat import get_db_time_str
from WeiDian.common.token_required import verify_token_decorator, is_tourist, is_admin, is_partner
sys.path.append(os.path.dirname(os.getcwd()))


class CAdImage():

    def __init__(self):
        from WeiDian.service.SAdImage import SAdImage
        self.sadimage = SAdImage()
        from WeiDian.service.SActivity import SActivity
        self.sactivity = SActivity()
        self.add_image_params = ['aiimage', "aitype"]

    @verify_token_decorator
    def get_image(self):
        if is_tourist():
            return AUTHORITY_ERROR(u"未登录")
        args = request.args.to_dict()
        lasting = args.get('lasting', 'true')
        logger.debug("get image args is %s", args)
        try:
            logger.info("get my image list")
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

    @verify_token_decorator
    def add_image(self):
        if not is_admin():
            return AUTHORITY_ERROR(u"权限不足")
        # parameter_required(*self.add_image_params)
        data = request.json
        adimage_list_web = data.get("adimage", [])
        if not adimage_list_web:
            raise PARAMS_MISS('adimage')
        for adimage_web in adimage_list_web:
            aitype = adimage_web.get("aitype")
            adimage = {
                'AIimage': adimage_web.get("aiimage"),
                'AItype': adimage_web.get("aitype"),
                'AIsize': adimage_web.get("aisize"),
                'ACid': adimage_web.get("acid"),
            }
            adimage_list = self.sadimage.get_image_by_aitype(aitype)
            if aitype < 8:
                if adimage_list:
                    update_result = self.sadimage.update_image(adimage_list[0].AIid, adimage)
                    if not update_result:
                        raise SYSTEM_ERROR(u"数据更新异常")
                else:
                    adimage['AIid'] = str(uuid.uuid1())
                    self.sadimage.add_model("AdImage", **adimage)

            else:
                if len(adimage_list) == 2:
                    adimage['AIcreatetime'] = get_db_time_str()
                    update_result = self.sadimage.update_image(adimage_list[1].AIid, adimage)
                    if not update_result:
                        raise SYSTEM_ERROR(u"数据更新异常")
                else:
                    adimage['AIid'] = str(uuid.uuid1())
                    self.sadimage.add_model("AdImage", **adimage)
        return import_status('save_photo_success', 'OK')

    @verify_token_decorator
    def get_image_by_aitype(self):
        if is_tourist():
            raise AUTHORITY_ERROR(u"未登录")
        aitype = request.args.to_dict().get("aitype")
        logger.debug('get aitype %s, and type of aitype %s', aitype, type(aitype))
        if re.match(r'^[0-9]+$', str(aitype)):
            aitype = int(aitype)
        else:
            aitype = -1

        if aitype == -1:
            if is_partner():
                adimage_list = self.sadimage.get_image_by_aitype(5)
            else:
                adimage_list = self.sadimage.get_image_by_aitype(4)
        else:
            adimage_list = self.sadimage.get_image_by_aitype(aitype)

        res = import_status('get_adimage_success', 'OK')
        if adimage_list:
            if aitype < 8:
                res['data'] = adimage_list[0]
                return res
            else:
                res['data'] = adimage_list
                return res
        res['message'] = u'尚未添加图片'
        return res
