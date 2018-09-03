# *- coding:utf8 *-
import sys
import os
from flask import request
from WeiDian.common.token_required import verify_token_decorator, is_admin, is_tourist, is_ordirnaryuser, is_customerservice
from WeiDian.common.TransformToList import list_add_models
from WeiDian.common.import_status import import_status
from WeiDian.common.divide import Partner
from WeiDian.config.response import TOKEN_ERROR, AUTHORITY_ERROR, PARAMS_MISS, SYSTEM_ERROR
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

    @verify_token_decorator
    def add_product_list(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        if not is_admin():
            return AUTHORITY_ERROR  # 权限不足
        json_data = request.json
        product_list = json_data.get('products')
        product_list = self.fix_product_list(product_list)
        list_add_models('Product', product_list)
        data = import_status('add_product_list_success', 'OK')
        data['data'] = {'prid': self.prid_list}
        return data

    def get_product_list(self):
        args = request.args.to_dict()
        page = int(args.get('page', 1))  # 页码
        start = int(args.get('start', 0))  # 起始位置
        count = int(args.get('count', 15))  # 取出条数
        if not start:
            start = (page -1) * count
        product_list = self.sproduct.get_all()
        len_product_list = len(product_list)
        if count > 30:
            count = 30
        end = start + count
        if end > len_product_list:
            end = len_product_list
        product_list = product_list[start: end]
        print start, end
        data = import_status('get_product_list_success', 'OK')
        data['data'] = product_list
        return data

    @verify_token_decorator
    def get_product_one(self):
        args = request.args.to_dict()
        prid = args.get('prid')
        if not prid:
            return PARAMS_MISS
        product = self.sproduct.get_product_by_prid(prid)
        if not product:
            return SYSTEM_ERROR
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
        self.fill_images(product)
        self.fill_product_sku_key(product)
        self.fill_product_sku_value(product)
        self.sproduct.update_view_num(prid)
        data = import_status('get_product_success', 'OK')
        data['data'] = product
        return data

