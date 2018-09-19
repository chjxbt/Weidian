# *- coding:utf8 *-
import sys
import os
import uuid

from SBase import SBase, close_session
from WeiDian.models.model import MyCenter, IdentifyingCode

sys.path.append(os.path.dirname(os.getcwd()))


class SMyCenter(SBase):

    @close_session
    def get_my_info_by_usid(self, usid):
        """返回我的基本数据"""
        return self.session.query(MyCenter).filter_by(USid=usid).first()

    @close_session
    def get_uptime_by_utel(self, utel):
        return self.session.query(IdentifyingCode.ICtime).filter_by(ICtelphone=utel) \
            .order_by(IdentifyingCode.ICtime.desc()).first()

    @close_session
    def get_inforcode_by_usphone(self, usphone):
        return self.session.query(IdentifyingCode).filter_by(ICtelphone=usphone).order_by(IdentifyingCode.ICtime.desc()).first()



    @close_session
    def add_inforcode(self, utel, code, time):
        new_infocode = IdentifyingCode()
        new_infocode.ICid = str(uuid.uuid1())
        new_infocode.ICtelphone = utel
        new_infocode.ICcode = code
        new_infocode.ICtime = time
        self.session.add(new_infocode)
        self.session.commit()
        self.session.close()
        return True