# *- coding:utf8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
from SBase import SBase, close_session
from WeiDian.models.model import ActivityLike, Activity


class SActivityLike(SBase):

    @close_session
    def get_likenum_by_acid(self, acid):
        """获得活动的点赞或虚拟数量"""
        cur_activity = self.session.query(Activity).filter_by(ACid=acid).first()
        if cur_activity.AClikeFakeNum:
            return cur_activity.AClikeFakeNum
        return self.session.query(Activity).filter_by(ACid=acid).count()

    @close_session
    def add_like(self, aclike):
        """添加喜欢数量"""
        acid = aclike.acid
        cur_activity = self.session.query(Activity).filter_by(ACid=acid).first()
        if cur_activity.AClikeFakeNum:
            cur_activity.AClikeFakeNum += 1
            self.session.add(cur_activity)
        self.session.add(aclike)

    @close_session
    def add_like(self, aclike):
        """取消喜欢"""
        acid = aclike.acid
        cur_activity = self.session.query(Activity).filter_by(ACid=acid).first()
        if cur_activity.AClikeFakeNum:
            cur_activity.AClikeFakeNum -= 1
            self.session.add(cur_activity)








if __name__ == '__main__':
    print(SActivityLike().get_likenum_by_acid(1))