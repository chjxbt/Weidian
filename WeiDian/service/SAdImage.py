# -*- coding:utf8 -*-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import AdImage
sys.path.append(os.path.dirname(os.getcwd()))

class SAdImage(SBase):

    @close_session
    def get_image_by_aiid(self, aiid):
        """获取图片"""
        return self.session.query(AdImage).filter_by(AIid=aiid, AIisdelete=False).first()
