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
