# -*- coding:utf8 -*-
import platform
import sys
import os
import base64
from datetime import datetime, timedelta
from WeiDian import logger
from WeiDian.common.make_qrcode import make_qrcode
from WeiDian.common.params_require import parameter_required
from WeiDian.config.setting import QRCODEHOSTNAME, LinuxRoot, LinuxImgs, WindowsRoot
from flask import request
import math
import uuid
from sqlalchemy.orm import Session
from WeiDian.common.token_required import verify_token_decorator, is_admin, is_tourist
from WeiDian.common.TransformToList import add_model
from WeiDian.common.import_status import import_status
from WeiDian.common.timeformat import format_for_db, get_db_time_str
from WeiDian.config.response import PARAMS_MISS, TOKEN_ERROR, AUTHORITY_ERROR, SYSTEM_ERROR
from WeiDian.control.BaseControl import BaseActivityControl, BaseFile
sys.path.append(os.path.dirname(os.getcwd()))


class CActivity(BaseActivityControl):
    def __init__(self):
        from WeiDian.service.SActivity import SActivity
        self.sactivity = SActivity()
        from WeiDian.service.SActivityComment import SActivityComment
        self.sacomment = SActivityComment()
        from WeiDian.service.SActivityLike import SActivityLike
        self.salike = SActivityLike()
        from WeiDian.service.SSuperUser import SSuperUser
        self.ssuperuser = SSuperUser()
        from WeiDian.service.SActivityMedia import SActivityMedia
        self.smedia = SActivityMedia()
        from WeiDian.service.SActivityTag import SActivityTag
        self.stags = SActivityTag()
        from WeiDian.service.SActivityFoward import SActivityFoward
        self.foward = SActivityFoward()
        from WeiDian.service.SProduct import SProduct
        self.sproduct = SProduct()
        self.session = Session()
        from WeiDian.service.SUser import SUser
        self.suser = SUser()

    @verify_token_decorator
    def get_all(self):
        """获取条件下的所有活动
        http://127.0.0.1:5000/activity/get_all?navid=q&lasting=true
        """
        if is_tourist():
            return AUTHORITY_ERROR(u"未登录")
        args = request.args.to_dict()
        logger.info("this is get all activity args %s", args)
        parameter_required('tnid', 'start', 'count')
        tnid = args.get('tnid')  # 导航id
        suid = args.get('suid')  # 管理员id
        lasting = args.get('lasting', True)  # 是否正在进行的活动
        start = int(args.get('start', 0))  # 起始位置
        count = int(args.get('count', 5))  # 取出条数
        page = (args.get('page'))
        if not page:
            page = int(math.floor(start / count) + 1)
        if not (tnid or suid):
            raise PARAMS_MISS(u"参数缺失")
        try:
            if tnid:
                activity_list = self.sactivity.get_activity_by_topnavid(tnid, page, count)
                len_aclist = self.sactivity.get_activity_count(tnid)
                logger.debug("get activity_list")

            if suid:
                activity_list = self.sactivity.get_activity_by_suid(suid, page, count)

            # if not activity_list:
            #     raise SYSTEM_ERROR(u'数据库错误')

            if lasting is True:
                now_time = datetime.strftime(datetime.now(), format_for_db)
                activity_list = filter(lambda act: act.ACstarttime < now_time < act.ACendtime, activity_list)
            for activity in activity_list:
                self.sactivity.update_view_num(activity.ACid)
                self.fill_detail(activity)
                self.fill_like_num(activity)
                self.fill_type(activity)
                if activity.ACSkipType == 0:
                    self.fill_comment_two(activity)
                if activity.ACSkipType == 2:
                    self.fill_soldnum(activity)
                    self.fill_product(activity)

            # map(self.fill_detail, activity_list)
            # map(self.fill_comment_two, activity_list)
            # map(self.fill_like_num, activity_list)
            # map(self.fill_type, activity_list)
            # s5 = time.time()
            # map(self.fill_product, activity_list)
            # e5 = time.time()
            # print "fill_product %s" %(e5 - s5)
            data = import_status("get_activity_list_success", "OK")
            data["count"] = len_aclist
            data["data"] = activity_list
            return data
        except:
            logger.exception("get activity error")
            return SYSTEM_ERROR(u"服务器繁忙")

    @verify_token_decorator
    def get_one(self):
        """通过acid获取活动及活动下的评论
        """
        if is_tourist():
            return AUTHORITY_ERROR(u"未登录或token错误")
        args = request.args.to_dict()
        logger.info("get one act args is %s", args)
        parameter_required('acid')
        acid = args.get('acid')  # 活动id
        try:
            activity = self.sactivity.get_activity_by_acid(acid)
            logger.debug("get one act access")
            if not activity:
                return SYSTEM_ERROR(u'数据错误，无此内容')
            activity = self.fill_detail(activity)
            activity = self.fill_comment(activity)
            data = import_status("get_activity_info_success", "OK")
            data["data"] = activity
            return data
        except:
            logger.exception("get one act error")
            return SYSTEM_ERROR(u"服务器繁忙")

    @verify_token_decorator
    def delete_one(self):
        """删除一个活动, 需要管理员的登录状态"""
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if not is_admin():
            return AUTHORITY_ERROR  # 权限不足
        data = request.json
        acid = data.get('acid')
        if not acid:
            return PARAMS_MISS
        self.sactivity.delete_activity(acid)
        response_del_activity = import_status('delete_activity_success', 'OK')
        response_del_activity['data'] = {}
        response_del_activity['data']['acid'] = acid
        return response_del_activity

    @verify_token_decorator
    def stop_one(self):
        """手动截止活动"""
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token
        if not is_admin():
            return AUTHORITY_ERROR  # 权限不足
        data = request.json
        acid = data.get('acid')
        if not acid:
            return PARAMS_MISS
        self.sactivity.stop_activity(acid)
        response_stop_activity = import_status('stop_activity_success', 'OK')
        response_stop_activity['data'] = {}
        response_stop_activity['data']['acid'] = acid
        return response_stop_activity

    @verify_token_decorator
    def add_one(self):
        """添加一个活动, 需要管理员的登录状态"""
        if not is_admin():
            raise AUTHORITY_ERROR(u'当前非管理员权限')
        data = request.json
        logger.info("add activity data is %s", data)
        parameter_required('ACtext', 'TopnavId', 'ACSkipType')
        now_time = datetime.strftime(datetime.now(), format_for_db)
        ACstarttime = data.get('acstarttime', now_time)                         # 活动开始时间, 默认当前时间
        ACstarttime_str_to_time = datetime.strptime(ACstarttime, format_for_db)
        three_days_later = datetime.strftime(ACstarttime_str_to_time + timedelta(days=3), format_for_db)
        ACendtime = data.get('ACendtime', three_days_later)                     # 活动结束时间, 默认3天以后
        TopnavId = data.get('TopnavId')       # 导航页面
        ACtext = data.get('ACtext')           # 文字内容
        ACSkipType = data.get('ACSkipType')   # 跳转类型
        BAid = data.get('BAid', '0')          # 专题id
        PRid = data.get('PRid', '0')          # 商品id
        media = data.get('media')             # 多媒体
        tags = data.get('tags')               # 右上角tag标签
        ACistop = data.get('ACistop', 0)
        ACtitle = data.get('ACtitle')

        if str(ACistop) == 'True':
            istop = self.sactivity.get_top_activity(TopnavId)
            if istop:
                self.sactivity.change_top_act_status(istop.ACid, {'ACistop': False})



        # if not media or not ACtext or not prid or not topnavid:
        #     return PARAMS_MISS
        # relation_product = self.sproduct.get_product_by_prid(PRid)  # 关联的商品
        # if not relation_product:  # 如果没有该商品
        #     return SYSTEM_ERROR("prid错误，没有该商品")
        # 创建活动
        ACid = str(uuid.uuid1())
        self.sactivity.add_model('Activity', **{
            'ACid': ACid,
            # 'PRid': relation_product.PRid,
            'ACSkipType': ACSkipType,
            'BAid': BAid,
            'PRid': PRid,
            'SUid': request.user.id,
            'ACtype': data.get('ACtype'),  # 类型
            'TopnavId': TopnavId,
            'ACtext': ACtext,
            'AClikeFakeNum': data.get('likenum', 0),  # 喜欢数
            'ACbrowsenum': data.get('browsenum', 0),  # 浏览数
            'ACforwardFakenum': data.get('fowardnum', 0),  # 转发数量
            'ACProductsSoldFakeNum': data.get('soldnum', 0),   # 商品的销售量
            'ACstarttime': ACstarttime,
            'ACendtime': ACendtime,
            'ACtitle': ACtitle,
            'ACistop': ACistop  # TODO 判断置顶待完善
        })
        # 创建media
        image_num = 0  # 标志用来限制图片或视频的数量
        for img_or_video in media:
            img_or_video_keys = img_or_video.keys()
            if 'AMimage' in img_or_video_keys and 'AMvideo' not in img_or_video_keys:
                """图片"""
                self.smedia.add_model('ActivityMedia', **{
                    'AMid': str(uuid.uuid1()),
                    'ACid': ACid,
                    'AMimage': img_or_video.get('AMimage'),
                    'AMsort': img_or_video.get('AMsort', 1)
                })
                image_num += 1
                if image_num >= 9:
                    raise SYSTEM_ERROR(u"图片超出数量限制")
            elif 'AMimage' not in img_or_video_keys and 'AMvideo' in img_or_video_keys:
                """视频"""
                if image_num < 1:
                    # 只有在无图片的状况下才会添加视频
                    self.smedia.add_model('ActivityMedia', **{
                        'AMid': str(uuid.uuid1()),
                        'ACid': ACid,
                        'AMvideo': img_or_video.get('AMvideo')
                    })
                    # 只可以添加一个视频, 且不可以再添加图片
                    break
        # 创建tag
        if tags:
            for tag in tags:
                add_model('ActivityTag', **{
                    'ATid': str(uuid.uuid1()),
                    'ACid': ACid,
                    'ATname': tag.get('ATname'),
                })
        response_make_activity = import_status('add_activity_success', 'OK')
        response_make_activity['data'] = {
            'ACid': ACid
        }
        return response_make_activity

    @verify_token_decorator
    def update_activity(self):
        if not is_admin():
            raise AUTHORITY_ERROR(u'当前非管理员权限')
        args = request.args.to_dict()
        logger.info("this is update activity args %s", args)
        data = request.json
        logger.info("this is update activity data %s", data)
        parameter_required("acid", "PRid", "ACtype", "TopnavId", "ACtext", "AClikeFakeNum", "ACforwardFakenum", "ACProductsSoldFakeNum", "ACstarttime", "ACendtime", "ACistop")
        now_time = datetime.strftime(datetime.now(), format_for_db)
        data['ACupdatetime'] = now_time
        act_info = self.sactivity.update_activity_by_acid(args["acid"], data)
        if not act_info:
            return SYSTEM_ERROR
        response = import_status('update_activity_success', 'OK')
        response['data'] = {'acid': args["acid"]}
        return response

    @verify_token_decorator
    def share_activity(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        data = request.json
        logger.info("share qrcode data is %s", data)
        data_url = data.get("dataurl")
        now_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
        logger.debug("get user info")
        try:
            user = self.suser.get_user_by_user_id(request.user.id)
            if not user:
                return SYSTEM_ERROR(u'找不到该用户')
            save_path = LinuxRoot + LinuxImgs + "/qrcode/" + user.openid + now_time + '.png' if platform.system() == "Linux" else WindowsRoot + "qrcode/" + user.openid + now_time + '.png'
            make_qrcode(user.USheader, data_url, save_path)
            response = import_status("make_qrcode_success", "OK")
            response["qrcodeurl"] = QRCODEHOSTNAME + '/' + LinuxImgs + '/qrcode/' + user.openid + now_time + '.png'
            response["components"] = QRCODEHOSTNAME + '/' + LinuxImgs + '/components.png'
            return response
        except:
            logger.debug("make qrcode error")
            return SYSTEM_ERROR

    @verify_token_decorator
    def generate_poster(self):
        # formdata = request.form
        data = request.json
        logger.info("data is %s", data)
        # files = request.files.get("file")
        if platform.system() == "Windows":
            rootdir = "D:/qrcode"
        else:
            rootdir = "/opt/WeiDian/imgs/shareposter/"
        if not os.path.isdir(rootdir):
            os.mkdir(rootdir)
        # if "FileType" not in formdata:
        #     return
        # filessuffix = str(files.filename).split(".")[-1]
        # index = formdata.get("index", 1)
        # filename = request.user.openid + get_db_time_str() + "." + filessuffix
        filename = request.user.openid + get_db_time_str() + ".png"
        filepath = os.path.join(rootdir, filename)
        print(filepath)
        # files.save(filepath)
        baseimg = data.get('baseimg')
        imgdata = baseimg.split(',')[-1]
        img = base64.b64decode(imgdata)
        file = open(filepath, 'wb')
        file.write(img)
        file.close()
        response = import_status("save_poster_success", "OK")
        # url = Inforcode.ip + Inforcode.LinuxImgs + "/" + filename
        url = QRCODEHOSTNAME + "/imgs/shareposter/" + filename
        # print(url)
        logger.info("this url is %s", url)
        response["data"] = url
        return response

    @verify_token_decorator
    def upload_home_images(self):
        if not is_admin():
            raise AUTHORITY_ERROR(u'权限不足')
        filetype = request.args.to_dict().get("filetype", 'home')

        url = BaseFile().upload_file(filetype)
        res = import_status("save_poster_success", "OK")
        res['data'] = url
        return res
