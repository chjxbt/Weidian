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
        return self.session.query(BankCard).filter_by(USid=usid).first()