# *- coding:utf8 *-
import sys
import os
from flask import request
import logging

from WeiDian.config.response import PARAMS_MISS, SYSTEM_ERROR, NETWORK_ERROR
from WeiDian.common.token_required import verify_token_decorator, usid_to_token
from WeiDian.common.import_status import import_status
from WeiDian.service.SUser import SUser
from WeiDian.config.response import PARAMS_MISS, SYSTEM_ERROR
sys.path.append(os.path.dirname(os.getcwd()))


class CUser():

    def __init__(self):
        self.suser = SUser()

    def login(self):
        json_data = request.json
        if not json_data:
            return PARAMS_MISS
        usname = json_data.get('usname')
        uspassword = json_data.get('uspassword')
        if not usname or not uspassword:
            raise PARAMS_MISS('请输入用户名或密码')
        user = self.suser.verify_user(usname, uspassword)
        if not user:
            raise SYSTEM_ERROR('用户名或者密码错误')
        if user.USlevel == 0:
            level = 'ordinary'
        if user.USlevel > 0:
            level = 'partner'
        token = usid_to_token(user.USid)
        data = import_status('generic_token_success', "OK")
        data['data'] = {
            'token': token,
            'level': level,
        }
        return data

    def get_openid(self):
        args = request.args.to_dict()
        logging.info("args", args)
        true_params = ["code"]
        for key in true_params:
            if key not in args:
                return PARAMS_MISS

        from WeiDian.config.setting import APP_ID, APP_SECRET_KEY
        request_url = "https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type={3}" \
            .format(APP_ID, APP_SECRET_KEY, args["code"], "authorization_code")
        strResult = None
        try:
            import urllib2
            req = urllib2.Request(request_url)
            response = urllib2.urlopen(req)
            strResult = response.read()
            response.close()
            logging.info(strResult)
        except Exception as e:
            print(e)
            return NETWORK_ERROR
        import json
        jsonResult = json.loads(strResult)
        if "openid" not in strResult or "session_key" not in strResult:
            return jsonResult
        openid = jsonResult["openid"]
        response = import_status("SUCCESS_GET_OPENID", "OK")
        response["data"] = {}
        response["data"]["openid"] = openid
        return response
