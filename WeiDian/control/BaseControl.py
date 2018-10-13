# -*- coding:utf8 -*-
import platform
import uuid
import os
import re
from datetime import datetime

from WeiDian.common.get_model_return_list import get_model_return_dict
from WeiDian.config.response import SYSTEM_ERROR
from flask import request
from WeiDian.common.TransformToList import list_add_models, dict_add_models
from WeiDian.common.divide import Partner
from WeiDian.common.token_required import is_partner, is_admin, is_tourist
from WeiDian.common.timeformat import get_web_time_str
from WeiDian.config.enums import activity_type, TASK_STATUS
from WeiDian import logger

class BaseActivityControl():

    def get_one_activity(self):
        pass

    def fill_detail(self, act):
        """填充一些关联活动的信息"""
        acid = act.ACid
        # tnid = act.TopnavId
        act.suuser = self.ssuperuser.get_one_super_by_suid(act.SUid)  # 超级用户
        act.media = self.smedia.get_media_by_acid(acid)  # 图片或视频
        act.tags = self.stags.get_show_tags_by_acid(acid)  # 右上角tag
        act.foward = self.foward.get_fowardnum_by_acid(acid)  # 转发数
        # act.likenum = self.salike.get_likenum_by_acid(acid)  # 喜欢数
        # if hasattr(request, 'user'):
        #     alreadylike = self.salike.is_like(request.user.id, acid)
        #     act.alreadylike = True if alreadylike else False
        # act.soldnum = self.sactivity.get_product_soldnum_by_acid(acid)  # 销量
        """活动剩余时间"""
        endtime = datetime.strptime(act.ACendtime, "%Y%m%d%H%M%S")
        remain = endtime - datetime.now()
        if remain.total_seconds() >= 21600:
            remaindays = remain.days
            remainhours = remain.seconds / 3600
            act.remaintime = [remaindays, remainhours, 0]
        else:
            remainminutes = remain.total_seconds() / 60
            act.remaintime = [0, remainminutes, 0]
        # act.count = self.sactivity.get_activity_count(tnid)
        act.add(
            'suuser',
            'media',
            'tags',
            'foward',
            'remaintime')
        return act

    def fill_soldnum(self, act):
        acid = act.ACid
        act.soldnum = self.sactivity.get_product_soldnum_by_acid(acid)  # 销量
        act.add('soldnum')
        return act


    def fill_like_num(self, activity):
        """添加点赞相关字段"""
        if hasattr(request, 'user'):
            alreadylike = self.salike.is_like(request.user.id, activity.ACid)
            activity.alreadylike = True if alreadylike else False
        activity.likenum = activity.AClikeFakeNum or activity.AClikenum
        activity.add('likenum', 'alreadylike')
        return activity

    def fill_type(self, act):
        act.ACtype = activity_type.get(str(act.ACtype))

    def fill_suser(self, obj):
        """给对象添加一个用户字段"""
        obj.suuser = self.suser.get_user_by_user_id(obj.USid)  # 对象的用户
        obj.add('user')
        return obj

    def fill_product(self, act):
        """填充活动商品"""
        # 粉丝页面显示本身价格和店主价, 以及相关商品推荐(规则?)
        prid = act.AClinkvalue
        product = self.sproduct.get_product_by_prid(prid)
        if product:
            prkeeperprice = product.PRprice * (1 - Partner().one_level_divide)
            product.prkeeperprice = ('%.2f' % prkeeperprice)
            prsavemonty = product.PRprice - prkeeperprice
            product.PRprice = ('%.2f' % product.PRprice)
            product.prsavemonty = ('%.2f' % prsavemonty)
            product.add('prkeeperprice', 'prsavemonty', 'prprice')
        act.product = product
        act.add('product')
        return act

    def fill_comment(self, act):
        """给活动对象附加一个评论属性"""
        acid = act.ACid
        act.comment = self.sacomment.get_comment_by_activity_id(acid)
        act.add('comment')
        map(self.fill_comment_apply_for, act.comment)
        return act

    def fill_comment_two(self, act):
        """给活动对象附加一个评论属性"""
        acid = act.ACid
        comments = self.sacomment.get_comment_by_acid_two(acid)
        for comment in comments:
            usid = comment.USid
            user = self.suser.get_user_by_user_id(usid)
            comment.user = user
            comment.add('user').hide('USid')
        act.comment = comments
        act.add('comment')
        # map(self.fill_comment_apply_for, act.comment)
        return act


    def fill_comment_apply_for(self, comment):
        """"如果既是评论又是回复则添加一个'所回复用户'属性"""
        acoid = comment.ACOid
        if not comment.ACOparentid:
            return comment  # 如果ACOid没有值, 说明这不是回复的内容
        comment.parent_apply_user = self.sacomment.get_apply_for_by_acoid(
            acoid)
        comment.add('parent_apply_user')
        return comment


