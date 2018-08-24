# *- coding:utf8 *-
from flask import request
from WeiDian.common.token_required import verify_token_decorator
from WeiDian.common.import_status import import_status
from WeiDian.service.SOrder import SOrder
from WeiDian.config.response import PARAMS_MISS, SYSTEM_ERROR, AUTHORITY_ERROR
from WeiDian.common.token_required import is_tourist


class COrder():
    def __init__(self):
        self.sorder = SOrder()

    @verify_token_decorator
    def add_one(self):
        if is_tourist():
            return AUTHORITY_ERROR

    @verify_token_decorator
    def get_order_list(self):
        if is_tourist():
            return AUTHORITY_ERROR

    @verify_token_decorator
    def update_order(self):
        if is_tourist(self):
            return AUTHORITY_ERROR
