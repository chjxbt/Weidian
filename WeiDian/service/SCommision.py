# -*- coding: utf-8 -*-
import datetime
from WeiDian.models.model import UserCommisionPriview, UserCommision, UserCommisionFlow, TeamCommision
from WeiDian.service.SBase import SBase, close_session


class SCommision(SBase):

    @close_session
    def get_commision_preview_by_usid(self, usid):
        """预估佣金"""
        return self.session.query(UserCommisionPriview).filter(
            UserCommisionPriview.USid == usid,
            UserCommisionPriview.UCPstatus == 0
        ).all()

    @close_session
    def get_usercommsion_by_usid(self, usid):
        """个人到帐佣金"""
        return self.session.query(UserCommision).filter(
            UserCommision.USid == usid
        ).first()

    @close_session
    def get_usercommsion_flow_filter(self, args):
        """佣金流水记录"""
        return self.session.query(UserCommisionFlow).filter_by(**args).all()

    @close_session
    def get_teamcommision_by_usid(self, usid, args=None):
        return self.session.query(TeamCommision).filter(TeamCommision.USid == usid).filter(*args).all()