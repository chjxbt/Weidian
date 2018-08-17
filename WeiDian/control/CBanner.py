# *- coding:utf8 *-
import sys
import os
from datetime import datetime

from sqlalchemy.orm import Session

from WeiDian.common.import_status import import_status
from WeiDian.common.timeformat import format_for_db
from test.errors import ApiException

sys.path.append(os.path.dirname(os.getcwd()))
from flask import request


class CBanner():
    def __init__(self):
        from WeiDian.service.SBanner import SBnner
        self.sbanner = SBnner()
        from WeiDian.service.SActivity import SActivity


    def get_all(self):
        args = request.args.to_dict()
        lasting = args.get('lasting', 'true')  # 有效时间内的轮播
        if lasting == 'true':
            banner_list = self.sbanner.get_all_lasting_banner()
        else:
            banner_list = self.sbanner.get_all_banner()
        data = import_status("get_hotmessage_list_success", "OK")
        data['data'] = banner_list
        return data

    def get_one(self):
        args = request.args.to_dict()
        baid = args.get('baid')
        if baid:
            banner = self.sbanner.get_one_by_baid(baid)
            if banner:
                data = import_status("get_activity_info_success", "OK")
                data['data'] = banner
                return data
            else:
                pass




