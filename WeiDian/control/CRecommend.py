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

from WeiDian.service.SSuperUser import SSuperUser

sys.path.append(os.path.dirname(os.getcwd()))


class CRecommend(BaseProductControl):
    
    def __init__(self):
        from WeiDian.service.SRecommend import SRecommend
        self.srecommend = SRecommend()
        self.sproduct = SProduct()
        self.ssuperuser = SSuperUser()

    @verify_token_decorator
    def get_list(self):
        args = request.args.to_dict()
        if not is_partner():
            return AUTHORITY_ERROR
        print '是合伙人'
        recommend = self.srecommend.get_recommend_list()
        lasting = args.get('lasting', 'true')  # 是否正在展示
        if lasting == 'true':
            now_time = datetime.strftime(datetime.now(), format_for_db)
            recommend = filter(lambda re: re.REstarttime < now_time < re.REendtime, recommend)
        map(self.fill_product, recommend)
        map(self.fill_recommend_nums, recommend)
        map(self.fill_super, recommend)
        data = import_status('get_recommend_success', 'OK')
        data['data'] = recommend
        return data


    # if is_tourist() or is_ordirnaryuser():
    #     print '是游客或者普通用户'
    #     product = self.trans_product_for_fans(product)
