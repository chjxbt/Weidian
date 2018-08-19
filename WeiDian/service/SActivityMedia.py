# *- coding:utf8 *-
import sys
import os
from collections import namedtuple

sys.path.append(os.path.dirname(os.getcwd()))
from SBase import SBase, close_session
from WeiDian.models.model import ActivityMedia, Activity
# media = namedtuple('media', ['ACid', 'AMmedia', 'AMsort'])


class SActivityMedia(SBase):

    @close_session
    def get_media_by_acid(self, acid):
        """获取活动中的媒体信息
        如果是视频, 返回一个单视频列表
        如果是图片, 返回图片列表"""
        cur_medias = self.session.query(ActivityMedia).filter_by(ACid=acid).order_by(ActivityMedia.AMsort)
        exists = cur_medias.first()
        if exists:
            cur_medias = cur_medias.all()
            """是有视频的活动"""
            cur_medias = filter(lambda x: x.AMimage or x.AMvideo, cur_medias)  # 过滤无效的记录
            map(lambda x: x.add('AMvideo') if x.AMvideo else x.add('AMimage', 'AMsort'), cur_medias)  # 添加转字典需要的字段
            return cur_medias
        return []
        
