from flask import jsonify
from flask_restful import Resource

from WeiDian.control.Cuser import CUser


class AUser(Resource):
    def __init__(self):
        self.cuser = CUser()

    def post(self, user):
        print user
        apis = {
            'login': 'self.cuser.login()',
            'get_openid': 'self.cuser.get_openid()'
        }
        res = eval(apis[user])
        return jsonify(res)