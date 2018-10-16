# -*- coding:utf8 -*-
import sys
import os

from WeiDian import logger
from flask import request
import uuid
from WeiDian.common.TransformToList import dict_add_models
from WeiDian.common.import_status import import_status
from WeiDian.common.params_require import parameter_required
from WeiDian.common.token_required import verify_token_decorator, is_tourist
from WeiDian.config.response import TOKEN_ERROR, SYSTEM_ERROR, NOT_FOUND
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
        args = request.args.to_dict()
        logger.debug("get like list args is %s", args)
        parameter_required("page_size", "page_num")
        page_num = args.get("page_num")
        page_size = args.get("page_size")
        page_num = 1 if not page_num else int(page_num)
        page_size = 5 if not page_size else int(page_size)
        try:
            productlike_list = self.sproductlike.get_productlike_list_by_usid(request.user.id, page_num, page_size)
            if not productlike_list:
                raise NOT_FOUND(u'用户无收藏信息')
            logger.info("get product like list success")
            map(self.fill_productinfo, productlike_list)
            # 获取转发数
            from WeiDian.service.SActivity import SActivity
            from WeiDian.service.SActivityFoward import SActivityFoward
            total_forward = 0
            for prlike in productlike_list:
                forward_act = SActivity().get_acid_by_filterid({'AClinkvalue': prlike.PRid,
                                                                'ACSkipType': 2,
                                                                })
                for act in forward_act:
                    forward_num = SActivityFoward().get_fowardnum_by_acid(act.ACid)
                    total_forward = total_forward + forward_num

                prlike.forwardnum = total_forward
                prlike.add("forwardnum")
            prlikecount = self.sproductlike.get_prlike_count_by_usid(request.user.id)
            data = import_status("get_product_like_success", "OK")
            data["count"] = prlikecount
            data["data"] = productlike_list
            return data
        except Exception as e:
            logger.exception("get product like error")
            raise SYSTEM_ERROR(u'收藏信息不存在')

    @verify_token_decorator
    def batch_delete_prlike(self):
        if is_tourist():
            return TOKEN_ERROR(u'未登录')
        data = request.json
        plid_list = data.get("plid").split(',') if data and 'plid' in data else None
        logger.info("batch del prlike data is %s", data)
        print plid_list
        try:
            self.sproductlike.batch_delete_prlike(plid_list)
            response = import_status('delete_activity_success', 'OK')
            response['data'] = {
                "plidlist": plid_list
            }
            return response
        except:
            logger.exception("batch del prlike error")
            return SYSTEM_ERROR

    def fill_productinfo(self, prlike):
        prid = prlike.PRid
        prlike.productinfo = self.sproduct.get_product_by_prid(prid)
        if not prlike.productinfo:
            raise SYSTEM_ERROR(u'无此收藏商品')
        prlike.productinfo.fields = ['PRmainpic', 'PRsalestatus']
        prlike.add('productinfo')
        return prlike
