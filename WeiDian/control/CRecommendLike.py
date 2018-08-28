# *- coding:utf8 *-
import sys
import os
import uuid
from WeiDian.common.TransformToList import dict_add_models
from WeiDian.common.import_status import import_status
from WeiDian.common.params_require import parameter_required
from WeiDian.common.token_required import verify_token_decorator, is_partner
from WeiDian.config.response import AUTHORITY_ERROR
from WeiDian.service.SRecommend import SRecommend
from WeiDian.service.SRecommendLike import SRecommendLike
from flask import request
sys.path.append(os.path.dirname(os.getcwd()))


class CRecommendLike():
    def __init__(self):
        self.srecommendlike = SRecommendLike()
        self.srecommend = SRecommend()

    @verify_token_decorator
    def like_or_cancel(self):
        if not is_partner():
            return AUTHORITY_ERROR
        print '是合伙人'
        json_data = parameter_required('reid')
        reid = json_data.get('reid')
        already_like = self.srecommendlike.get_recommend_like_by_usidreid(request.user.id, reid)
        recommend = self.srecommend.get_recommend_by_reid(reid)
        if not already_like:
            rl_dict = dict(
                rlid=str(uuid.uuid4()),
                usid=request.user.id,
                reid=reid
            )
            dict_add_models('RecommendLike', rl_dict)
            rlid = already_like.RLid if already_like else rl_dict['rlid']
            self.srecommend.add_like_num(reid)  # 数量更改
            data = import_status('add_recommend_like_success', 'OK')
            data['data'] = {'rlid': rlid}
            return data
        else:
            # 删除点赞
            self.srecommendlike.del_like(request.user.id, reid)
            self.srecommend.del_like_num(reid)
            response_make_like = import_status('cancel_recommend_like_success', 'OK')
            response_make_like['data'] = {'reid': reid}
            return response_make_like
