# *- coding:utf8 *-
import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.getcwd()))
from SBase import SBase, close_session
from WeiDian.models.model import Activity


class SActivity(SBase):

    @close_session
    def get_activity_all(self):
        return self.session.query(Activity.ACid, Activity.GOid, Activity.ACtype, Activity.TopnavId, Activity.ACtext,
                                  Activity.AClikenum, Activity.AClikeFakeNum, Activity.ACbrowsenum,
                                  Activity.ACforwardnum, Activity.ACProductsSoldFakeNum, Activity.ACcreatetime,
                                  Activity.ACstarttime, Activity.ACendtime, Activity.ACistop).filter_by(
            ACisdelte=False).all()

    @close_session
    def get_activity_by_topnavid(self, navid):
        return self.session.query(Activity.ACid, Activity.GOid, Activity.ACtype, Activity.ACtext,
                                  Activity.AClikenum, Activity.AClikeFakeNum, Activity.ACbrowsenum,
                                  Activity.ACforwardnum, Activity.ACProductsSoldFakeNum, Activity.ACcreatetime,
                                  Activity.ACstarttime, Activity.ACendtime, Activity.ACistop).filter_by(
            ACisdelte=False, TopnavId=navid).all()

    @close_session
    def get_notend_activity_by_tonavid(self, navid):
        # 该导航下的所有正在进行的活动(未完成)
        all_activity = self.get_activity_by_topnavid(navid)
        pass

    @close_session
    def add_activity(self):
        pass






if __name__ == '__main__':
    test = SActivity()
    res = test.get_activity_all()
    print(res)