class BaseProductControl():

    def fix_product_list(self, items):
        """调整传入json数据列表,"""
        self.prid_list = []
        for item in items:
            prid = str(uuid.uuid4())  # 生成商品id
            prtarget_items = item.pop("prtarget")  # 每个商品对应多个专题
            self.prid_list.append(prid)
            psvid = str(uuid.uuid4())  # 每一个商品对应一个psv
            image_items = item.pop('images')  # 取出image列表
            sku_items = item.pop('sku')  # 获取sku的key列表, 用于填充至ProductSkuKey
            sku_value = item.get('sku_value')  # 获取sku的value列表
            item['prid'] = prid
            item['suid'] = request.user.id
            image_items = self.fix_image_list(image_items, prid)
            sku_items = self.fix_sku_list(sku_items, prid, psvid)
            productskuvalue = self.fix_sku_value(sku_value, prid, psvid)
            prtarget_items = self.fix_tartget_list(prtarget_items, prid)
            list_add_models('ProductTarget', prtarget_items)
            list_add_models('ProductImage', image_items)
            list_add_models('ProductSkuKey', sku_items)
            if productskuvalue:
                dict_add_models('ProductSkuValue', productskuvalue)
        return items

    def fix_image_list(self, image_items, prid):
        """为每一个image_item添加prid和piid"""
        if not image_items:
            return
        for image_item in image_items:
            image_item['piid'] = str(uuid.uuid4())
            image_item['prid'] = prid
        return image_items

    def fix_tartget_list(self, target_list, prid):
        if not isinstance(target_list, list) or not target_list:
            return []
        if '101' in target_list:
            targer_model_list = [{'prid': prid, 'prtarget': '101', 'ptid': str(uuid.uuid4())}]
        else:
            targer_model_list = [{'prid': prid, 'prtarget': prtarget, 'ptid': str(uuid.uuid4())}
                                 for prtarget in target_list]

        return targer_model_list[:3]

    def fix_sku_list(self, sku_items, prid, psvid):
        """
        sku_items: sku列表
        prid: 商品id
        psvid: 对应的value表id
        功能: 为每一个psk_item添加pskid, prid, psvid"""
        if not sku_items:
            return
        for sku_item in sku_items:
            sku_item['pskid'] = str(uuid.uuid4())
            sku_item['prid'] = prid
            sku_item['psvid'] = psvid
            # psk_key值是一个列表, 元素是个字典, 类似{key: 大小, value: xl}
        return sku_items

    def fix_sku_value(self, sku_value, prid, psvid):
        if not sku_value:
            return
        productskuvalue = {}
        productskuvalue['psvid'] = psvid
        productskuvalue['prid'] = prid
        productskuvalue['psvpropervalue'] = sku_value
        return productskuvalue

    def fill_images(self, product):
        prid = product.PRid
        images_list = self.sproductimage.get_images_by_prid(prid)
        product.images = images_list
        product.add('images')
        return product

    def fill_prtarget(self, product):
        prid = product.PRid
        target_list = [target.PRtarget for target in self.sproduct.get_product_target_by_productid(prid)]
        # if '101' in target_list:
        product.PRtarget = target_list
        return product

    def fill_product_sku_key(self, product):
        prid = product.PRid
        # 该商品的所有skukey
        sku_list = self.sproductskukey.get_psk_by_pid(prid)
        if not sku_list:
            return product
        map(lambda x: x.hide('PRid'), sku_list)
        product.sku = sku_list
        product.add('sku')
        return product

    def fill_product_sku_value(self, product):
        prid = product.PRid
        sku_value = self.sproductskuvalue.get_skvalue_by_prid(prid)
        if not sku_value:
            return
        sku_value.PSVpropervalue = sku_value.PSVpropervalue
        sku_value.hide('PRid')
        product.sku_value = sku_value
        product.add('sku_value')
        return product

    def fill_activity(self, product):
        prid = product.PRid
        activity_list = self.activity.get_activiti_by_prid(prid)
        product.activity = activity_list
        product.add('activity')
        return product

    def trans_product_for_fans(self, product):
        """调整为粉丝版本"""
        # 粉丝页面显示本身价格和店主价, 以及相关商品推荐(规则?)
        prkeeperprice = product.PRprice * (1 - self.partner.one_level_divide)
        product.prkeeperprice = ('%.2f' % prkeeperprice)
        prsavemonty = product.PRprice - prkeeperprice
        product.prsavemonty = ('%.2f' % prsavemonty)
        product.add('prkeeperprice', 'prsavemonty')
        return product

    def trans_product_for_shopkeeper(self, product):
        """调整为店主版本"""
        # 店主页面需要显示赚多少, '买'和'卖'分别省多少和赚多少(10%)
        # 暂定为赚取金额为店主价-普通价格
        # prkeeperprice = product.PRprice * self.partner.one_level_divide
        # # 节省或赚取的价格
        # product.prsavemonty = prkeeperprice
        # product.add('prsavemonty')
        # return product
        # 返回数据一致, 不再区分
        return self.trans_product_for_fans(product)

    def fill_product_nums(self, product):
        prid = product.PRid
        soldnum = product.PRsalefakenum or product.PRsalesvolume  # 显示销量
        viewnum = product.PRfakeviewnum or product.PRviewnum  # 浏览数
        likenum = product.PRfakelikenum or self.sproductlike.get_product_like_num_by_prid(
            prid)  # 收藏(喜欢)数目
        product.prsoldnum = soldnum
        product.prviewnum = viewnum
        product.prlikenum = likenum
        product.add('prsoldnum', 'prlikenum', 'prviewnum')
        return product

    def fill_suser(self, obj):
        """给对象添加一个用户字段"""
        obj.suuser = self.suser.get_user_by_user_id(obj.USid)  # 对象的用户
        obj.add('super')
        return obj

    def fill_super(self, obj):
        """添加一个管理员字段"""
        obj.suuser = self.ssuperuser.get_one_super_by_suid(obj.SUid)  # 超级用户
        obj.add('suuser')
        return obj

    def fill_recommend_nums(self, recommend):
        """日荐页中部浏览数和笑脸数"""
        if hasattr(request, 'user'):
            alreadylike = self.srecommendlike.get_recommend_like_by_usidreid(
                request.user.id, recommend.REid)
            recommend.alreadylike = True if alreadylike else False
        else:
            recommend.alreadylike = False
        viewnum = recommend.REfakeviewnum or recommend.REviewnum  # 浏览数
        likenum = recommend.RElikefakenum or recommend.RElikenum  # 笑脸数
        recommend.reviewnum = viewnum
        recommend.relikenum = likenum
        recommend.add('reviewnum', 'relikenum', 'alreadylike')
        return recommend

    def fill_recommend_product(self, recommend):
        """日荐页中中部商品填充"""
        reid = recommend.REid
        products = self.sproduct.get_product_list_by_reid(reid)
        from WeiDian.service.SRecommend import SRecommend
        for product in products:
            product.rpsort = get_model_return_dict(SRecommend().get_recommendproduct_sort_by_filter({'REid': reid,
                                                                               'PRid': product.PRid}))['RPsort']
            prkeeperprice = product.PRprice * (1 - Partner().one_level_divide)
            product.prkeeperprice = ('%.2f' % prkeeperprice)
            prsavemonty = product.PRprice - prkeeperprice
            product.prsavemonty = ('%.2f' % prsavemonty)
            product.PRprice = ('%.2f' % product.PRprice)
            product.add('prkeeperprice', 'prsavemonty', 'rpsort')
        recommend.products = products
        recommend.add('products')
        return recommend


