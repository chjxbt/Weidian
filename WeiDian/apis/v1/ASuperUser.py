from flask import jsonify
from flask_restful import Resource

from WeiDian.control.CSuperUser import CSuperUser


class ASuperUser(Resource):

    def __init__(self):
        self.csuperuser = CSuperUser()

    def post(self, super):
        print super
        apis = {
            'login': 'self.csuperuser.login()',
        }
        res = eval(apis[super])
        return jsonify(res)
