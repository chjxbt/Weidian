# *- coding:utf8 *-
import sys
import os
from flask import request
# import logging
import uuid
import datetime
from WeiDian import logger
from WeiDian.config.response import PARAMS_MISS, SYSTEM_ERROR, NETWORK_ERROR
from WeiDian.common.token_required import verify_token_decorator, usid_to_token
from WeiDian.common.import_status import import_status
from WeiDian.common.timeformat import format_for_db
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

    def get_accesstoken(self):
        args = request.args.to_dict()
        logger.info("args", args)
        true_params = ["code"]
        for key in true_params:
            if key not in args:
                return PARAMS_MISS

        from WeiDian.config.setting import APP_ID, APP_SECRET_KEY
        from WeiDian.config.urlconfig import get_access_toke, get_user_info
        # 获取access_token openid

        request_url = get_access_toke.format(APP_ID, APP_SECRET_KEY, args["code"])
        strResult = None
        try:
            import urllib2
            req = urllib2.Request(request_url)
            response = urllib2.urlopen(req)
            strResult = response.read()
            response.close()
            logger.debug(strResult)
        except Exception as e:
            print(e)
            return NETWORK_ERROR
        import json

        jsonResult = json.loads(strResult)
        print("!!!get result = ", jsonResult)
        if "access_token" not in strResult or "openid" not in strResult:
            return jsonResult
        access_token = jsonResult["access_token"]
        openid = jsonResult['openid']
        user = self.suser.get_user_by_openid(openid)
        is_first = not bool(user)
        try:
            req = urllib2.Request(get_user_info.format(access_token, openid))
            response = urllib2.urlopen(req)
            user_info = response.read()
            response.close()
            logger.debug("get user info : %s", user_info)
        except:
            logger.exception("get user info error")
            return NETWORK_ERROR

        user_info = json.loads(user_info)
        if "errcode" in user_info or "errmsg" in user_info:
            response = import_status("get_user_info_error", "WD_ERROR", "error_get_user_info")
            response['data'] = user_info
            return response

        if is_first:
            usid = str(uuid.uuid1())
            self.suser.add_model("User", **{
                "USid": usid,
                "openid": openid,
                "USlastlogin": datetime.datetime.now().strftime(format_for_db),
                "USheader": user_info.get("headimgurl"),
                "USlevel": 0,
                "USgender": user_info.get("sex"),
                "USname": user_info.get("nickname"),
                "UPPerd": args.get("UPPerd", ""),
                "unionid": user_info.get("unionid")
            })
        else:
            usid = user.USid
            self.suser.update_user(usid, {
                "USlastlogin": datetime.datetime.now().strftime(format_for_db),
                "USheader": user_info.get("headimgurl"),
                "USgender": user_info.get("sex"),
                "USname": user_info.get("nickname"),
                "UPPerd": args.get("UPPerd", ""),
                "unionid": user_info.get("unionid")
            })

        self.suser.add_model("UserLoginTime", **{
            "ULTid": str(uuid.uuid1()),
            "USid": usid,
            "USTip": request.remote_addr,
            "USTcreatetime": datetime.datetime.now().strftime(format_for_db),
        })
        response = import_status("SUCCESS_GET_OPENID", "OK")
        response["data"] = {}
        response["data"]["access_token"] = access_token
        return response

    def get_wx_config(self):
        # ip = request.remote_addr
        # print ip
        from WeiDian.config.setting import APP_ID
        import random
        import string
        import time
        import hashlib
        noncestr = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        data = {
            "appid": APP_ID,
            'timestamp': int(time.time()),
            "nonceStr": noncestr,
            # "secret": APP_SECRET_KEY
        }
        try:
            response_str = "&".join([str(k)+'='+str(v) for k, v in data.items()])
            signature = hashlib.sha1(response_str).hexdigest()
            data['signature'] = signature
        except:
            logger.exception("Get wx config error")
            return SYSTEM_ERROR
        response = import_status("SUCCESS_GET_CONFIG", "OK")
        response['data'] = data
        return response
