# -*- coding: utf-8 -*-
from flask import jsonify
from flask_restful import Resource

from WeiDian.control.CCommision import CCommision


class ACommision(Resource):
    def __init__(self):
        self.ccommision = CCommision()

    def get(self, comm):
        apis = {
            'get_comm_list': "self.ccommision.get_commsion_list()"
        }
        res = eval(apis[comm])
        return jsonify(res)
