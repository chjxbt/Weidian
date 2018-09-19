# -*- coding:utf8 -*-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import BankCard

sys.path.append(os.path.dirname(os.getcwd()))


class SBankCard(SBase):

    @close_session
    def get_bankcard_by_usid(self, usid):
        """获取绑定银行卡信息"""
        return self.session.query(BankCard).filter_by(USid=usid, BCisdelete=False).first()

    @close_session
    def get_bankcard_count(self, usid):
        """获取绑定银行卡数量"""
        return self.session.query(BankCard).filter_by(USid=usid, BCisdelete=False).count()

    @close_session
    def update_bankcard(self, bcid, bankcardinfo):
        """修改银行卡信息"""
        return self.session.query(BankCard).filter_by(BCid=bcid).update(bankcardinfo)

    @close_session
    def del_bankcard(self, bcid, usid):
        """解除银行卡绑定"""
        return self.session.query(BankCard).filter_by(BCid=bcid, USid=usid).update({'BCisdelete': True})
