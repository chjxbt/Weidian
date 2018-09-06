# *- coding:utf8 *-
import sys
import os
import uuid

from flask import request
from WeiDian.config.response import TOKEN_ERROR, PARAMS_MISS, SYSTEM_ERROR
from WeiDian.common.import_status import import_status
from WeiDian.common.params_require import parameter_required
from WeiDian.common.token_required import verify_token_decorator
# sys.path.append(os.path.dirname(os.getcwd()))
from WeiDian import logger


class CComplain():
    def __init__(self):
        from WeiDian.service.SComplain import SComplain
        self.scomplain = SComplain()
        from WeiDian.service.SActivity import SActivity
        self.sactivity = SActivity()

    @verify_token_decorator
    def get_complain_by_usid(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        try:
            complain_list = self.scomplain.get_complain_by_usid(request.user.id)

            data = import_status("get_complain_success", "OK")
            data['data'] = complain_list
            return data
        except:
            logger.exception("get complain by usid error")
            return SYSTEM_ERROR

    @verify_token_decorator
    def add_complain(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        parameter_required("ORid", "COtype")
        data = request.json
        try:
            complain = self.scomplain.get_complain_by_orid(data.get("ORid"))
            logger.debug("get complain by orid", )
            if complain:
                return import_status("complain_repeat_error", "WD_ERROR", "error_complain_exit")
            coid = str(uuid.uuid1())
            self.scomplain.add_model("Complain", **{
                "COid": coid,
                "COcontent": data.get("COcontent"),
                "COtype": data.get("COtype"),
                "ORid": data.get("ORid"),
                "USid": request.user.id,
            })
            response = import_status("complain_success", "OK")
            response['data'] = {
                "COid": coid
            }
            return response
        except:
            logger.exception("add complain error")
            return SYSTEM_ERROR
