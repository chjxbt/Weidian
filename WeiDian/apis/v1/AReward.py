# -*- coding:utf8 -*-
import sys
import os
from flask import jsonify
from flask_restful import Resource
sys.path.append(os.path.dirname(os.getcwd()))


class AReward(Resource):
    def __init__(self):
        from WeiDian.control.CRaward import CRaward
        self.creward = CRaward()

    def get(self, reward):
        print reward
        apis = {
            "get_one_reward": "self.creward.get_one_reward()"
        }
        res = eval(apis[reward])
        return jsonify(res)

    def post(self, reward):
        print reward
        apis = {
            "create_reward": "self.creward.create_reward()",
            "receive_reward": "self.creward.user_receive_reward()",
        }
        res = eval(apis[reward])
        return jsonify(res)
