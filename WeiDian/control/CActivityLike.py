# -*- coding:utf8 -*-
import sys
import os
import uuid

from WeiDian import logger
from WeiDian.common.TransformToList import dict_add_models
from WeiDian.common.import_status import import_status
from WeiDian.common.params_require import parameter_required
from WeiDian.common.token_required import verify_token_decorator, is_tourist
from WeiDian.config.response import AUTHORITY_ERROR
from WeiDian.service.SActivity import SActivity
from WeiDian.service.SActivityLike import SActivityLike
from WeiDian.service.SProduct import SProduct
from WeiDian.service.SProductLike import SProductLike
from flask import request
sys.path.append(os.path.dirname(os.getcwd()))


class CActivityLike():
    def __init__(self):
        self.sactivity = SActivity()
        self.salike = SActivityLike()
        self.sproduct = SProduct()
        self.sproductlike = SProductLike()

    @verify_token_decorator
    def like_or_cancel(self):
        if is_tourist():
            raise AUTHORITY_ERROR(u"未登录")
        print (request.user.USname.encode('utf8'))
        json_data = request.json
        logger.debug("act like data is %s", json_data)
        parameter_required('acid')
        acid = json_data.get('acid')
        usid = request.user.id
        already_like = self.salike.is_like(usid, acid)
        activity = self.sactivity.get_activity_by_acid(acid)
        if not already_like:
            logger.info("this is not already_like to add activitylike")
            al_dict = {
                'ALid': str(uuid.uuid4()),
                'USid': request.user.id,
                'ACid': acid
            }
            self.salike.add_model('ActivityLike', **al_dict)
            self.salike.add_like_by_acid(acid)
            data = import_status('add_activity_like_success', 'OK')
            # data = import_status('add_productlike_success', 'OK')
            if activity.ACSkipType == 2 and activity.AClinkvalue:
                logger.info("this is add productlike")
                pl_dict = {
                    'PLid': str(uuid.uuid4()),
                    'USid': request.user.id,
                    'PRid': activity.AClinkvalue
                }
                self.sproductlike.add_model('ProductLike', **pl_dict)
                self.sproduct.update_like_num(activity.AClinkvalue)
                data = import_status('add_ac_pr_like_success', 'OK')
        # elif not already_like:
            # al_dict = dict(
            #     alid=str(uuid.uuid4()),
            #     usid=request.user.id,
            #     acid=acid
            # )
            # dict_add_models('ActivityLike', al_dict)
            # self.salike.add_like_by_acid(acid)
            # data = import_status('add_activity_like_success', 'OK')
            # # data = import_status('add_productlike_success', 'OK')

        # elif already_like and not activity.PRid:
        #     self.salike.del_like(request.user.id, acid)
        #     self.salike.cancel_like_by_acid(acid)
        #     data = import_status('cancel_activity_like_success', 'OK')
        else:
            logger.info("this is already like activity to cancel like")
            self.salike.del_like(usid, acid)
            product_like = self.sproductlike.get_product_is_like_by_prid(usid, activity.AClinkvalue)
            logger.info("this is already like product to cancel like")
            if product_like:
                self.sproductlike.del_productlike_usidprid(usid, activity.AClinkvalue)
            self.salike.cancel_like_by_acid(acid)
            self.sproduct.update_like_num(activity.AClinkvalue, -1)
            data = import_status('cancel_activity_like_success', 'OK')
        alid = already_like.ALid if already_like else al_dict['ALid']
        data['data'] = {'alid': alid}
        return data
