# -*- coding:utf8 -*-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import UserAddress, Province, City, Area
sys.path.append(os.path.dirname(os.getcwd()))


class SUserAddress(SBase):

    @close_session
    def get_default_address_by_usid(self, usid):
        """获取默认地址"""
        return self.session.query(UserAddress).filter_by(USid=usid, UAdefault=True, UAisdelete=False).first()

    @close_session
    def get_first_no_default_address(self, usid):
        return (self.session.query(UserAddress).filter_by(USid=usid, UAisdelete=False, UAdefault=False)
                .order_by(UserAddress.UAcreatetime.desc()).first())

    @close_session
    def get_address_list_by_usid(self, usid):
        """获取所有地址"""
        return self.session.query(UserAddress).filter_by(USid=usid, UAisdelete=False).order_by(UserAddress.UAcreatetime.desc()).all()

    @close_session
    def change_default_address_status(self, uaid, status):
        """改变地址默认状态"""
        return self.session.query(UserAddress).filter_by(UAid=uaid).update(status)

    @close_session
    def update_address(self, uaid, address):
        """通过uaid获取地址"""
        return self.session.query(UserAddress).filter_by(UAid=uaid).update(address)

    @close_session
    def delete_address(self, uaid):
        """删除地址"""
        return self.session.query(UserAddress).filter_by(UAid=uaid).update({"UAisdelete": True})


    @close_session
    def get_province(self):
        """获取所有省份"""
        return self.session.query(Province).all()

    @close_session
    def get_citylist_by_provinceid(self, provinceid):
        """根据省份编号获取城市列表"""
        return self.session.query(City).filter_by(provinceid=provinceid).all()

    @close_session
    def get_arealist_by_cityid(self, cityid):
        """通过城市编号获取区县列表"""
        return self.session.query(Area).filter_by(cityid=cityid).all()

    @close_session
    def get_address_by_uaid(self, uaid):
        return self.session.query(UserAddress).filter_by(UAid=uaid, UAisdelete=False).first()

    @close_session
    def get_one_or_default_address(self, uafilter):
        return self.session.query(UserAddress).filter_by(**uafilter).first()

    @close_session
    def get_addressinfo_by_areaid(self, areaid):
        return self.session.query(Area, City, Province).filter(Area.cityid == City.cityid, City.provinceid == Province.provinceid).filter(Area.areaid == areaid).all()