# *- coding:utf8 *-
import uuid
import random
from datetime import datetime

from flask import request

from WeiDian.common.timeformat import format_for_db
from WeiDian.common.token_required import verify_token_decorator
from WeiDian.common.import_status import import_status
from WeiDian.service.SOrder import SOrder
from WeiDian.service.SProductSkuKey import SProductSkuKey
from WeiDian.config.response import PARAMS_MISS, SYSTEM_ERROR, AUTHORITY_ERROR, TOKEN_ERROR
from WeiDian.common.token_required import is_tourist



class COrder():
    def __init__(self):
        self.sorder = SOrder()
        self.sproductskukey = SProductSkuKey()

    @verify_token_decorator
    def add_one(self):
        if is_tourist():
            return TOKEN_ERROR
        data = request.json
        if not data:
            return PARAMS_MISS
        required = ['oiaddress', 'oisingername', 'oisingerphone', 'sku']
        missed = filter(lambda x: x not in data, required)
        if missed:
            return PARAMS_MISS('参数缺失' + '.'.join(missed))
        order_dict = dict(
            oiid=str(uuid.uuid4()),
            oisn=datetime.strftime(datetime.now(), format_for_db) + str(random.randint(10000, 100000)),
            oileavetext=data.get('oileavetext') or '',
        )
        sku = data.get('sku')
        self.fix_orderproduct_info(sku, order_dict['oiid'])

    def fix_orderproduct_info(self, sku, oiid):
        """调整参数以可以持久化到orderproductinfo表"""
        pskid = sku.get('pskid')
        productskukey = self.sproductskukey.get_psk_by_pskid(pskid)
        prid = product.PRid
        orderprductinfo_dict = dict(
                opiid=str(uuid.uuid4()),
                oiid=oiid,
                prid=prid,
                PSKproperkey=productskukey.PSKproperkey,  # 订单的sku值

        )

    @verify_token_decorator
    def get_order_list(self):
        if is_tourist():
            return TOKEN_ERROR

    @verify_token_decorator
    def update_order(self):
        if is_tourist(self):
            return TOKEN_ERROR 
