# *- coding:utf8 *-
class BaseActivityControl():

    def get_one_activity(self):
        pass

    def fill_detail(self, act):
        """填充一些关联活动的信息"""
        acid = act.ACid
        act.user = self.suser.get_user_by_user_id(act.USid)
        act.media= self.smedia.get_media_by_acid(acid)  # 图片或视频
        act.tags = self.stags.get_show_tags_by_acid(acid)  # 右上角tag
        act.foward = self.foward.get_fowardnum_by_acid(acid)  # 转发数
        act.likenum = self.salike.get_likenum_by_acid(acid)  # 喜欢数
        act.soldnum = self.sactivity.get_product_soldnum_by_acid(acid)  # 销量
        act.add('user', 'media', 'tags', 'foward', 'likenum', 'soldnum')
        return act

    def fill_comment(self, act):
        acid = act.ACid
        act.comment= self.sacomment.get_comment_by_activity_id(acid)
        return act

