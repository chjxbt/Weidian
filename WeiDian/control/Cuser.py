# *- coding:utf8 *-
import re
import sys
import os
from flask import request, redirect
# import logging
import uuid
import datetime
import json
import urllib2

from weixin import WeixinError
from weixin.login import WeixinLoginError, WeixinLogin

from WeiDian import logger
from WeiDian import mp
from WeiDian.common.params_require import parameter_required
from WeiDian.config.response import PARAMS_MISS, SYSTEM_ERROR, NETWORK_ERROR, TOKEN_ERROR
from WeiDian.common.token_required import verify_token_decorator, usid_to_token
from WeiDian.common.import_status import import_status
from WeiDian.common.timeformat import format_for_db
from WeiDian.config.setting import QRCODEHOSTNAME, APP_ID, APP_SECRET_KEY
from WeiDian.config.urlconfig import get_subscribe
from WeiDian.service.SUser import SUser
from WeiDian.service.STask import STask
from WeiDian.service.SMyCenter import SMyCenter
from WeiDian.common.loggers import generic_log
sys.path.append(os.path.dirname(os.getcwd()))


class CUser():

    def __init__(self):
        self.suser = SUser()
        self.stask = STask()
        self.smycenter = SMyCenter()

    def login(self):
        json_data = request.json
        if not json_data:
            return PARAMS_MISS
        usname = json_data.get('usname')
        # uspassword = json_data.get('uspassword')
        # if not usname or not uspassword:
        #     raise PARAMS_MISS('请输入用户名或密码')
        user = self.suser.verify_user(usname)
        # if not user:
        #     raise SYSTEM_ERROR('用户名或者密码错误')
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

    def weixin_callback(self):
        """回调, 通过code, 获取用户信息"""
        try:
            args = request.args.to_dict()
            code = args.get('code')
            state = args.get('state')
            state = state.replace('$', '#').replace('~', '?').replace('+', '=')

            wxlogin = WeixinLogin(APP_ID, APP_SECRET_KEY)
            data = wxlogin.access_token(code)
            # 这是本人的openid
            openid = data.openid
            user = self.suser.get_user_by_openid(openid)
            # 是否关注 todo
            wx_subscribe = self.get_wx_response(get_subscribe.format(data.access_token, openid), "get subscribe")
            generic_log(wx_subscribe)
            # if "subscribe" not in wx_subscribe:
            #     logger.error("get subscribe error %s", wx_subscribe)
            #     raise WeixinError(u'get subscribe error')
            wx_subscribe = dict()
            subscribe = wx_subscribe.get("subscribe", 0)
            data = wxlogin.user_info(data.access_token, data.openid)
            if not user:
                # 新用户
                # 这是上级openid, 而非本人openid, 根据openid获取上级身份
                upper_list = re.findall(r'openid=(.*?)&?', state)
                upper = upper_list[0] if upper_list else None
                upperd = self.suser.get_user_by_openid(upper)
                upperd_id = upperd.USid if upperd else None
                # 添加用户
                usid = str(uuid.uuid1())
                self.suser.add_model("User", **{
                    "USid": usid,
                    "openid": openid,
                    "USlastlogin": datetime.datetime.now().strftime(format_for_db),
                    "USheader": data.get('headimgurl'),
                    "USlevel": 0,
                    "USgender": data.get('sex'),
                    "USname": data.get('nickname'),
                    "UPPerd": upperd_id,
                    "unionid": data.get('openid'),
                    "subscribe": subscribe,
                })
            else:
                # 老用户
                usid = user.USid
                print(usid)
                update_dict = {
                    "USlastlogin": datetime.datetime.now().strftime(format_for_db),
                    "USheader": data.get("headimgurl"),
                    "USgender": data.get("sex"),
                    "USname": data.get("nickname"),
                    "unionid": data.get("unionid"),
                    "subscribe": subscribe,
                }
                update_result = self.suser.update_user(usid, update_dict)
                if not update_result:
                    raise SYSTEM_ERROR()
            # 生成token
            token = usid_to_token(usid)
            redirect_url = state + "?newtoken=" + token
            return redirect(redirect_url)
        except WeixinError as e:
            generic_log(e)
            return redirect(QRCODEHOSTNAME)

    def wx_login(self):
        data = request.json
        state_url = data.get('url') or request.url
        state_url = state_url.replace('#', '$').replace('?', '~').replace('=', '+')
        state = str(state_url)
        login = WeixinLogin(APP_ID, APP_SECRET_KEY)
        redirect_url = login.authorize(QRCODEHOSTNAME + "/user/wechat_callback", 'snsapi_userinfo', state=state)
        return {"message":
            {
                'redirect_url': redirect_url
            }, "status": 302}

    def get_accesstoken(self):
        args = request.args.to_dict()
        logger.info("args", args)
        true_params = ["code"]
        for key in true_params:
            if key not in args:
                return PARAMS_MISS

        from WeiDian.config.setting import APP_ID, APP_SECRET_KEY, wximg
        from WeiDian.config.urlconfig import get_access_toke, get_user_info, get_subscribe
        # 获取access_token openid

        request_url = get_access_toke.format(APP_ID, APP_SECRET_KEY, args["code"])
        # strResult = None
        # try:
        #
        #     req = urllib2.Request(request_url)
        #     response = urllib2.urlopen(req)
        #     strResult = response.read()
        #     response.close()
        #     logger.debug(strResult)
        # except Exception as e:
        #     print(e)
        #     return NETWORK_ERROR

        jsonResult = self.get_wx_response(request_url, "get access_token")
        if "access_token" not in jsonResult or "openid" not in jsonResult:
            logger.error("get access token and openid error %s", jsonResult)
            return jsonResult
        access_token = jsonResult["access_token"]
        openid = jsonResult['openid']
        user = self.suser.get_user_by_openid(openid)

        is_first = not bool(user)

        wx_subscribe = self.get_wx_response(get_subscribe.format(mp.access_token, openid), "get subscribe")
        if "subscribe" not in wx_subscribe:
            logger.error("get subscribe error %s", wx_subscribe)
            return wx_subscribe
        subscribe = wx_subscribe.get("subscribe", 0)

        user_info = self.get_wx_response(get_user_info.format(access_token, openid), "get user info")
        if "errcode" in user_info or "errmsg" in user_info:
            response = import_status("get_user_info_error", "WD_ERROR", "error_get_user_info")
            response['data'] = user_info
            return response
        upperd = self.suser.get_user_by_openid(args.get("UPPerd", ""))

        upperd_id = upperd.USid if upperd else None
        user_level = 0 if is_first else user.USlevel

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
                "UPPerd": upperd_id,
                "unionid": user_info.get("unionid"),
                "accesstoken": access_token,
                "subscribe": subscribe,
            })
            # self.smycenter.add_model("MyCenter", **{
            #     "MYid": str(uuid.uuid1()),
            #     "USid": usid,
            #     "MYranking": '0',
            #     "MYrewards": '0'
            # })

            tasl_level = self.stask.get_tasklevel_by_level(1)
            task_list = self.stask.get_task_by_tlid(tasl_level.TLid)

            for task in task_list:
                self.suser.add_model("TaskUser", **{
                    "TUid": str(uuid.uuid1()),
                    "USid": usid,
                    "TAid": task.TAid,
                    "TUstatus": 0,
                    "TUnumber": 0
                })

        else:
            usid = user.USid
            update_result = self.suser.update_user(usid, {
                "USlastlogin": datetime.datetime.now().strftime(format_for_db),
                "USheader": user_info.get("headimgurl"),
                "USgender": user_info.get("sex"),
                "USname": user_info.get("nickname"),
                "unionid": user_info.get("unionid"),
                "accesstoken": access_token,
                "subscribe": subscribe,
            })
            if not update_result:
                return SYSTEM_ERROR
        userlogintime = self.suser.get_user_login_time(usid)
        now = datetime.datetime.now().strftime(format_for_db)

        is_today_first = True
        if userlogintime:
            is_today_first = bool(userlogintime.USTcreatetime[:-6] < now[:-6])
        self.suser.add_model("UserLoginTime", **{
            "ULTid": str(uuid.uuid1()),
            "USid": usid,
            "USTip": request.remote_addr,
            "USTcreatetime": now,
        })
        response = import_status("SUCCESS_GET_OPENID", "OK")
        from WeiDian.config.enums import icon
        response["data"] = {
            "is_first": int(is_first),
            "subscribe": subscribe,
            "openid": openid,
            "access_token": access_token,
            "wximg": wximg,
            'user_level': user_level,
            "is_today_first": int(is_today_first),
            "token": usid_to_token(usid),
            "icon": icon
        }
        logger.debug("get loggin response %s", response)
        return response

    # # @verify_token_decorator
    # def get_wx_config_accesstoken(self):
    #     from WeiDian.config.urlconfig import get_jsapi, get_server_access_token, signature_str
    #     from WeiDian.config.setting import APP_ID
    #     import random
    #     import string
    #     import time
    #     import hashlib
    #     # if not hasattr(request, 'user'):
    #     #     return TOKEN_ERROR  # 未登录, 或token错误
    #     url = request.args.to_dict().get("url")
    #     # user = self.suser.get_user_by_user_id(request.user.id)
    #     # logger.info('get user accesstoken: %s', user.accesstoken)
    #     # logger.info('get user id : %s', request.user.id)
    #     # if not user:
    #     #     return SYSTEM_ERROR
    #     from WeiDian.common.divide import Partner
    #     pt = Partner()
    #     access_token_server, ticket, access_time = pt.access_token
    #     access_time = datetime.datetime.strptime(access_time, format_for_db) if access_time else datetime.datetime.now()
    #     now = datetime.datetime.now()
    #     delta_time = (now - access_time).seconds
    #     if not ticket or delta_time > 60 * 60 * 2:
    #         access_token_server_res = self.get_wx_response(get_server_access_token, "get server access token")
    #         if "access_token" not in access_token_server_res:
    #             logger.error("get access token server error : %s", access_token_server_res)
    #             return NETWORK_ERROR
    #         access_token_server = access_token_server_res.get("access_token")
    #
    #         jsapiticket = self.get_wx_response(get_jsapi.format(access_token_server), "get jsapi_ticket")
    #
    #         if jsapiticket.get("errcode") == 0 and jsapiticket.get("errmsg") == "ok":
    #             ticket = jsapiticket.get("ticket")
    #         else:
    #             logger.error("get jsapi error :  %s", jsapiticket)
    #             return import_status("get_jsapi_error", "WD_ERROR", "error_get_jsapi")
    #
    #         pt.access_token = (access_token_server, ticket, now.strftime(format_for_db))
    #     # update_result = self.suser.update_user(user.USid, {"jsapiticket": ticket})
    #     # if not update_result:
    #     #     return SYSTEM_ERROR
    #
    #     noncestr = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    #     data = {
    #         "url": url,
    #         "jsapi_ticket": ticket,
    #         'timestamp': int(time.time()),
    #         "noncestr": noncestr,
    #
    #         # "secret": APP_SECRET_KEY
    #     }
    #     logger.info("get wx config %s", data)
    #     try:
    #         # response_str = "&".join([str(k)+'='+str(v) for k, v in data.items()])
    #         response_str = signature_str.format(**data)
    #         logger.debug("get response: %s", response_str)
    #         signature = hashlib.sha1(response_str).hexdigest()
    #         logger.debug('get signature: %s', signature)
    #         data['signature'] = signature
    #         data['appid'] = APP_ID
    #     except:
    #         logger.exception("Get wx config error")
    #         return SYSTEM_ERROR
    #     response = import_status("SUCCESS_GET_CONFIG", "OK")
    #     response['data'] = data
    #     return response

    def get_wx_config(self):

        url = request.args.get("url", request.url)
        # url = request.json.get("url", request.url)
        logger.debug('get url %s', url)
        data = mp.jsapi_sign(url=url)
        data['ticket'] = mp.jsapi_ticket
        logger.debug("get wx config %s", data)
        response = import_status("SUCCESS_GET_CONFIG", "OK")
        response['data'] = data
        return response

    def get_wx_response(self, url, urltype):
        try:
            req = urllib2.Request(url)
            response = urllib2.urlopen(req)
            strResult = response.read()
            response.close()
            logger.info("%s is %s", urltype, strResult)
            return json.loads(strResult)
        except:
            logger.exception("%s error", urltype)
            raise NETWORK_ERROR
