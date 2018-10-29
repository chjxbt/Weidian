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
            "get_one_reward": "self.creward.get_one_reward()",
            "get_user_reward": "self.creward.get_user_reward()",
            "get_hand_out_reward": "self.creward.get_hand_out_reward()",
            "get_reward_packets": "self.creward.get_rewardpacket()",
            "get_reward_packet_detail": "self.creward.get_reward_packet_detail()",
            "get_grant_record": "self.creward.get_grant_record()",
        }
        res = eval(apis[reward])
        return jsonify(res)

    def post(self, reward):
        print reward
        apis = {
            "create_reward": "self.creward.create_reward()",
            "receive_reward": "self.creward.user_receive_reward()",
            "hand_out_reward": "self.creward.hand_out_reward()",
            "admin_giving_reward": "self.creward.admin_giving_reward()",
            "give_reward_to_others": "self.creward.give_reward_to_others()",
            "get_user_reward": "self.creward.get_user_pay_reward()",
            "get_transfer_reward": "self.creward.get_transfer_reward()",
            "create_rewardpacket": "self.creward.create_rewardpacket()",
            "del_rewardpacket": "self.creward.del_rewardpacket()",
            "update_reward": "self.creward.update_reward()",
        }
        res = eval(apis[reward])
        return jsonify(res)