class BaseShoppingCart(BaseProductControl):

    def fill_sku(self, cart):
        """
        填充选择的sku信息
        """
        pskid = cart.PSKid
        if pskid:
            sku = self.sproductskukey.get_psk_by_pskid(pskid)
            if not sku:
                return cart
            sku.add('PSKproperkey')
            # 价格计算, 合伙人优惠
            cart.PRprice = sku.PSKprice * \
                Partner().one_level_divide if is_partner() else sku.PSKprice
            cart.subtotal = cart.PRprice * cart.SCnums
            cart.current_sku = sku
            cart.add('current_sku', 'subtotal')
        return cart

    def fill_product(self, cart):
        """填充购物车的商品信息"""
        if not hasattr(cart, 'current_sku'):
            return cart
        prid = cart.current_sku.PRid
        if prid:
            product = self.sproduct.get_product_by_prid(prid)

            if product:
                # product
                cart.PRimage = product.PRmainpic
                cart.PRtitle = product.PRtitle
                cart.PRstatus = product.PRstatus
                cart.PRprice = product.PRprice
                sku_key = self.fill_product_sku_key(product)  # 给获得货品的所有skukey值
                # sku
                cart.sku = sku_key.sku
                cart.add('PRimage', 'PRtitle', 'PRstatus', 'PRprice', 'sku')
                # sku_value
                self.fill_product_sku_value(product)
                cart.sku_value = product.sku_value
                cart.add('sku_value')
        return cart

    def total_price(self, cart_list):
        """总金额"""
        # todo modify current_sku
        has_price = filter(
            lambda x: hasattr(
                x,
                'current_sku') and hasattr(
                x.current_sku,
                'PSKprice'),
            cart_list)
        if not has_price:
            return 0
        total = sum([x.current_sku.PSKprice * x.SCnums +
                     x.current_sku.PSKpostfee for x in has_price])
        return total


