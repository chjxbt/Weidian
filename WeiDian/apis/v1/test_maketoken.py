from flask import Blueprint
from flask.views import MethodView

from WeiDian.common.MakeToken import verify_token_decorator


class TestToken(MethodView):
    def post(self):
        usid = '6882ad09-bf5f-4607-8ad1-1cd46b6158e0'
        from WeiDian.common.MakeToken import usid_to_token
        return usid_to_token(usid)
        return str(len(usid_to_token(usid)))


    @verify_token_decorator
    def get(self):
        from flask import request
        request.user
        import ipdb
        ipdb.set_trace()

        return ''