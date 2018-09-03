# *- coding:utf8 *-
import sys
import os
from datetime import datetime
from WeiDian.common.timeformat import format_for_db
from SBase import SBase, close_session
from WeiDian.models.model import SearchField
sys.path.append(os.path.dirname(os.getcwd()))


class SSearchField(SBase):

    @close_session
    def get_lasting_searchfield(self):
        """正在进行活动的商品字段"""
        searchfields = self.session.query(SearchField).order_by(SearchField.SFsort).all()
        now_time = datetime.strftime(datetime.now(), format_for_db)
        searchfield_list = filter(lambda sf: sf.SFstarttime < now_time < sf.SFendtime and not sf.ACisended, searchfields)
        return searchfield_list

    @close_session
    def add_searchfield(self, searchfield):
        """添加商品搜索字段"""
        self.session.add(searchfield)

    @close_session
    def update_searchfield(self, sfid, **kwargs):
        searchfield = self.session.query(SearchField).filter_by(SFid=sfid).first()
        if searchfield:
            if 'sftext' in kwargs.keys():
                searchfield.SFtext = kwargs['sftext']
            if 'sfstarttime' in kwargs.keys():
                searchfield.SFstarttime = kwargs['sfstarttime']
            if 'sfendtime' in kwargs.keys():
                searchfield.SFendtime = kwargs['sfendtime']
            if 'sfsort' in kwargs.keys():
                searchfield.SFsort = kwargs['sfsort']
            self.session.add(searchfield)
            return True
# TODO 更新搜索
    
    @close_session
    def del_searchfield(self, sfid):
        return self.session.query(SearchField).filter(SearchField.SFid == sfid).delete()

    @close_session
    def get_all_searchfield(self):
        searchfields = self.session.query(SearchField).order_by(SearchField.SFsort).all()
        return searchfields