class BaseActivityCommentControl():

    def fill_user(self, comment):
        """给对象添加一个用户字段"""
        if comment.ACOrobot:
            user = {
                'usname': comment.ACOrobot,
                'robot': 1
            }
        else:
            usid = comment.USid
            user = self.suser.get_user_by_user_id(usid)  # 对象的用户
            user.fill(False, 'robot')
        comment.user = user  # 对象的用户
        comment.add('user').hide('USid')
        return comment

    def fill_comment_apply_for(self, comment):
        """"如果既是评论又是回复则添加一个'所回复用户(这里的用户是管理员)'属性"""
        acoid = comment.ACOid
        comment.add('type')
        if not comment.ACOparentid:
            comment.type = 'comment'
            return comment  # 如果ACOid没有值, 说明这不是回复的内容
        comment.parent_apply_user = self.sactivitycomment.get_apply_for_by_acoid(acoid)
        comment.type = 'apply'
        comment.add('parent_apply_user', 'USid')
        return comment


class BaseMyCenterControl():

    def fill_user_info(self, myinfo):
        usid = myinfo.USid
        user = self.suser.get_user_by_user_id(usid)
        if user.USlevel == 0:
            user.level = 'ordinary'
        if user.USlevel > 0:
            user.level = 'partner'
        user.add('level')
        myinfo.user = user
        myinfo.add('user')
        return myinfo

    def fill_list_userlevel_without_usid(self, f_list):
        """向列表中的每一项填充用户等级显示"""
        user = self.suser.get_user_by_user_id(request.user.id)
        if user.USlevel == 0:
            user.level = 'ordinary'
        if user.USlevel > 0:
            user.level = 'partner'
        for f in f_list:
            user.add('level').hide('USid', 'USname', 'USheader')
            f.user = user
            f.add('user')
        return f_list


class BaseOrder():
    pass


