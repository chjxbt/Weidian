# -*- coding:utf8 -*-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import LevelRules
sys.path.append(os.path.dirname(os.getcwd()))


class SLevelRules(SBase):

    @close_session
    def get_rule_list(self):
        """获取我的弹窗规则内容"""
        return self.session.query(LevelRules).filter_by(LRisdelete=False).order_by(LevelRules.LRcreatetime.desc()).all()
