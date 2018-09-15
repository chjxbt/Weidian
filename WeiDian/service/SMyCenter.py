# *- coding:utf8 *-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import MyCenter
sys.path.append(os.path.dirname(os.getcwd()))


class SMyCenter(SBase):

    @close_session
    def get_my_info_by_usid(self, usid):
        """返回我的基本数据"""
        return self.session.query(MyCenter).filter_by(USid=usid).first()
