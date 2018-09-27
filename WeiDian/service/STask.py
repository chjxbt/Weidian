# *- coding:utf8 *-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import Task, TaskUser, TaskLevel
sys.path.append(os.path.dirname(os.getcwd()))


class STask(SBase):

    @close_session
    def get_tasklevel_by_level(self, level):
        return self.session.query(TaskLevel).filter(TaskLevel.TAlevel == level).first()

    @close_session
    def get_task_all(self):
        return self.session.query(Task).all()

    @close_session
    def get_user_task_by_userid(self, usid):
        return self.session.query(TaskUser).filter(TaskUser.USid == usid).all()

    @close_session
    def get_task_by_taid(self, taid):
        return self.session.query(Task).filter(Task.TAid == taid).first()

    @close_session
    def get_user_task_by_id(self, tuid):
        return self.session.query(TaskUser).filter(TaskUser.TUid == tuid).first()

    @close_session
    def update_task(self, taid, task):
        return self.session.query(Task).filter(Task.TAid == taid).update(task)

    @close_session
    def update_user_task(self, tuid, user_task):
        return self.session.query(TaskUser).filter(TaskUser.TUid == tuid).update(user_task)

    @close_session
    def update_user_tasks(self, usid, user_task):
        return self.session.query(TaskUser).filter(TaskUser.USid == usid).update(user_task)

    @close_session
    def get_todo_user_task_by_user_id(self, usid):
        return self.session.query(TaskUser).filter(TaskUser.USid == usid, TaskUser.TUstatus == 0).all()

    @close_session
    def update_task_level(self, tlid, tasklevel):
        return self.session.query(TaskLevel).filter(TaskLevel.TLid == tlid).update(tasklevel)

    @close_session
    def get_task_level_by_tlid(self, tlid):
        return self.session.query(TaskLevel).filter(TaskLevel.TLid == tlid).first()
