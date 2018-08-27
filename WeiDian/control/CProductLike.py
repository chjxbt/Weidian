# *- coding:utf8 *-
from flask import request
import uuid
from WeiDian.common.TransformToList import dict_add_models
from WeiDian.common.import_status import import_status
from WeiDian.common.params_require import parameter_required
from WeiDian.common.token_required import verify_token_decorator, is_tourist
from WeiDian.config.response import TOKEN_ERROR
from WeiDian.service.SProduct import SProduct
from WeiDian.service.SProductLike import SProductLike


class CProductLike():
    def __init__(self):
        self.sproductlike = SProductLike()
        self.sproduct = SProduct()

    @verify_token_decorator
    def add_like(self):
        """添加喜欢(收藏)"""
        if is_tourist():
            return TOKEN_ERROR()
        json_data = parameter_required('prid')
        prid = json_data.get('prid')
        already_like = self.sproductlike.get_productlike_by_usidprid(
            request.user.id, prid)
        # 该用户是否已经收藏了此商品
        if not already_like:
            pl_dict = dict(
                plid=str(uuid.uuid4()),
                usid=request.user.id,
                prid=prid
            )
            dict_add_models('ProductLike', pl_dict)
        plid = already_like.PLid if already_like else pl_dict['plid']
        data = import_status('add_productlike_success', 'OK')
        data['data'] = {
            'plid': plid
        }
        return data

    @verify_token_decorator
    def get_like_list(self):
        """获取用户的收藏列表"""
        if is_tourist():
            return TOKEN_ERROR()
        productlike_list = self.sproductlike.get_productlike_list_by_usid(request.user.id)
        pass
