# -*- coding:utf8 -*-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import UserAddress
sys.path.append(os.path.dirname(os.getcwd()))


class SUserAddress(SBase):

    @close_session
    def get_default_address_by_usid(self, usid):
        """获取默认地址"""
        return self.session.query(UserAddress).filter_by(USid=usid, UAdefault=True, UAisdelete=False).first()

    @close_session
    def get_address_list_by_usid(self, usid):
        """获取所有地址"""
        return self.session.query(UserAddress).filter_by(USid=usid, UAisdelete=False).order_by(UserAddress.UAceratetime.desc()).all()

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
        return self.session.query(UserAddress).filter_by(UAid=uaid).update({"UAisdelete":True})