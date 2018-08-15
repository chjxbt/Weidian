# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource

from WeiDian.control.CActivity import CActivity


class AActivity(Resource):
    def __init__(self):
        self.control_activity = CActivity()

    def get(self, activity):
        print activity
        apis = {
            "get_all": "self.control_activity.get_all()",
        }
        res = apis[activity]
        return res