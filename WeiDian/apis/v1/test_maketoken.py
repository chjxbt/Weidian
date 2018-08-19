from flask import Blueprint
from flask.views import MethodView

from WeiDian.common.MakeToken import verify_token_decorator
from test.errors import ApiException


class TestToken(MethodView):
    def post(self):
        usid = '6882ad09-bf5f-4607-8ad1-1cd46b6158e0'
        from WeiDian.common.MakeToken import usid_to_token
        return usid_to_token(usid, model='SuperUser')

    @verify_token_decorator
    def get(self):
        from flask import request
        raise ApiException
        return 'fsfd'