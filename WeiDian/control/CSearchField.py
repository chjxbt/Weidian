# *- coding:utf8 *-
import sys
import os

from WeiDian.common.import_status import import_status

sys.path.append(os.path.dirname(os.getcwd()))
from flask import request

class CSearchField():
    def __init__(self):
        from WeiDian.service.SSearchField import SSearchField
        self.s_searchfield = SSearchField()

    def get_all(self):
        """活动内的所有商品字段"""
        args = request.args.to_dict()
        lasting = args.get('lasting', 'true')
        sf_list = self.s_searchfield.get_all_searchfield()
        if lasting == 'true':
            sf_list = self.s_searchfield.get_lasting_searchfield()
        data = import_status("get_serachfield_success", "OK")
        data['data'] = sf_list
        return data
