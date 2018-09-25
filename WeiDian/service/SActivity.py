# *- coding:utf8 *-
import sys
import os
from datetime import datetime
from WeiDian.common.timeformat import format_for_db
from SBase import SBase, close_session
from WeiDian.models.model import Activity, Product
sys.path.append(os.path.dirname(os.getcwd()))


class SActivity(SBase):

    @close_session
    def get_activity_all(self, page_num, page_size):
        """所有活动
        返回活动对象列表"""
        activity_list = self.session.query(Activity).filter_by(ACisdelete=False).offset(page_size * (page_num - 1)).limit(page_size).all()
        return activity_list

    @close_session
    def get_activity_count(self, tnid):
        return self.session.query(Activity).filter_by(ACisdelete=False, TopnavId=tnid).count()

    @close_session
    def get_activity_by_topnavid(self, tnid, page_num, page_size):
        """根据导航的id获取活动"""
        return self.session.query(Activity).filter_by(ACisdelete=False, TopnavId=tnid).order_by(Activity.ACcreatetime.desc()).offset(page_size * (page_num - 1)).limit(page_size).all()

    @close_session
    def get_activity_by_suid(self, suid, page_num, page_size):
        acvitity_list = self.session.query(Activity).filter_by(ACisdelete=False, SUid=suid).order_by(Activity.ACcreatetime.desc()).offset(page_size * (page_num - 1)).limit(page_size).all()
        return acvitity_list

    @close_session
    def get_lasting_activity_by_topnavid(self, navid):
        """该导航下的所有正在进行的活动"""
        now_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
        all_activity = self.session.query(Activity).filter_by(ACisdelete=False, TopnavId=navid)
        all_lasting_activity = all_activity.filter(now_time < Activity.ACendtime, now_time > Activity.ACstarttime).all()
        print all_lasting_activity
        return all_lasting_activity

    @close_session
    def update_view_num(self, acid):
        # cur_activity = self.session.query(Activity).filter_by(ACid=acid).first()
        # cur_activity.ACbrowsenum += 1
        # self.session.add(cur_activity)
        # self.session.commit()
        return self.session.query(Activity).filter_by(ACid=acid).update({Activity.ACbrowsenum: Activity.ACbrowsenum+1})

    @close_session
    def add_activity(self, activity):
        self.session.add(activity)

    @close_session
    def delete_activity(self, acid):
        """
        根据活动id删除
        """
        return self.session.query(Activity).filter_by(ACid=acid).update({Activity.ACisdelete: True})

    @close_session
    def stop_activity(self, acid):
        """
        手动停止活动
        """
        return self.session.query(Activity).filter_by(ACid=acid).update({Activity.ACisended: True})

    @close_session
    def get_activity_by_acid(self, acid):
        """根据id获取活动"""
        activity = self.session.query(Activity).filter_by(ACid=acid).first()
        # if not activity:
        #     raise ApiException()
        return activity

    @close_session
    def get_activity_by_prid(self, prid):
        return self.session.query(Activity).filter_by(PRid=prid, ACisdelete=False).all()

    @close_session
    def get_product_soldnum_by_acid(self, acid):
        """根据活动获取对应商品的销量"""
        cur_activity = self.session.query(Activity).filter_by(ACid=acid).first()
        if cur_activity.ACProductsSoldFakeNum:
            return cur_activity.ACProductsSoldFakeNum
        else:
            prid = cur_activity.PRid
            product = self.session.query(Product).filter_by(PRid=prid).first()
            if product:
                return product.PRsalesvolume
            else:
                print '无此商品, 销量查询无效'
                return 0

    @close_session
    def update_activity_by_acid(self, acid, activity):
        return self.session.query(Activity).filter_by(ACid=acid).update(activity)

    @close_session
    def foward_activity(self, forward):
        """转发活动"""
        self.session.add(forward)

#
# if __name__ == '__main__':
#     test = SActivity()
#     res = test.get_activity_by_acid(1)
#     import ipdb
#
#     ipdb.set_trace()
#     print(res)
