# -*- coding:utf8 -*-
import uuid
import os
from datetime import datetime
from WeiDian.config.response import SYSTEM_ERROR
from flask import request
from WeiDian.common.TransformToList import list_add_models, dict_add_models
from WeiDian.common.divide import Partner
from WeiDian.common.token_required import is_partner
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
            # 'soldnum',
            'remaintime')
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
        prid = act.PRid
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
        for product in products:
            prkeeperprice = product.PRprice * (1 - Partner().one_level_divide)
            product.prkeeperprice = ('%.2f' % prkeeperprice)
            prsavemonty = product.PRprice - prkeeperprice
            product.prsavemonty = ('%.2f' % prsavemonty)
            product.PRprice = ('%.2f' % product.PRprice)
            product.add('prkeeperprice', 'prsavemonty')
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
            cart.sku = sku
            cart.add('sku', 'subtotal')
        return cart

    def fill_product(self, cart):
        """填充购物车的商品信息"""
        if not hasattr(cart, 'sku'):
            return cart
        prid = cart.sku.PRid
        if prid:
            product = self.sproduct.get_product_by_prid(prid)
            if product:
                cart.PRimage = product.PRmainpic
                cart.PRtitle = product.PRtitle
                cart.PRstatus = product.PRstatus
                product = self.fill_product_sku_key(product)  # 给获得货品的所有skukey值
                cart.sku_total = product.sku
                cart.add('PRimage', 'PRtitle', 'PRstatus', 'sku_total')
        return cart

    def total_price(self, cart_list):
        """总金额"""
        has_price = filter(
            lambda x: hasattr(
                x,
                'sku') and hasattr(
                x.sku,
                'PSKprice'),
            cart_list)
        if not has_price:
            return 0
        total = sum([x.sku.PSKprice * x.SCnums +
                     x.sku.PSKpostfee for x in has_price])
        return total


class BaseActivityCommentControl():

    def fill_user(self, comment):
        """给对象添加一个用户字段"""
        usid = comment.USid
        comment.user = self.suser.get_user_by_user_id(usid)  # 对象的用户
        comment.add('user').hide('USid')
        return comment

    def fill_comment_apply_for(self, comment):
        """"如果既是评论又是回复则添加一个'所回复用户'属性"""
        acoid = comment.ACOid
        comment.add('type')
        if not comment.ACOparentid:
            comment.type = 'comment'
            return comment  # 如果ACOid没有值, 说明这不是回复的内容
        comment.parent_apply_user = self.sactivitycomment.get_apply_for_by_acoid(
            acoid)
        comment.type = 'apply'
        comment.add('parent_apply_user')
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

    def fill_task_detail(self, task):
        if task.TUendtime:
            now = datetime.now()
            endtime = datetime.strptime(task.TUendtime, "%Y%m%d%H%M%S")
            if now > endtime:
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
            raward.RAnumber = task_raward.RAnumber
            raward.add("RAnumber")
            rawards.append(raward)

        if not rawards:
            return

        task.RAward = rawards
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


class BaseFile():

    def upload_file(self, rootdir):
        from WeiDian.common.timeformat import get_db_time_str
        from WeiDian.config.setting import QRCODEHOSTNAME, LinuxRoot, LinuxImgs
        files = request.files.get("file")
        filessuffix = str(files.filename).split(".")[-1]
        filedir = os.path.join(LinuxRoot, LinuxImgs, rootdir)
        if not os.path.isdir:
            os.mkdir(filedir)

        filename = rootdir + request.user.openid + get_db_time_str() + "." + filessuffix
        filepath = os.path.join(filedir, filename)
        print(filepath)
        files.save(filepath)
        url = QRCODEHOSTNAME + "/imgs/{0}/".format(rootdir) + filename
        return url
