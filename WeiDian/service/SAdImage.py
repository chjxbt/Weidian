# -*- coding:utf8 -*-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import AdImage
sys.path.append(os.path.dirname(os.getcwd()))

class SAdImage(SBase):

    @close_session
    def get_myimage(self):
        """获取我的底部图片"""
        return self.session.query(AdImage).filter_by(AItype=1, AIisdelete=False).order_by(AdImage.AIcreatetime.desc()).all()

    @close_session
    def get_image_by_aitype(self, aitype):
        """通过图片类型获取数据"""
        return self.session.query(AdImage).filter(AdImage.AItype == aitype).order_by(AdImage.AIcreatetime.desc()).all()

    @close_session
    def update_image(self, aiid, adimage):
        return self.session.query(AdImage).filter(AdImage.AIid == aiid).update(adimage)