import sys
import os
from datetime import datetime
from WeiDian.common.timeformat import format_for_db
from SBase import SBase, close_session
from WeiDian.models.model import Complain
sys.path.append(os.path.dirname(os.getcwd()))


class SComplain(SBase):

    @close_session
    def get_complain_by_usid(self, usid):
        return self.session.query(Complain).filter(Complain.USid == usid).order_by(Complain.COcreatetime).all()

    @close_session
    def admin_get_all_complain(self, page_size, page_num):
        return self.session.query(Complain).order_by(Complain.COcreatetime.desc()).offset(page_size * (page_num - 1)).limit(page_size).all()

    @close_session
    def admin_get_complain_count(self):
        return self.session.query(Complain).count()

    @close_session
    def get_complain_by_oiid(self, oiid):
        return self.session.query(Complain).filter(Complain.OIid == oiid).first()

    @close_session
    def get_complain_by_coid(self, coid):
        return self.session.query(Complain).filter(Complain.COid == coid).first()

    @close_session
    def update_complain(self, coid, complain):
        return self.session.query(Complain).filter(Complain.COid == coid).update(complain)