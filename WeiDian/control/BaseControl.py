# *- coding:utf8 *   -
class BaseControl():

    def get_one_activity(self):
        pass

    def fill_detail(self, act):
        """填充一些关联活动的信息"""
        acid = act.ACid
        act.suuser = self.ssuperuser.get_one_super_by_suid(act.SUid)  # 超级用户
        act.media = self.smedia.get_media_by_acid(acid)  # 图片或视频
        act.tags = self.stags.get_show_tags_by_acid(acid)  # 右上角tag
        act.foward = self.foward.get_fowardnum_by_acid(acid)  # 转发数
        act.likenum = self.salike.get_likenum_by_acid(acid)  # 喜欢数
        act.soldnum = self.sactivity.get_product_soldnum_by_acid(acid)  # 销量
        act.add('suuser', 'media', 'tags', 'foward', 'likenum', 'soldnum')
        return act

    def fill_suser(self, obj):
        """给对象添加一个用户字段"""
        obj.suuser = self.suser.get_user_by_user_id(obj.USid)  # 对象的用户
        obj.add('user')
        return obj

    def fill_comment(self, act):
        """给活动对象附加一个评论属性"""
        acid = act.ACid
        act.comment = self.sacomment.get_comment_by_activity_id(acid)
        act.add('comment')
        map(self.fill_comment_apply_for, act.comment)
        return act

    def fill_comment_apply_for(self, comment):
        """"如果既是评论又是回复则添加一个'所回复用户'属性"""
        acoid = comment.ACOid
        if not comment.ACOparentid:
            return comment  # 如果ACOid没有值, 说明这不是回复的内容
        comment.parent_apply_user = self.sacomment.get_apply_for_by_acoid(acoid)
        comment.add('parent_apply_user')
        return comment

