# *- coding:utf8 *-
import sys
import os
from datetime import datetime

from sqlalchemy.orm import Session

from WeiDian.common.import_status import import_status
from WeiDian.common.timeformat import format_for_db

sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import json
import uuid


class CHotMessage():
    def __init__(self):
        from WeiDian.service.SHotMessage import SHotMessage
        self.s_hotmessage = SHotMessage()

    def get_all(self):
        """活动所有热文"""
        args = request.args.to_dict()
        lasting = args.get('lasting', 'true')
        hot_list = self.s_hotmessage.get_all_hot()
        if lasting == 'true':
            hot_list = self.s_hotmessage.get_lasting_hot()
        data = import_status("get_hotmessage_list_success", "OK")
        data['data'] = hot_list
        return data