class BaseTask():
    filter_str = '{0}张满{1}-{2}新衣币'
    ratio_str = '佣金上涨{0}%'
    amout_str = '{0}张{1}元无门槛新衣币'

    def fill_task_detail(self, task):
        if task.TUendtime:
            now = datetime.now()
            endtime = datetime.strptime(task.TUendtime, "%Y%m%d%H%M%S")
            if now > endtime:
                return
        if task.TUstatus == 4:
            return
        return self.fill_task_params(task)

    def fill_reward(self, task):
        # 转置为str
        task_raward_list = self.sraward.get_raward_by_tlid(task.TLid)
        if not task_raward_list:
            return
        rawards = []
        for task_raward in task_raward_list:
            raward = self.sraward.get_raward_by_id(task_raward.RAid)
            if raward.RAtype == 0:
                reward_str = self.filter_str.format(int(task_raward.RAnumber), int(raward.RAfilter), int(raward.RAamount))
            elif raward.RAtype == 1 :
                reward_str = self.ratio_str.format(int(raward.RAratio))
                if task_raward.RAnumber == 1:
                    reward_str = "售出首单" + reward_str
            else:
                reward_str = self.amout_str.format(int(task_raward.RAnumber), int(raward.RAamount))
            # raward.RAnumber = task_raward.RAnumber
            #
            # raward.add("RAnumber")

            rawards.append(reward_str)

        if not rawards:
            return

        task.RAward = " + ".join(rawards)
        task.add("RAward")
        return task

    def fill_task_params(self, task):
        task_detail = self.stask.get_task_by_taid(task.TAid)
        if not task_detail or task_detail.TAstatus == 4:
            return
        task.TAname = task_detail.TAname
        task.TAtype = task_detail.TAtype
        task.TAhead = task_detail.TAhead
        task.TLid = task_detail.TLid
        # task.TArole = task_detail.TArole
        # task.TAcomplateNotifications = task_detail.TAcomplateNotifications
        # task.RAid = task_detail.RAid
        task.TAstatus = TASK_STATUS.get(task_detail.TAstatus)
        task.TAmessage = task_detail.TAmessage
        task.TAurl = task_detail.TAurl
        task.TAstartTime = get_web_time_str(task_detail.TAstartTime)
        task.TAduration = task_detail.TAduration
        task.TAendTime = get_web_time_str(task_detail.TAendTime)
        task.add(
            'TAname', "TAtype", "TAhead", "TLid",
            "TAstatus", "TAmessage", "TAurl",
            "TAendTime", "TAstartTime", "TAduration"
        )
        return task


    def do_shoppingtask_or_forwardtask(self, task_type):
        if not re.match(r'^[0-4]$', str(task_type)):
            return
        task_type = int(str(task_type))
        usid = request.user.id
        task_list = self.stask.get_user_task_by_userid(usid)
        task_list = [self.fill_task_detail(_task) for _task in task_list]
        task_list = [_task for _task in task_list if _task]
        for task in task_list:
            if int(task.TAtype) == task_type and int(task.TUstatus) == 0:
                tunumber = int(task.TUnumber) + 1
                tasknumber = int(task.TAurl)
                task_user = {}
                task_user['TUnumber'] = tunumber
                if tunumber == tasknumber:
                    task_user['TUstatus'] = 1

                update_result = self.stask.update_user_task(task.TUid, task_user)
                if not update_result:
                    logger.error('update usertask error user is %s, task is %s', usid, task.TUid)


class BaseFile():

    def upload_file(self, rootdir, notimetag, filepath=None):
        logger.debug('get filetype %s', rootdir)
        from WeiDian.common.timeformat import get_db_time_str
        from WeiDian.config.setting import QRCODEHOSTNAME, LinuxRoot, LinuxImgs, LinuxStaticImgs
        files = request.files.get("file")
        if filepath:
            filepath = os.path.join(LinuxStaticImgs, filepath)
            url = QRCODEHOSTNAME + "/imgs/icon/" + filepath
        else:
            filename = files.filename
            if not isinstance(filename, basestring):
                filename = str(filename)
            filessuffix = filename.split(".")[-1]
            filedir = os.path.join(LinuxRoot, LinuxImgs, rootdir)
            logger.debug('get filedir is %s', filedir)
            if not os.path.isdir(filedir):
                os.mkdir(filedir)
            if not is_admin():
                filename_title = request.user.openid
            else:
                filename_title = request.user.id
            if str(notimetag) == 'true':
                filename = rootdir + filename_title + "." + filessuffix
            else:
                filename = rootdir + filename_title + get_db_time_str() + "." + filessuffix
            filepath = os.path.join(filedir, filename)
            url = QRCODEHOSTNAME + "/imgs/{0}/".format(rootdir) + filename
        print(filepath)
        files.save(filepath)
        return url
