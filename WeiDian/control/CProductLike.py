# -*- coding:utf8 -*-
import sys
import os
from flask import request
import uuid
from WeiDian.common.TransformToList import dict_add_models
from WeiDian.common.import_status import import_status
from WeiDian.common.params_require import parameter_required
from WeiDian.common.token_required import verify_token_decorator, is_tourist
from WeiDian.config.response import TOKEN_ERROR
from WeiDian.service.SProduct import SProduct
from WeiDian.service.SProductLike import SProductLike
sys.path.append(os.path.dirname(os.getcwd()))


class CProductLike():
    def __init__(self):
        self.sproductlike = SProductLike()
        self.sproduct = SProduct()

    @verify_token_decorator
    def add_like(self):
        """添加(删除)喜欢(收藏)"""
        if is_tourist():
            return TOKEN_ERROR()
        json_data = parameter_required('prid')
        prid = json_data.get('prid')
        # 该用户是否已经收藏了此商品
        already_like = self.sproductlike.get_productlike_by_usidprid(
            request.user.id, prid)
        if not already_like:
            pl_dict = dict(
                plid=str(uuid.uuid4()),
                usid=request.user.id,
                prid=prid
            )
            dict_add_models('ProductLike', pl_dict)
            self.sproduct.update_like_num(prid)
            data = import_status('add_productlike_success', 'OK')
        else:
            # 删除
            self.sproductlike.del_productlike_usidprid(request.user.id, prid)
            self.sproduct.update_like_num(prid, -1)
            data = import_status('cancel_product_like_success', 'OK')
        plid = already_like.PLid if already_like else pl_dict['plid']
        data['data'] = {
            'plid': plid
        }
        return data

    @verify_token_decorator
    def get_like_list(self):
        """获取用户的收藏列表"""
        if is_tourist():
            return TOKEN_ERROR(u'未登录')
        print '已登录'
        productlike_list = self.sproductlike.get_productlike_list_by_usid(request.user.id)
        map(self.fill_product, productlike_list)
        data = import_status("get_product_like_success", "OK")
        data["data"] = productlike_list
        return data

    def fill_product(self, prlike):
        prid = prlike.PRid
        prlike.productinfo = self.sproduct.get_product_by_prid(prid)
        prlike.productinfo.fields = ['PRmainpic']
        prlike.add('productinfo')
        return prlike