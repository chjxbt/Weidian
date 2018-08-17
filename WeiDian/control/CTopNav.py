# *- coding:utf8 *-
import sys
import os
from datetime import datetime

from WeiDian.common.import_status import import_status
from WeiDian.config.response import PARAMS_MISS

sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import json
import uuid


class CTopNav():
    def __init__(self):
        from WeiDian.service.STopNav import STopNav
        self.s_topnav = STopNav()

    def get_all(self):
        res = self.s_topnav.get_all()
        data = import_status('get_nav_list_success', "OK")
        data['data'] = res
        return data
