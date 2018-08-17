# *- coding:utf8 *-
import sys
import os
from datetime import datetime

from WeiDian.common.timeformat import format_for_db

sys.path.append(os.path.dirname(os.getcwd()))
from SBase import SBase, close_session
from WeiDian.models.model import SearchField
# from WeiDian.models.model import Activity

class SSearchField(SBase):

    @close_session
    def get_lasting_searchfield(self):
        """正在进行活动的商品字段"""
        searchfields = self.session.query(SearchField).order_by(SearchField.SFsort).all()
        now_time = datetime.strftime(datetime.now(), format_for_db)
        searchfield_list = filter(lambda sf: sf.SFstarttime < now_time < sf.SFendtime and not sf.ACisended, searchfields)
        return searchfield_list

    @close_session
    def get_all_searchfield(self):
        searchfields = self.session.query(SearchField).order_by(SearchField.SFsort).all()
        return searchfields