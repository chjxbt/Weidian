# *- coding:utf8 *-
import sys
import os
from flask import request
import re
import json
import uuid
from WeiDian import logger
from WeiDian.common.params_require import parameter_required
from WeiDian.common.token_required import verify_token_decorator, is_admin, is_tourist, is_ordirnaryuser, is_customerservice
from WeiDian.common.TransformToList import list_add_models
from WeiDian.common.import_status import import_status
from WeiDian.common.divide import Partner
from WeiDian.common.timeformat import get_db_time_str
from WeiDian.config.response import TOKEN_ERROR, AUTHORITY_ERROR, PARAMS_MISS, SYSTEM_ERROR, NOT_FOUND
from WeiDian.control.BaseControl import BaseProductControl
sys.path.append(os.path.dirname(os.getcwd()))


class CProduct(BaseProductControl):
    def __init__(self):
        from WeiDian.service.SProduct import SProduct
        self.sproduct = SProduct()
        from WeiDian.service.SProductSkuValue import SProductSkuValue
        self.sproductskuvalue = SProductSkuValue()
        from WeiDian.service.SProductImage import SProductImage
        self.sproductimage = SProductImage()
        from WeiDian.service.SProductSkuKey import SProductSkuKey
        self.sproductskukey = SProductSkuKey()
        from WeiDian.service.SActivity import SActivity
        self.sactivity = SActivity()
        from WeiDian.service.SProductLike import SProductLike
        self.sproductlike = SProductLike()
        # 后续修改
        self.partner = Partner()
        self.update_sku_params = ['PRid', "PSVid", 'PSKproductnum',
                                  'PSKalias', 'PSKprice', 'PSKpostfee', 'PSKactiviyid', 'PSKproperkey', "PSisdelete"]

        self.update_product_params = [
            'PRmainpic',
            'PRdetail',
            'PRimporturl',
            'PRishot',
            'PRtitle',
            'PRname',
            'Maketlias',
            'PRalias',
            'PRprice',
            'PReditstate',
            'PRsalesvolume',
            'PRoldprice',
            'PRchannelname',
            'PRvipprice',
            'PRlogisticsfee',
            'PRchannelid',
            'SUid',
            'PRstock',
            'PRsalestatus',
            'PRishhare',
            'PRtarget',
            'PRviewnum',
            'PRfakeviewnum',
            'PRfakelikenum',
            'PRsalefakenum',
        ]

    @verify_token_decorator
    def add_product_list(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if not is_admin():
            return AUTHORITY_ERROR  # 权限不足
        json_data = request.json
        product_list = json_data.get('products')
        logger.debug('get product list %s', product_list)
        product_list = self.fix_product_list(product_list)
        list_add_models('Product', product_list)
        data = import_status('add_product_list_success', 'OK')
        data['data'] = {'prid': self.prid_list}
        return data

    # 删除商品
    @verify_token_decorator
    def delete_product(self):
        if not is_admin():
            return AUTHORITY_ERROR(u'权限不足')
        data = parameter_required('productid')
        logger.debug('get delete_product data %s', data)
        product = self.sproduct.get_product_by_productid(data.get('productid'))
        if not product:
            return import_status('no_product', 'OK')

        update_result = self.sproduct.update_product_by_productid(data.get('productid'), {
            "PRisdelete": True, 'PRmodifytime': get_db_time_str()})
        if not update_result:
            raise SYSTEM_ERROR(u'服务器繁忙')
        return import_status('delete_product_success', 'OK')

    # 上下架商品
    @verify_token_decorator
    def shelves_product(self):
        """状态改成0 上架  1下架"""
        if not is_admin():
            return AUTHORITY_ERROR(u'权限不足')
        data = parameter_required('productid')
        prstatus = data.get("prstatus", 1)
        logger.debug('get prestatus. %s', prstatus)
        logger.debug('get productid. %s', data.get('productid'))
        if not re.match(r'^[0-2]$', str(prstatus)):
            raise PARAMS_MISS(u'prstatus, 参数异常')
        prstatus = int(prstatus)
        prstatus = 0 if int(prstatus) else 1
        product = self.sproduct.get_product_by_productid(data.get('productid'))
        logger.debug('get product %s', product)
        if not product and prstatus != 1:
            return import_status('no_product', 'OK')
        update_result = self.sproduct.update_product_by_productid(data.get('productid'), {
            "PRstatus": prstatus, 'PRmodifytime': get_db_time_str()})
        if not update_result:
            raise SYSTEM_ERROR(u'服务器繁忙')
        return import_status('update_product_success', 'OK')

    # 更新sku
    @verify_token_decorator
    def update_sku(self):
        if not is_admin():
            return AUTHORITY_ERROR(u'权限不足')
        data = parameter_required('psskuid', 'productid')
        logger.debug('get update_sku data %s', data)
        pskpropervalue = data.get('pskpropervalue')
        skukey = {}
        product = self.sproduct.get_product_by_productid(data.get('productid'))
        if not product:
            return import_status('no_product', 'OK')

        for key in self.update_sku_params:
            if not data.get(key.lower()) and data.get(key.lower()) != 0:
                continue
            skukey[key] = data.get(key.lower())

        if skukey.get("PSKproperkey"):
            skukey['_PSKproperkey'] = json.dumps(skukey.pop('PSKproperkey'))

        productsku = self.sproductskukey.get_psk_by_psskuid(data.get("psskuid"), product.PRid)
        if not productsku:
            psv = self.sproductskuvalue.get_skvalue_by_prid(product.PRid)
            skukey['PSKid'] = str(uuid.uuid1())
            skukey['PRid'] = product.PRid
            skukey['PSVid'] = psv.PSVid
            skukey['PSskuid'] = data.get("psskuid")
            self.sproductskukey.add_model("ProductSkuKey", **skukey)
        else:
            update_result = self.sproductskukey.update_product_sku(data.get("psskuid"), product.PRid, skukey)
            if not update_result:
                raise SYSTEM_ERROR(u'服务器繁忙')

        if pskpropervalue and product:
            update_result = self.sproductskuvalue.update_skuvalue(product.PRid, {"_PSVpropervalue": json.dumps(pskpropervalue)})
            if not update_result:
                raise SYSTEM_ERROR(u'服务器繁忙')
        return import_status('update_product_sku_success', 'OK')

    # 更新商品
    @verify_token_decorator
    def update_product(self):
        if not is_admin():
            raise AUTHORITY_ERROR(u'权限不足')

        data = parameter_required('productid')
        logger.debug('get update_product data %s', data)
        productid = data.get('productid')
        product = self.sproduct.get_product_by_productid(productid)
        if not product:
            return import_status('no_product', 'OK')
        product = {}
        for key in self.update_product_params:
            if not data.get(key.lower()) and data.get(key.lower()) != 0:
                continue
            product[key] = data.get(key.lower())
        product['PRmodifytime'] = get_db_time_str()
        update_result = self.sproduct.update_product_by_productid(productid, product)
        if not update_result:
            raise SYSTEM_ERROR(u'服务器繁忙')

        return import_status('update_product_success', 'OK')

    # 更新商品
    @verify_token_decorator
    def update_product_image(self):
        if not is_admin():
            raise AUTHORITY_ERROR(u'权限不足')

        data = parameter_required('productid', 'images')
        logger.debug('get update_product_image data %s', data)
        product = self.sproduct.get_product_by_productid(data.get("productid"))
        if not product:
            raise PARAMS_MISS(u"商品不存在或已删除")
        # for image in data.get("images"):
        #     primage = self.sproductimage.get_images_by_prid_pisort(product.PRid, image.get('pisort', 0))
        #     if primage:
        #         update_result = self.sproductimage.update_image(
        #             primage.PIid, {"PIurl": image.get("piurl"), "PIexist": image.get("piexist", 1)})
        #         if not update_result:
        #             logger.error('update product image error, sort is %s', image.get("pisort", 0))
        #             raise SYSTEM_ERROR(u"数据库异常")
        #     else:
        #         self.sproductimage.add_model("ProductImage", **{
        #             "PIid": str(uuid.uuid1()),
        #             "PRid": product.PRid,
        #             "PIurl": image.get("piurl"),
        #             "PIsort": image.get("pisort", 0),
        #             "PIexist": image.get("piexist", 1),
        #         })
        self.sproductimage.update_image_by_prid(product.PRid, {"PIexist": 0})
        for image in data.get('images'):
            self.sproductimage.add_model("ProductImage", **{
                "PIid": str(uuid.uuid1()),
                "PRid": product.PRid,
                "PIurl": image.get("piurl"),
                "PIsort": image.get("pisort", 0),
                "PIexist": image.get("piexist", 1),
            })

        return import_status('update_product_image_success', 'OK')

    def get_product_list(self):
        args = request.args.to_dict()
        logger.debug("get product list args is %s", args)
        page = int(args.get('page_num', 1))  # 页码
        count = int(args.get('page_size', 15))  # 取出条数
        kw = args.get('kw')
        if kw not in ['', None]:
            kw = kw.encode('utf8')
        status = args.get('status')
        try:
            isdelete = int(args.get('isdelete'))  # 0  or  1
            isdelete = False if isdelete else True
        except Exception as e:
            isdelete = None
        product_list = self.sproduct.get_product_filter(kw, isdelete, status, page, count)
        data = import_status('get_product_list_success', 'OK')
        data['data'] = product_list
        data["count"] = request.all_count
        data["page_count"] = request.page_count
        return data

    @verify_token_decorator
    def get_product_one(self):
        logger.info(request.detail)
        args = request.args.to_dict()
        prid = args.get('prid')
        if is_tourist():
            usid = None
        else:
            usid = request.user.id
        if not prid:
            raise PARAMS_MISS()
        product = self.sproduct.get_product_by_prid(prid)
        if not product:
            raise NOT_FOUND(u'无此商品')
        # 是管理员或客服则显示全部信息
        if is_admin() or is_customerservice():
            product.fields = product.all
            print '是管理员或客服'
        else:
            # 如果是游客, 或者是未购买开店大礼包的普通用户
            if is_tourist() or is_ordirnaryuser():
                print '是游客或者普通用户'
                product = self.trans_product_for_fans(product)
            else:  # 合伙人(即已购买开店大礼包的用户)
                print '合伙人'
                product = self.trans_product_for_shopkeeper(product)
            product = self.fill_product_nums(product)
        # 填充一些都需要的信息
        self.fill_product_alreadylike(product, usid)
        self.fill_images(product)
        self.fill_prtarget(product)
        self.fill_product_sku_key(product)
        self.fill_product_sku_value(product)
        self.sproduct.update_view_num(prid)
        data = import_status('get_product_success', 'OK')
        data['data'] = product
        return data

    @verify_token_decorator
    def get_one_by_productid(self):
        logger.info(request.detail)
        args = request.args.to_dict()
        prid = args.get('productid')
        usid = request.user.id
        if not prid:
            raise PARAMS_MISS()
        product = self.sproduct.get_product_by_productid(prid)
        if not product:
            raise NOT_FOUND(u"无此商品")
        # 是管理员或客服则显示全部信息
        if is_admin() or is_customerservice():
            product.fields = product.all
            print '是管理员或客服'
        else:
            # 如果是游客, 或者是未购买开店大礼包的普通用户
            if is_tourist() or is_ordirnaryuser():
                print '是游客或者普通用户'
                product = self.trans_product_for_fans(product)
            else:  # 合伙人(即已购买开店大礼包的用户)
                print '合伙人'
                product = self.trans_product_for_shopkeeper(product)
            product = self.fill_product_nums(product)
        # 填充一些都需要的信息
        self.fill_product_alreadylike(product, usid)
        self.fill_images(product)
        self.fill_prtarget(product)
        self.fill_product_sku_key(product)
        self.fill_product_sku_value(product)
        self.sproduct.update_view_num(product.PRid)
        data = import_status('get_product_success', 'OK')
        data['data'] = product
        return data