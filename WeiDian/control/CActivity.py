# -*- coding:utf8 -*-
import platform
import sys
import os
import base64
from datetime import datetime, timedelta
from WeiDian import logger
from WeiDian.common.divide import Partner
from WeiDian.common.get_model_return_list import get_model_return_list
from WeiDian.common.loggers import generic_log
from WeiDian.common.make_qrcode import make_qrcode
from WeiDian.common.params_require import parameter_required
from WeiDian.config.setting import QRCODEHOSTNAME, LinuxRoot, LinuxImgs, WindowsRoot
from flask import request
import math
import uuid
from WeiDian.common.token_required import verify_token_decorator, is_admin, is_tourist, is_partner
from WeiDian.common.TransformToList import add_model
from WeiDian.common.import_status import import_status
from WeiDian.common.timeformat import format_for_db, get_db_time_str, get_web_time_str, format_for_web_second
from WeiDian.config.response import PARAMS_MISS, TOKEN_ERROR, AUTHORITY_ERROR, SYSTEM_ERROR, NOT_FOUND, PARAMS_ERROR
from WeiDian.control.BaseControl import BaseActivityControl, BaseFile, BaseTask
from WeiDian.models.model import Activity
sys.path.append(os.path.dirname(os.getcwd()))


class CActivity(BaseActivityControl, BaseTask):
    hmsk_type = ['3', '4']

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
        from WeiDian.service.SUser import SUser
        self.suser = SUser()
        from WeiDian.service.SBigActivity import SBigActivity
        self.sbigactivity = SBigActivity()
        from WeiDian.service.STopNav import STopNav
        self.stopnav = STopNav()
        from WeiDian.service.STask import STask
        self.stask = STask()
        self.empty = ['', None, [], {}]

    @verify_token_decorator
    def set_show_type(self):
        if not is_admin():
            raise TOKEN_ERROR(u'请使用管理员登录')
        data = parameter_required('skip_type')
        try:
            skip_type = str(data.get('skip_type'))
            if skip_type not in ['0', '1', '2']:
                raise TypeError()
        except TypeError as e:
            raise PARAMS_ERROR(u'参数skip_type错误')
        Partner().set_item('skip', 'skip_type', skip_type)
        response = import_status('set_success', 'OK')
        return response

    @verify_token_decorator
    def get_show_type(self):
        if not is_admin():
            raise AUTHORITY_ERROR(u'请使用管理员登录')
        settings = Partner()
        skiptype = settings.get_item('skip', 'skip_type')
        response = import_status("messages_get_item_ok", "OK")
        response['data'] = {'skiptype': skiptype}
        return response

    @verify_token_decorator
    def get_all(self):
        """获取条件下的所有活动
        """
        if is_tourist():
            return AUTHORITY_ERROR(u"未登录")
        args = request.args.to_dict()
        logger.info("this is get all activity args %s", args)
        parameter_required(u'tnid')
        tnid = args.get('tnid')  # 导航id
        suid = args.get('suid')  # 管理员id
        lasting = args.get('lasting', 'true')  # 是否正在进行的活动
        acid = args.get("acid")
        if not acid:
            acid = None
        start = int(args.get('start', 0))  # 起始位置
        count = int(args.get('count', 5))  # 取出条数
        page = (args.get('page'))
        # 过滤跳转类型
        skiptype = args.get('skiptype')
        if skiptype is None:
            settings = Partner()
            skiptype = settings.get_item('skip', 'skip_type')  # 配置文件中的过滤条件(默认)
        if skiptype == 'all':
            skiptype = None
        # 分页
        if not page:
            page = int(math.floor(start / count) + 1)
        if not (tnid or suid):
            raise PARAMS_MISS(u"参数缺失")
        try:
            topnav = self.stopnav.get_topnav_by_tnid(tnid)
            if not topnav:
                raise NOT_FOUND(u'无此tnid')
            if topnav.TNtype == 2 and str(tnid) != '1':  # '1'为每日十荐页tnid
                skiptype = 0
            print (skiptype)

            now_time = None

            if str(lasting) == 'true':
                now_time = datetime.strftime(datetime.now(), format_for_db)
            activity_list = self.sactivity.get_activity_by_topnavid(tnid, page, count, skiptype, acid, suid, now_time)
            logger.info("get activity_list success")

            # if suid:
            #     activity_list = self.sactivity.get_activity_by_suid(suid, page, count)
            # if not activity_list:
            #     raise SYSTEM_ERROR(u'数据库错误')

            for activity in activity_list:
                self.sactivity.update_view_num(activity.ACid)
                self.fill_detail(activity)
                self.fill_like_num(activity)
                self.fill_type(activity)
                activity.fill(activity.AClinkvalue, 'aclinkvalue')
                if activity.ACSkipType == 0:
                    self.fill_comment_two(activity)
                    activity.fill('none_skip', 'skip_type')
                    activity.fill('无跳转类型', 'zh_skip_type')
                elif activity.ACSkipType == 1:
                    baid = activity.AClinkvalue
                    activity.fill('bigactivity', 'skip_type')
                    activity.fill('专题', 'zh_skip_type')
                    bigactivity = self.sbigactivity.get_one_big_act(baid)
                    if not bigactivity:
                        # raise NOT_FOUND()
                        pass
                    else:
                        bigactivity_type = bigactivity.BAtype
                        big_activity_content = {'type': bigactivity_type}
                        big_activity_content.setdefault('baid', bigactivity.BAid)
                        # 图片类型专题
                        if bigactivity_type == 0:
                            big_activity_content.setdefault('baimage', bigactivity.BAlongimg)  # 返回字段不修改
                            big_activity_content.setdefault('baid', bigactivity.BAid)
                        activity.fill(big_activity_content, 'bigactivity')
                elif activity.ACSkipType == 2:
                    self.fill_soldnum(activity)
                    self.fill_product(activity)
                    activity.fill('product', 'skip_type')
                    activity.fill('商品', 'zh_skip_type')
                activity.ACstarttime = get_web_time_str(activity.ACstarttime)
                activity.ACendtime = get_web_time_str(activity.ACendtime)

            # map(self.fill_detail, activity_list)
            # map(self.fill_comment_two, activity_list)
            # map(self.fill_like_num, activity_list)
            # map(self.fill_type, activity_list)
            # s5 = time.time()
            # map(self.fill_product, activity_list)
            # e5 = time.time()
            # print "fill_product %s" %(e5 - s5)
            data = import_status("get_activity_list_success", "OK")
            data["count"] = request.all_count
            data["page_count"] = request.page_count
            data["data"] = activity_list
            return data
        except Exception as e:
            logger.exception("get activity error")
            generic_log(e)
            return e

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
                raise SYSTEM_ERROR(u'数据错误，无此内容')
            self.sactivity.update_view_num(activity.ACid)
            self.fill_detail(activity)
            self.fill_like_num(activity)
            self.fill_type(activity)
            if activity.ACSkipType == 0:
                self.fill_comment_two(activity)
                activity.fill('none_skip', 'skip_type')
                activity.fill('无跳转类型', 'zh_skip_type')
            elif activity.ACSkipType == 1:
                baid = activity.AClinkvalue
                activity.fill('bigactivity', 'skip_type')
                activity.fill('专题', 'zh_skip_type')
                bigactivity = self.sbigactivity.get_one_big_act(baid)
                if not bigactivity:
                    # raise NOT_FOUND()
                    pass
                else:
                    bigactivity_type = bigactivity.BAtype
                    big_activity_content = {'type': bigactivity_type}
                    big_activity_content.setdefault('baid', bigactivity.BAid)
                    # 图片类型专题
                    if bigactivity_type == 0:
                        big_activity_content.setdefault('baimage', bigactivity.BAlongimg)  # 返回字段不修改
                        big_activity_content.setdefault('baid', bigactivity.BAid)
                    activity.fill(big_activity_content, 'bigactivity')
            elif activity.ACSkipType == 2:
                self.fill_soldnum(activity)
                self.fill_product(activity)
                activity.fill('product', 'skip_type')
                activity.fill('商品', 'zh_skip_type')
            activity.ACstarttime = get_web_time_str(activity.ACstarttime)
            activity.ACendtime = get_web_time_str(activity.ACendtime)
            data = import_status("get_activity_info_success", "OK")
            data["data"] = activity
            return data
        except:
            logger.exception("get one act error")
            return SYSTEM_ERROR(u"服务器繁忙")

    # @verify_token_decorator
    # def delete_one(self):
    #     """删除一个活动, 需要管理员的登录状态"""
    #     if not hasattr(request, 'user'):
    #         return TOKEN_ERROR  # 未登录, 或token错误
    #     if not is_admin():
    #         return AUTHORITY_ERROR  # 权限不足
    #     data = request.json
    #     acid = data.get('acid')
    #     if not acid:
    #         return PARAMS_MISS
    #     self.sactivity.delete_activity(acid)
    #     response_del_activity = import_status('delete_activity_success', 'OK')
    #     response_del_activity['data'] = {}
    #     response_del_activity['data']['acid'] = acid
    #     return response_del_activity

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
        logger.debug("add activity data is %s", data)
        parameter_required(u'ACtext', u'TopnavId')
        now_time = datetime.strftime(datetime.now(), format_for_web_second)
        ACstarttime = get_db_time_str(data.get('ACstarttime', now_time))                         # 活动开始时间, 默认当前时间
        ACstarttime_str_to_time = datetime.strptime(ACstarttime, format_for_db)
        three_days_later = datetime.strftime(ACstarttime_str_to_time + timedelta(days=3), format_for_web_second)
        ACendtime = get_db_time_str(data.get('ACendtime', three_days_later))                    # 活动结束时间, 默认3天以后
        TopnavId = data.get('TopnavId')       # 导航页面
        ACtext = data.get('ACtext')           # 文字内容
        # BAid = data.get('BAid', '0')          # 专题id
        # PRid = data.get('PRid', '0')          # 商品id
        media = data.get('media')             # 多媒体
        tags = data.get('tags')               # 右上角tag标签
        ACistop = data.get('ACistop', 0)
        ACtitle = data.get('ACtitle')
        AClinkvalue = data.get('AClinkvalue')
        SUid = data.get('SUid')
        SUid = request.user.id if not SUid else str(SUid)
        ACSkipType = int(data.get('ACSkipType', 0))   # 跳转类型
        # ACProductsSoldFakeNum = data.get('acproductssoldfakenum')
        # ACforwardFakenum = data.get('acforwardfakenum')
        # ACbrowsenum = data.get('acbrowsenum')
        # AClikeFakeNum = data.get('AClikeFakeNum')
        ACProductsSoldFakeNum = str(data.get('ACProductsSoldFakeNum', '')).strip() or 0
        ACforwardFakenum = str(data.get('ACforwardFakenum', '')).strip() or 0
        ACbrowsenum = str(data.get('ACbrowsenum', '')).strip() or 0
        AClikeFakeNum = str(data.get('AClikeFakeNum', '')).strip() or 0

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
        # 创建media
        image_num = 0  # 标志用来限制图片或视频的数量
        if media:
            for img_or_video in media:
                img_or_video_keys = img_or_video.keys()
                if 'amimage' in img_or_video_keys and 'amvideo' not in img_or_video_keys:
                    """图片"""
                    self.smedia.add_model('ActivityMedia', **{
                        'AMid': str(uuid.uuid1()),
                        'ACid': ACid,
                        'AMimage': img_or_video.get('amimage'),
                        'AMsort': img_or_video.get('amsort', 1)
                    })
                    image_num += 1
                    if image_num > 9:
                        raise SYSTEM_ERROR(u"图片超出数量限制")
                elif 'amimage' not in img_or_video_keys and 'amvideo' in img_or_video_keys:
                    """视频"""
                    if image_num < 1:
                        # 只有在无图片的状况下才会添加视频
                        self.smedia.add_model('ActivityMedia', **{
                            'AMid': str(uuid.uuid1()),
                            'ACid': ACid,
                            'AMvideo': img_or_video.get('amvideo')
                        })
                        # 只可以添加一个视频, 且不可以再添加图片
                        break
        # 创建tag
        if tags:
            for tag in tags:
                self.stags.add_model('ActivityTag', **{
                    'ATid': str(uuid.uuid1()),
                    'ACid': ACid,
                    'ATname': tag.get('ATname'),
                })

        # 是否添加进入专题
        baid = data.get('BAid')
        model_dict = {
            'ACid': ACid,
            # 'PRid': relation_product.PRid,
            'ACSkipType': ACSkipType,
            'AClinkvalue': AClinkvalue,
            # 'BAid': BAid,
            # 'PRid': PRid,
            'SUid': SUid,
            'ACtype': data.get('ACtype'),  # 类型
            'TopnavId': TopnavId,
            'ACtext': ACtext,
            'AClikeFakeNum': AClikeFakeNum,  # 喜欢数
            'ACbrowsenum': ACbrowsenum,  # 浏览数
            'ACforwardFakenum': ACforwardFakenum,  # 转发数量
            'ACProductsSoldFakeNum': ACProductsSoldFakeNum,   # 商品的销售量
            'ACstarttime': ACstarttime,
            'ACendtime': ACendtime,
            'ACtitle': ACtitle,
            'ACistop': ACistop
        }
        if baid:
            if ACSkipType != 2:
                raise PARAMS_ERROR(u'参数不合理, 仅跳转到商品的推文可以加入专题')
            model_dict['BAid'] = baid
        self.sactivity.add_model('Activity', **model_dict)

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
        logger.debug("this is update activity args %s", args)
        data = request.json
        logger.debug("this is update activity data %s", data)
        parameter_required("acid")
        now_time = datetime.strftime(datetime.now(), format_for_web_second)
        acid = args.get('acid')
        ACstarttime = get_db_time_str(data.get('acstarttime', now_time))  # 活动开始时间, 默认当前时间
        ACstarttime_str_to_time = datetime.strptime(ACstarttime, format_for_db)
        three_days_later = datetime.strftime(ACstarttime_str_to_time + timedelta(days=3), format_for_db)
        ACendtime = get_db_time_str(data.get('acendtime', get_web_time_str(three_days_later)))  # 活动结束时间, 默认3天以后
        TopnavId = data.get('topnavid')  # 导航页面
        ACtext = data.get('actext')  # 文字内容
        media = data.get('media')  # 多媒体
        tags = data.get('tags')  # 右上角tag标签
        ACistop = data.get('acistop', 0)
        ACtitle = data.get('actitle')
        AClinkvalue = data.get('aclinkvalue')
        SUid = data.get('suid')
        SUid = request.user.id if not SUid else str(SUid)
        ACSkipType = int(data.get('acskiptype', 0))  # 跳转类型
        ACProductsSoldFakeNum = data.get('acproductssoldfakenum')
        ACforwardFakenum = data.get('acforwardFakenum')
        ACbrowsenum = data.get('acbrowsenum')
        AClikeFakeNum = data.get('aclikeFakeNum')

        if str(ACistop) == 'True':
            istop = self.sactivity.get_top_activity(TopnavId)
            if istop:
                self.sactivity.change_top_act_status(istop.ACid, {'ACistop': False})

        image_num = 0  # 标志用来限制图片或视频的数量
        if media:
            for img_or_video in media:
                img_or_video_keys = img_or_video.keys()
                if 'amimage' in img_or_video_keys and 'amvideo' not in img_or_video_keys:
                    """图片"""
                    self.smedia.del_media_by_acid(acid)
                    self.smedia.add_model('ActivityMedia', **{
                        'AMid': str(uuid.uuid1()),
                        'ACid': acid,
                        'AMimage': img_or_video.get('amimage'),
                        'AMsort': img_or_video.get('amsort', 1)
                    })

                    image_num += 1
                    if image_num > 9:
                        raise SYSTEM_ERROR(u"图片超出数量限制")
                elif 'amimage' not in img_or_video_keys and 'amvideo' in img_or_video_keys:
                    """视频"""
                    if image_num < 1:
                        # 只有在无图片的状况下才会添加视频
                        self.smedia.del_media_by_acid(acid)
                        self.smedia.add_model('ActivityMedia', **{
                            'AMid': str(uuid.uuid1()),
                            'ACid': acid,
                            'AMvideo': img_or_video.get('amvideo')
                        })
                        # 只可以添加一个视频, 且不可以再添加图片
                        break
        # 创建tag
        if tags:
            for tag in tags:
                self.stags.del_tags_by_acid(acid)
                self.stags.add_model('ActivityTag', **{
                    'ATid': str(uuid.uuid1()),
                    'ACid': acid,
                    'ATname': tag.get('atname'),
                })

        # 是否添加进入专题
        baid = data.get('baid')
        model_dict = {
            'ACSkipType': ACSkipType,
            'AClinkvalue': AClinkvalue,
            'SUid': SUid,
            'ACtype': data.get('actype'),  # 类型
            'ACtext': ACtext,
            'AClikeFakeNum': AClikeFakeNum,  # 喜欢数
            'ACbrowsenum': ACbrowsenum,  # 浏览数
            'ACforwardFakenum': ACforwardFakenum,  # 转发数量
            'ACProductsSoldFakeNum': ACProductsSoldFakeNum,  # 商品的销售量
            'ACstarttime': ACstarttime,
            'ACendtime': ACendtime,
            'ACtitle': ACtitle,
            'ACistop': ACistop,
            'BAid': baid,
            'ACisdelete': data.get('acisdelete')
        }

        if baid:
            if ACSkipType != 2:
                raise PARAMS_ERROR(u'参数不合理, 仅跳转到商品的推文可以加入专题')
            model_dict['BAid'] = baid
        model_dict = {k: v for k, v in model_dict.items() if v not in self.empty}
        act_info = self.sactivity.update_activity_by_acid(acid, model_dict)
        if not act_info:
            raise SYSTEM_ERROR(u'数据错误')
        response = import_status('update_activity_success', 'OK')
        response['data'] = {'acid': acid}
        return response

    @verify_token_decorator
    def get_exist_tags(self):
        if not is_admin():
            raise AUTHORITY_ERROR(u'非管理员权限')
        args = request.args.to_dict()
        logger.debug("get tags args is %s", args)
        try:
            # tags_list = set(get_model_return_list(self.stags.get_exist_tags())['ATname'])
            tags_list = self.stags.get_exist_tags()
            originallist = []
            for tag in tags_list:
                originallist.append(tag[0])
            setlist = set(originallist)
            changelist = list(setlist)

            logger.info("try to get tags")
            response = import_status("messages_get_item_ok", "OK")
            response['date'] = {"tags_list": changelist}
            return response
        except Exception as e:
            logger.exception("get exist tags error")
            raise SYSTEM_ERROR(u"数据错误")

    @verify_token_decorator
    def share_activity(self):
        if is_tourist():
            raise TOKEN_ERROR(u'未登录')
        data = request.json
        logger.debug("share qrcode data is %s", data)
        # data_url = data.get("dataurl")
        data_url = self.get_share_url(data.get("dataurl"))
        try:
            logger.info("get user info")
            user = self.suser.get_user_by_user_id(request.user.id)
            if not user:
                raise SYSTEM_ERROR(u'找不到该用户')
            save_path = LinuxRoot + LinuxImgs + "/qrcode/" + user.openid + '.png' if platform.system() == "Linux" else WindowsRoot + "qrcode/" + user.openid + '.png'
            make_qrcode(user.USheader, data_url, save_path)
            response = import_status("make_qrcode_success", "OK")
            response["qrcodeurl"] = QRCODEHOSTNAME + '/' + LinuxImgs + '/qrcode/' + user.openid + '.png'
            response["components"] = QRCODEHOSTNAME + '/' + LinuxImgs + '/components.png'
            logger.debug('response url is %s', response["qrcodeurl"])

            if is_partner():

                self.do_shoppingtask_or_forwardtask(1)
            return response
        except:
            logger.exception("make qrcode error")
            return SYSTEM_ERROR(u'服务器繁忙')

    def get_share_url(self, url):
        if isinstance(url, unicode):
            _url = url.encode('utf8')
        else:
            _url = str(url)
        now_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')

        _url_punctuation = '& 'if '?' in _url else '?'
        _url = _url + "{0}time={1}".format(_url_punctuation, now_time)
        return _url

    @verify_token_decorator
    def generate_poster(self):
        # formdata = request.form
        data = request.json
        # logger.info("data is %s", data)   # 因为base64 太大，所以注释掉
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
        notimetag = request.args.to_dict().get("notimetag", '')
        url = BaseFile().upload_file(filetype, notimetag)
        res = import_status("save_photo_success", "OK")
        res['data'] = url
        return res

    @verify_token_decorator
    def get_activity_list_by_actitle(self):
        if not is_admin():
            raise AUTHORITY_ERROR(u'当前非管理员权限')
        args = request.args.to_dict()
        logger.debug('get arsgs %s', args)
        actitle = args.get("actitle")
        hmtype = args.get('hmtype', 3)
        if str(hmtype) not in self.hmsk_type:
            raise PARAMS_MISS(u"参数错误")

        from WeiDian.config.enums import HMSkipType
        topnav = self.stopnav.get_topnav_by_name(HMSkipType.get(str(hmtype)))
        acfilter = {Activity.ACtitle.contains(actitle), Activity.ACtext.contains(actitle)}
        activity_list = self.sactivity.get_activity_by_filter(acfilter, topnav.TNid)
        res = import_status("add_activity_success", "OK")
        res['data'] = activity_list
        return res