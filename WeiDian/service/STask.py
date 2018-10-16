# *- coding:utf8 *-
import sys
import os
from SBase import SBase, close_session


sys.path.append(os.path.dirname(os.getcwd()))


from WeiDian.models.model import Task, TaskUser, TaskLevel


class STask(SBase):

    @close_session
    def get_tasklevel_by_level(self, level):
        return self.session.query(TaskLevel).filter(TaskLevel.TAlevel == level, TaskLevel.TLisdelete == 0).order_by(
            TaskLevel.TAlevel.desc()).first()

    @close_session
    def get_task_all(self):
        return self.session.query(Task).order_by(Task.TAcreatetime).all()

    @close_session
    def get_user_task_by_userid(self, usid):
        return self.session.query(TaskUser).filter(TaskUser.USid == usid).order_by(TaskUser.TUcreatetime).all()

    @close_session
    def get_task_by_taid(self, taid):
        return self.session.query(Task).filter(Task.TAid == taid).first()

    @close_session
    def get_user_task_by_id(self, tuid):
        return self.session.query(TaskUser).filter(TaskUser.TUid == tuid).first()

    @close_session
    def get_todo_user_task_by_user_id(self, usid):
        return self.session.query(TaskUser).filter(TaskUser.USid == usid, TaskUser.TUstatus == 0).all()

    @close_session
    def get_task_level_by_tlid(self, tlid):
        return self.session.query(TaskLevel).filter(TaskLevel.TLid == tlid, TaskLevel.TLisdelete == 0).first()

    @close_session
    def get_task_by_tlid(self, tlid):
        return self.session.query(Task).filter(Task.TLid == tlid).order_by(Task.TAcreatetime).all()

    @close_session
    def get_task_level_all(self):
        return self.session.query(TaskLevel).filter(TaskLevel.TLisdelete == 0).order_by(TaskLevel.TAlevel).all()

    @close_session
    def get_all_user_task(self):
        return self.session.query(TaskUser).order_by(TaskUser.TUcreatetime).all()

    # @close_session
    # def del_task_level(self, tasklevel):
    #     self.session.query(TaskLevel).filter(TaskLevel.TAlevel == tasklevel).update({"TLisdelete": True})

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
    def update_task_level(self, tlid, tasklevel):
        return self.session.query(TaskLevel).filter(TaskLevel.TLid == tlid).update(tasklevel)

    @close_session
    def update_task_by_tlid(self, tlid, task):
        return self.session.query(Task).filter(Task.TLid == tlid).update(task)

if __name__ == '__main__':
    usid = '980513c6-ce8e-11e8-bdc4-00163e0cc024'
    sb = SBase()
    from WeiDian.models import model

    sb.session.query(model.ActivityComment).filter(model.ActivityComment.USid == usid).delete()
    sb.session.query(model.ActivityLike).filter(model.ActivityLike.USid == usid).delete()
    sb.session.query(model.ActivityFoward).filter(model.ActivityFoward.USid == usid).delete()
    sb.session.query(model.ProductLike).filter(model.ProductLike.USid == usid).delete()
    sb.session.query(model.RecommendLike).filter(model.RecommendLike.USid == usid).delete()
    sb.session.query(model.ShoppingCart).filter(model.ShoppingCart.USid == usid).delete()
    sb.session.query(model.OrderInfo).filter(model.OrderInfo.USid == usid).delete()
    sb.session.query(model.User).filter(model.User.USid == usid).delete()
    sb.session.query(model.UserLoginTime).filter(model.UserLoginTime.USid == usid).delete()
    sb.session.query(model.Complain).filter(model.Complain.USid == usid).delete()
    sb.session.query(model.TaskUser).filter(model.TaskUser.USid == usid).delete()
    sb.session.query(model.UserRaward).filter(model.UserRaward.USid == usid).delete()
    sb.session.query(model.BankCard).filter(model.BankCard.USid == usid).delete()
    sb.session.query(model.UserAddress).filter(model.UserAddress.USid == usid).delete()
    sb.session.query(model.PartnerSellOrinviteMount).filter(model.PartnerSellOrinviteMount.USid == usid).delete()
    sb.session.commit()
