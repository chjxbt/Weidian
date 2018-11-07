# -*- coding: utf-8 -*-
import datetime
from WeiDian.models.model import UserCommisionPriview, UserCommision, UserCommisionFlow, TeamCommision, CommisionToCash
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
    def get_usercommsion_flow_filter(self, args, time_start=None, time_end=None):
        """佣金流水记录"""
        return self.session.query(UserCommisionFlow).filter_by(**args).gt(
            UserCommisionFlow.UCFtime == time_start).lt(UserCommisionFlow.UCFtime == time_end).all()

    @close_session
    def get_teamcommision_by_usid(self, usid):
        """团队佣金"""
        return self.session.query(TeamCommision).filter(TeamCommision.USid == usid).all()

    @close_session
    def get_extractcommision_by_filter(self, ecfilter):
        """正提取佣金"""
        return self.session.query(CommisionToCash).filter_by(**ecfilter).all()
