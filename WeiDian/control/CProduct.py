# *- coding:utf8 *-
import sys
import os

from WeiDian.common.MakeToken import verify_token_decorator
from WeiDian.common.import_status import import_status
from WeiDian.config.response import TOKEN_ERROR, AUTHORITY_ERROR

sys.path.append(os.path.dirname(os.getcwd()))
from flask import request



class CProduct():

    @verify_token_decorator
    def add_product_list(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if request.user.scope != 'SuperUser':
            return AUTHORITY_ERROR  # 权限不足
        json_data = request.json
        product_list = json_data.get('data')
        for product in product_list:
            pass


