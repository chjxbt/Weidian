# -*- coding:utf8 -*-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import BigActivity
sys.path.append(os.path.dirname(os.getcwd()))


class SBigActivity(SBase):

    @close_session
    def get_home_banner_by_said(self):
        """获取首页轮播图"""
        return self.session.query(BigActivity).filter_by(BAposition=0, BAisdisplay=True, BAisdelete=False).\
            order_by(BigActivity.BAsort.asc()).all()

    @close_session
    def get_discover_banner_by_said(self):
        """获取发现页轮播图"""
        return self.session.query(BigActivity).filter_by(BAposition=1, BAisdisplay=True, BAisdelete=False).\
            order_by(BigActivity.BAsort.asc()).all()

    @close_session
    def get_bigactivity_banner_by_baid(self, baid):
        """获取专题页题图"""
        return self.session.query(BigActivity.BAimage).filter_by(BAid=baid).first()
