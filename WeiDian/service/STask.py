# *- coding:utf8 *-
import sys
import os
from datetime import datetime
from WeiDian.common.timeformat import format_for_db
from SBase import SBase, close_session
from WeiDian.models.model import Task, TaskUser
sys.path.append(os.path.dirname(os.getcwd()))

class STask(SBase):

    @close_session
    def get_task_by_level(self, level):
        return self.session.query(Task).filter(Task.TAlevel == level).all()

    @close_session
    def get_task_all(self):
        return self.session.query(Task).all()
