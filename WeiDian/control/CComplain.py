import sys
import os
import uuid
import logging
from datetime import datetime, timedelta
from flask import request
from WeiDian.config.response import TOKEN_ERROR, PARAMS_MISS, AUTHORITY_ERROR, SYSTEM_ERROR
from WeiDian.common.import_status import import_status
from WeiDian.common.token_required import verify_token_decorator, is_admin, token_to_usid
from WeiDian.common.TransformToList import add_model
from WeiDian.common.timeformat import format_for_db
sys.path.append(os.path.dirname(os.getcwd()))


class CComplain():
    def __init__(self):
        from WeiDian.service.SComplain import SComplain
        self.scomplain = SComplain()
        from WeiDian.service.SActivity import SActivity
        self.sactivity = SActivity()

    def get_complain_by_usid(self):
        args = request.args.to_dict()
        if not args.get("USid"):
            return PARAMS_MISS
        try:
            complain_list = self.scomplain.get_complain_by_usid(args.get("USid"))

            data = import_status("get_complain_success", "OK")
            data['data'] = complain_list
            return data
        except Exception as e:
            logging.error(e)
            return SYSTEM_ERROR

    @verify_token_decorator
    def add_complain(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        usid = request.user.id
        data = request.json
        
        orid = data.get("ORid")

