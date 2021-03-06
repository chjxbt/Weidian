# *- coding:utf8 *-
import sys
import os
from datetime import datetime

from WeiDian.common.divide import Partner
from SBase import SBase, close_session
from WeiDian.common.timeformat import format_for_db
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
    def get_activity_count(self, acfilter):
        settings = Partner()
        skiptype = settings.get_item('skip', 'skip_type')
        acfilter.add(Activity.ACisdelete == False)
        acfilter.add(Activity.ACSkipType == skiptype)

        return self.session.query(Activity).filter(*acfilter).count()

    @close_session
    def get_top_activity(self, tnid):
        """获取置顶推文"""
        return self.session.query(Activity).filter_by(ACisdelete=False, TopnavId=tnid, ACistop=True).first()

    @close_session
    def change_top_act_status(self, acid, status):
        return self.session.query(Activity).filter_by(ACid=acid).update(status)

    @close_session
    def get_activity_by_topnavid(self, tnid=None, page_num=None, page_size=None, skiptype=None, acid=None, suid=None, now_time=None):
        """根据导航的id获取活动"""
        return self.session.query(Activity).filter(Activity.ACisdelete == False). \
            filter_without_none(Activity.ACSkipType == skiptype, Activity.TopnavId == tnid,
                                Activity.ACid == acid, Activity.SUid == suid).\
            gt(Activity.ACendtime == now_time).lt(Activity.ACstarttime == now_time).\
            order_by(Activity.ACistop.desc(), Activity.ACcreatetime.desc()).all_with_page(page_num, page_size)

    @close_session
    def get_activity_by_suid(self, suid, page_num, page_size):
        acvitity_list = self.session.query(Activity).filter_by(ACisdelete=False, SUid=suid).order_by(Activity.ACcreatetime.desc()).offset(page_size * (int(page_num) - 1)).limit(page_size).all()
        return acvitity_list

    # @close_session
    # def get_lasting_activity_by_topnavid(self, navid):
    #     """该导航下的所有正在进行的活动"""
    #     now_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
    #     all_activity = self.session.query(Activity).filter_by(ACisdelete=False, TopnavId=navid)
    #     all_lasting_activity = all_activity.filter(now_time < Activity.ACendtime, now_time > Activity.ACstarttime).all()
    #     print all_lasting_activity
    #     return all_lasting_activity

    @close_session
    def update_view_num(self, acid):
        return self.session.query(Activity).filter_by(ACid=acid).update({Activity.ACbrowsenum: Activity.ACbrowsenum+1})
        # cur_activity = self.session.query(Activity).filter_by(ACid=acid).first()
        # cur_activity.ACbrowsenum += 1
        # self.session.add(cur_activity)
        # self.session.commit()

    @close_session
    def update_forward_fakenum(self, acid):
        return self.session.query(Activity).filter(Activity.ACid == acid).update({Activity.ACforwardFakenum: Activity.ACforwardFakenum + 1})

    @close_session
    def delete_activity(self, acid):
        """删除活动"""
        return self.session.query(Activity).filter_by(ACid=acid).update({Activity.ACisdelete: True})

    @close_session
    def stop_activity(self, acid):
        """手动停止活动"""
        return self.session.query(Activity).filter_by(ACid=acid).update({Activity.ACisended: True})

    @close_session
    def get_acid_by_filterid(self, filterid):
        return self.session.query(Activity).filter_by(**filterid).all()

    @close_session
    def get_activity_by_acid(self, acid):
        """根据id获取活动"""
        return self.session.query(Activity).filter_by(ACid=acid, ACisdelete=False).first()
        # if not activity:
        #     raise ApiException()

    @close_session
    def get_activity_by_prid(self, prid):
        return self.session.query(Activity).filter_by(ACSkipType=2, AClinkvalue=prid, ACisdelete=False).all()

    @close_session
    def get_one_act_by_prid(self, prid):
        return self.session.query(Activity.ACtext).filter_by(ACSkipType=2, AClinkvalue=prid, ACisdelete=False).order_by(Activity.ACcreatetime.desc()).first()

    @close_session
    def get_activity_list_by_actext(self, actext, tnid):
        """根据actext获取"""
        return self.session.query(Activity).filter(Activity.ACtext.like("%{0}%".format(actext)), Activity.TopnavId == tnid, Activity.ACisdelete == False).all()

    @close_session
    def get_product_soldnum_by_acid(self, acid):
        """根据活动获取对应商品的销量"""
        cur_activity = self.session.query(Activity).filter_by(ACid=acid).first()
        if cur_activity.ACProductsSoldFakeNum:
            return cur_activity.ACProductsSoldFakeNum
        else:
            prid = cur_activity.AClinkvalue
            product = self.session.query(Product).filter_by(PRid=prid).first()
            if product:
                if product.PRsalefakenum:
                    return product.PRsalefakenum
                else:
                    return product.PRsalesvolume
            else:
                print '无此商品, 销量查询无效'
                return 0

    @close_session
    def update_activity_by_acid(self, acid, activity):
        """更新活动"""
        return self.session.query(Activity).filter_by(ACid=acid).update(activity)

    @close_session
    def get_bigactivity_by_baid(self, baid, page_num, page_size):
        """获取专题页内容"""
        return self.session.query(Activity).filter_by(BAid=baid, ACSkipType=2, ACisdelete=False).order_by(Activity.ACcreatetime.desc()).offset(page_size * (page_num - 1)).limit(page_size).all()

    @close_session
    def get_bigactivity_count_by_baid(self, baid):
        return self.session.query(Activity).filter_by(AClinkvalue=baid, ACSkipType=2, ACisdelete=False).count()

    @close_session
    def get_activity_by_filter(self, acfilter, tnid):
        from sqlalchemy import or_
        return self.session.query(Activity).filter(or_(*acfilter), Activity.TopnavId == tnid).order_by(Activity.ACistop.desc(), Activity.ACcreatetime.desc()).all()
#
# if __name__ == '__main__':
#     test = SActivity()
#     res = test.get_activity_by_acid(1)
#     import ipdb
#
#     ipdb.set_trace()
#     print(res)
