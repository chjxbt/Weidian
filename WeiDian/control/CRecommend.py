# *- coding:utf8 *-
import sys
import os
from datetime import datetime

from WeiDian.common.import_status import import_status
from WeiDian.common.timeformat import format_for_db
from WeiDian.common.token_required import verify_token_decorator, is_partner
from WeiDian.config.response import AUTHORITY_ERROR
from WeiDian.control.BaseControl import BaseProductControl
from WeiDian.service.SProduct import SProduct
from flask import request

sys.path.append(os.path.dirname(os.getcwd()))

class CRecommend(BaseProductControl):
    def __init__(self):
        from WeiDian.service.SRecommend import SRecommend
        self.srecommend = SRecommend()
        self.sproduct = SProduct()

    @verify_token_decorator
    def get_all(self):
        if not is_partner():
            return AUTHORITY_ERROR
        print '是合伙人'
        args = request.args.to_dict()
        recommend_list = self.srecommend.get_recommend()
        lasting = args.get('lasting', 'true')  # 是否正在展示
        if lasting == 'true':
            now_time = datetime.strftime(datetime.now(), format_for_db)
            recommend_list = filter(lambda re: re.REstarttime < now_time < re.REendtime, recommend_list)
        map(self.fill_recommend_nums, recommend_list)
        map(self.fill_product, recommend_list)
        data = import_status('get_recommend_success', 'OK')
        data['data'] = recommend_list
        return data


    # if is_tourist() or is_ordirnaryuser():
    #     print '是游客或者普通用户'
    #     product = self.trans_product_for_fans(product)







