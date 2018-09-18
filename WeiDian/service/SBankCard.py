# -*- coding:utf8 -*-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import BankCard, Province, City, Area

sys.path.append(os.path.dirname(os.getcwd()))


class SBankCard(SBase):

    @close_session
    def get_bankcard_by_usid(self, usid):
        """获取绑定银行卡信息"""
        return self.session.query(BankCard).filter_by(USid=usid).first()

    @close_session
    def get_bankcard_count(self, usid):
        return self.session.query(BankCard).filter_by(USid=usid).count()

    @close_session
    def get_province(self):
        """获取所有省份"""
        return self.session.query(Province).all()

    @close_session
    def get_citylist_by_provinceid(self, province_id):
        """根据省份编号获取城市列表"""
        return self.session.query(City).filter_by(province_id=province_id).all()

    @close_session
    def get_arealist_by_cityid(self, cityid):
        return self.session.query(Area).filter_by(city_id=cityid).all()