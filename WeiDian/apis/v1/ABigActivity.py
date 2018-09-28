# -*- coding:utf8 -*-
import sys
import os
from flask import jsonify
from flask_restful import Resource
sys.path.append(os.path.dirname(os.getcwd()))


class ABigActivity(Resource):
    def __init__(self):
        from WeiDian.control.CBigActivity import CBigActivity
        self.cbigactivity = CBigActivity()

    def get(self, bigactivity):
        print (bigactivity)
        apis = {
            "get_home_banner": "self.cbigactivity.get_home_banner()",
            "get_discover_banner": "self.cbigactivity.get_discover_banner()",
            "get_bigactivity": "self.cbigactivity.get_bigactivity()",
            'get_bigactivitys': "self.cbigactivity.get_bigactivity_list()",
        }
        res = eval(apis[bigactivity])
        return jsonify(res)

    def post(self, bigactivity):
        apis = {
            "create_hbact": "self.cbigactivity.create_home_bigactivity()",
            "create_dbact": "self.cbigactivity.create_discover_bigactivity()"
        }
        res = eval(apis[bigactivity])
        return jsonify(res)
