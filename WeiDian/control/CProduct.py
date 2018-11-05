# *- coding:utf8 *-
import sys
import os

from WeiDian.config.enums import activity_edit_status
from WeiDian.models.model import ProductTarget
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
from WeiDian.common.timeformat import get_db_time_str, get_web_time_str
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
        from WeiDian.control.Cuser import CUser
        self.cuser = CUser()
        from WeiDian.service.SBigActivity import SBigActivity
        self.sbigactivity = SBigActivity()
        from WeiDian.service.STopNav import STopNav
        self.stopnav = STopNav()
        from WeiDian.service.SOrder import SOrder
        self.sorder = SOrder()
        from WeiDian.service.SSuperUser import SSuperUser
        self.ssuperuser = SSuperUser()
        self.empty = ['', [], {}, None]
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
            'PRbaid'
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

    @verify_token_decorator
    def get_product_pools(self):
        """后台获取商品池列表内容"""
        if not is_admin():
            raise AUTHORITY_ERROR(u'请使用管理员账号重新登录')
        args = request.args.to_dict()
        logger.debug("Get Commodity Pools data is %s", args)
        page, count = self.cuser.get_pagesize_pagenum(args)
        time_start = args.get('time_start')
        if time_start:
            time_start = get_db_time_str(time_start)
        time_end = args.get('time_end')
        if time_end:
            time_end = get_db_time_str(time_end)
        status = args.get('status')
        kw = args.get('kw')
        if kw not in self.empty:
            kw = kw.encode('utf8')
        isdelete = args.get('isdelete', 0)  # 0  or  1
        if str(isdelete) == '0':
            isdelete = False
        elif str(isdelete) == '1':
            isdelete = True
        else:
            isdelete = None
        product_list = self.sproduct.get_product_filter(kw, time_start, time_end, isdelete, status, page, count)
        for product in product_list:
            self.sproduct.update_view_num(product.PRid)
            self.fill_prbaid(product)
            self.fill_prtarget(product)
            if product.PRcreatetime:
                prcreatetime = get_web_time_str(product.PRcreatetime)
                product.fill(prcreatetime, 'prcreatetime')
            if product.SUmodifyid:
                isclaim = True
                canclaim = True if product.SUmodifyid == request.user.id else False
                caneditact = True if product.SUmodifyid == request.user.id else False
            else:
                isclaim = False
                canclaim = True
                caneditact = False
            product.fill(product.SUmodifyid or '', "claimid")
            product.fill(isclaim, "isclaim")
            product.fill(canclaim, "canclaim")
            product.fill(caneditact, "caneditact")
            isbig = False
            if product.PRtarget:
                isbig = True if product.PRtarget[0] == '101' else False
            product.fill(isbig, 'isbig')
            pv = product.PRviewnum
            product.fill(pv, 'pv')
            salesvolume = product.PRsalesvolume
            transform = 0 if pv == 0 else salesvolume / float(pv)
            ortransform = "%.2f%%" % (transform * 100)
            product.fill(ortransform, 'ortransform')
            refund_list = self.sorder.get_refund_product()
            redfund_num = 0
            if refund_list:
                for refund in refund_list:
                    refund_product = self.sorder.get_orderproductinfo_by_opiid(refund.OPIid)
                    if refund_product:
                        redfund_num = redfund_num + refund_product.OPIproductnum
            refundrate_f = 0 if salesvolume == 0 else redfund_num / float(salesvolume)
            refundrate = "%.2f%%" % (refundrate_f * 100)
            product.fill(refundrate, 'refundrate')
            product.fill(product.prbaid, 'prbaid')
            product.fill(product.PRstatus, 'prstatus')
            activitystatus = 0
            acid = None
            ac_list = self.sactivity.get_acid_by_filterid(
                {'AClinkvalue': product.PRid, 'ACSkipType': 2, 'ACisdelete': False})
            if ac_list not in self.empty:
                for act in ac_list:
                    temp_num = -1 if act.ACeditstatus is None else act.ACeditstatus
                    activitystatus = temp_num + 1
                    acid = act.ACid
            zh_activitystatus = activity_edit_status.get(str(activitystatus))
            product.fill(activitystatus, 'activitystatus')
            product.fill(zh_activitystatus, 'zh_activitystatus')
            product.fill(acid, 'acid')
        data = import_status('get_product_list_success', 'OK')
        data['data'] = product_list
        data["count"] = request.all_count
        data["page_count"] = request.page_count
        return data

    @verify_token_decorator
    def update_sku_price(self):
        """更新sku里的售价/进价/利润"""
        if not is_admin():
            raise AUTHORITY_ERROR(u'请使用管理员账号重新登录')
        data = request.json
        pskid = data.get('pskid')
        parameter_required('pskid')
        logger.debug("update sku price data is %s", data)
        sku_info = self.sproductskukey.get_psk_by_pskid(pskid)
        if not sku_info:
            raise NOT_FOUND(u'没有找到相应的sku')
        price_dict = {
            "PSKprice": data.get('pskprice'),
            "PSKprofict": data.get('pskprofict'),
            "PSKpurchase": data.get('pskpurchase')
        }
        price_dict = {k: v for k, v in price_dict.items() if v not in self.empty}
        if price_dict not in self.empty:
            up_info = self.sproductskukey.update_sku_price_by_filter({'PSKid': pskid}, price_dict)
            if not up_info:
                raise SYSTEM_ERROR(u'更新数据错误')
        # 操作日志
        operation_dict = {"PSKprice": u'更新售价',
                          "PSKprofict": u'更新利润',
                          "PSKpurchase": u'更新进货价'
                          }
        if price_dict not in self.empty:
            for i in price_dict.keys():
                self.__make_product_recording(sku_info.PRid, sku_info.PSskuid, operation_dict[i])
        response = import_status("update_success", "OK")
        response['data'] = {'pskid': pskid}
        return response

    @verify_token_decorator
    def shelf_product_and_claim_act(self):
        """商品上下架/删除商品/推文认领"""
        if not is_admin():
            raise AUTHORITY_ERROR(u'请使用管理员账号重新登录')
        data = request.json
        logger.debug("shelf product and claim act data is %s", data)
        prid = data.get('prid')
        parameter_required('prid')
        shelf = data.get('shelf')  # 0 下架 1 上架
        claim = data.get('claim')  # 0 取消认领 1 认领推文
        prdel = data.get('prdel')  # 1 删除
        modifyid = None
        if shelf not in self.empty and claim not in self.empty:
            raise PARAMS_MISS(u'参数错误，只能进行一项操作')
        pr_info = self.sproduct.get_product_by_prid(prid)
        if not pr_info:
            raise NOT_FOUND(u'无该商品信息')
        if pr_info.PRisdelete == True:
            raise NOT_FOUND(u'数据错误，该商品已被删除')
        if shelf not in self.empty:
            if not re.match(r'^[0-1]$', str(shelf)):
                raise PARAMS_MISS(u'shelf, 参数异常')
            if pr_info.PRstatus == int(shelf):
                raise SYSTEM_ERROR(u'已完成上/下架操作')
            upinfo = self.sproduct.update_product_info_by_filter(
                    {'PRid': prid},
                    {'PRmodifytime': get_db_time_str(),
                     'PRstatus': int(shelf)
                     })
            if not upinfo:
                raise SYSTEM_ERROR(u'更新数据错误')
            # 操作日志
            shelf_operation = u'上架商品' if str(shelf) == '1' else u'下架商品'
            self.__make_product_recording(prid, prid, shelf_operation)
        if claim not in self.empty:
            if not re.match(r'^[0-1]$', str(claim)):
                raise PARAMS_MISS(u'claim, 参数异常')
            if pr_info.SUmodifyid:
                if pr_info.SUmodifyid != request.user.id:
                    raise SYSTEM_ERROR(u'该推文已被其他运营认领')
                else:
                    if str(claim) == '1':
                        raise SYSTEM_ERROR(u'您已完成认领')
            else:
                if str(claim) == '0':
                    raise SYSTEM_ERROR(u'您没有认领该商品的关联推文，不能进行解除操作')
            modifyid = request.user.id if str(claim) == '1' else None
            upinfo = self.sproduct.update_product_info_by_filter(
                    {'PRid': prid},
                    {'PRmodifytime': get_db_time_str(),
                     'SUmodifyid': modifyid
                     })
            if not upinfo:
                raise SYSTEM_ERROR(u'更新数据错误')
            # 操作日志
            operation = u'认领推文' if str(claim) == '1' else u'解除推文认领'
            self.__make_product_recording(prid, prid, operation)
        if prdel not in self.empty:
            if str(prdel) == '1':
                update_result = self.sproduct.update_product_info_by_filter({'PRid': prid}, {
                    "PRisdelete": True, 'PRmodifytime': get_db_time_str()})
                if not update_result:
                    raise SYSTEM_ERROR(u'删除数据错误')
                # 操作日志
                self.__make_product_recording(prid, prid, u'删除商品')
        response = import_status("update_success", "OK")
        response['data'] = {'prid': prid,
                            'claimid': modifyid or ''}
        return response

    @verify_token_decorator
    def get_product_operation_record(self):
        """获取商品操作记录"""
        if not is_admin():
            raise AUTHORITY_ERROR(u'请使用管理员账号重新登录')
        args = request.args.to_dict()
        prid = args.get('prid')
        page_num, page_size = self.cuser.get_pagesize_pagenum(args)
        record_list = self.sproduct.get_product_operation_record(page_num, page_size, prid)
        if record_list:
            for record in record_list:
                portarget = record.PRid if not record.PORtarget else record.PORtarget
                record.PORcreatetime = get_web_time_str(record.PORcreatetime)
                suser = self.ssuperuser.get_one_super_by_suid(record.SUid)
                suname = suser.SUname if suser else ''
                record.fill(suname, 'suname')
                record.fill(portarget, 'portarget')
        response = import_status("messages_get_item_ok", "OK")
        response['data'] = record_list
        response['page_count'] = request.page_count
        response['count'] = request.all_count
        return response

    @verify_token_decorator
    def update_product_relate_prtarget(self):
        """商品池修改商品与模块的关联"""
        if not is_admin():
            raise AUTHORITY_ERROR(u'请使用管理员账号重新登录')
        data = request.json
        logger.debug("update product relate prtarget data is %s", data)
        prid = data.get('prid')
        prtargets = data.get('prtarget')
        if prtargets:
            if len(prtargets) > 3:
                raise SYSTEM_ERROR(u'每个商品最多只能关联三个模块')
            ptid = str(uuid.uuid1())
            if '101' in prtargets:
                del_info = self.sproduct.del_product_target_by_filter({"PRid": prid})
                logger.debug("del prtarget relation success before add operation, del count: %s", del_info)
                self.sproduct.add_model("ProductTarget", ** {
                    'PTid': ptid,
                    'PRid': prid,
                    'PRtarget': '101'
                })
                # 操作记录
                self.__make_product_recording(prid, prid, u'更改为大礼包商品')
            else:
                topnav_list = self.stopnav.get_all_tnid()
                tnid_list = []
                [tnid_list.append(topnav.TNid) for topnav in topnav_list]
                with self.sproduct.auto_commit() as session:
                    model_beans = []
                    for targetid in prtargets:
                        if str(targetid) not in tnid_list:
                            raise PARAMS_MISS(u'prtarget参数错误，未找到要关联的模块')
                        prtarget_dict = dict(
                            PTid=str(uuid.uuid4()),
                            PRid=prid,
                            PRtarget=targetid
                        )
                        prtarget_info = ProductTarget.create(prtarget_dict)
                        model_beans.append(prtarget_info)
                        # 操作记录
                        self.__make_product_recording(prid, targetid, u'更改模块关联')
                    session.query(ProductTarget).filter(ProductTarget.PRid == prid).delete()
                    session.add_all(model_beans)
        elif prtargets == []:
            # 操作记录
            try:
                target_info = self.sproduct.get_product_target_by_prid(prid)
                if target_info:
                    for tgid in target_info:
                        self.__make_product_recording(prid, tgid.PRtarget, u'解除模块关联')
            except Exception as e:
                logger.exception("not found prtargetid ,error is %s", e)
                self.__make_product_recording(prid, prid, u'解除模块关联')
            del_info = self.sproduct.del_product_target_by_filter({"PRid": prid})
            logger.debug("del prtarget relation success this is none list: %s", del_info)
        response = import_status("update_success", "OK")
        response['data'] = {'prid': prid}
        return response

    @verify_token_decorator
    def get_product_relate_bigactivity(self):
        """商品池获取商品与专题的关联详情"""
        if not is_admin():
            raise AUTHORITY_ERROR(u'请使用管理员账号重新登录')
        prid = request.args.to_dict().get('prid')
        parameter_required('prid')
        logger.debug("get product relate bigactivity PRID is %s", prid)
        prbaids = self.sproduct.get_product_baid_by_prid(prid)
        list_baid = []
        suid = ''
        suname = u'批量导入'
        updatetime = ''
        for prbaid in prbaids:
            record_info = self.sproduct.get_singel_record_by_filter({'PRid': prid, 'PORtarget': prbaid.BAid})
            if record_info:
                suid = record_info.SUid
                suser_info = self.ssuperuser.get_one_super_by_suid(suid)
                suname = suser_info.SUname if suser_info else ''
                updatetime = get_web_time_str(record_info.PORcreatetime)
            dict_baid = {
                'pbid': prbaid.PBid,
                'baid': prbaid.BAid,
                'claimid': suid,
                'clainname': suname,
                'updatetime': updatetime
            }
            list_baid.append(dict_baid)
        response = import_status("messages_get_item_ok", "OK")
        response['data'] = list_baid
        return response

    @verify_token_decorator
    def update_product_relate_bigactivity(self):
        """商品池修改商品与专题的关联"""
        if not is_admin():
            raise AUTHORITY_ERROR(u'请使用管理员账号重新登录')
        data = request.json
        logger.debug("update product relate bigactivity data is %s", data)
        pbid = data.get('pbid')
        baid = data.get('baid')
        prid = data.get('prid')
        option = data.get('option')
        if not re.match(r'^[0-2]$', str(option)):
            raise PARAMS_MISS(u'option 参数异常')
        if baid == '':
            raise PARAMS_MISS(u'baid 参数异常')
        elif baid not in self.empty:
            bigact = self.sbigactivity.get_one_big_act(baid)
            if not bigact:
                raise NOT_FOUND(u'输入的关联专题不存在')
        if prid == '':
            raise PARAMS_MISS(u'prid 参数异常')
        elif prid not in self.empty:
            product = self.sproduct.get_product_by_prid(prid)
            if not product:
                raise NOT_FOUND(u'商品信息不存在')
        if str(option) == '0':  # 0 删除
            parameter_required('pbid')
            # 操作记录
            pbinfo = self.sproduct.get_single_productbigactivity_by_filter({'PBid': pbid})
            if pbinfo:
                self.__make_product_recording(pbinfo.PRid, pbinfo.BAid, u'解除专题关联')
            del_info = self.sproduct.del_productbigactivity_by_filter({'PBid': pbid})
            if not del_info:
                raise NOT_FOUND(u'错误，未找到要删除的关联专题')
        elif str(option) == '1':  # 1 添加
            parameter_required('prid', 'baid')
            prbaid_list = self.sproduct.get_product_baid_by_prid(prid)
            if prbaid_list:
                logger.debug("exist prbaid count is %s", len(prbaid_list))
                if len(prbaid_list) >= 3:
                    raise SYSTEM_ERROR(u'每个商品最多只能关联三个专题')
                for prbaid in prbaid_list:
                    if baid == prbaid.BAid:
                        raise SYSTEM_ERROR(u'已与此专题进行过关联')
            pbid = str(uuid.uuid1())
            self.sproduct.add_model('ProductBigActivity', **{
                'PBid': pbid,
                'PRid': prid,
                'BAid': baid
                })
            # 操作记录
            self.__make_product_recording(prid, baid, u'添加专题关联')
        elif str(option) == '2':  # 2 修改
            parameter_required('pbid', 'baid')
            pbact = self.sproduct.update_productbigactivity_by_filter({'PBid': pbid}, {'BAid': baid})
            if not pbact:
                raise NOT_FOUND(u'修改失败')
            # 操作记录
            pbinfo = self.sproduct.get_single_productbigactivity_by_filter({'PBid': pbid})
            if pbinfo:
                self.__make_product_recording(pbinfo.PRid, baid, u'修改专题关联')
        response = import_status("update_success", "OK")
        response['data'] = {'pbid': pbid}
        return response

    def get_product_list(self):
        args = request.args.to_dict()
        logger.debug("get product list args is %s", args)
        page = int(args.get('page_num', 1))  # 页码
        count = int(args.get('page_size', 15))  # 取出条数
        kw = args.get('kw')
        if kw not in ['', None]:
            kw = kw.encode('utf8')
        status = args.get('status')
        status = 1 if status in self.empty else int(status)
        try:
            isdelete = int(args.get('isdelete'))  # 0  or  1
            isdelete = False if isdelete else True
        except Exception as e:
            isdelete = None
        product_list = self.sproduct.get_product_filter(kw, isdelete, status, page, count)
        for product in product_list:
            self.sproduct.update_view_num(product.PRid)
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
        self.fill_prbaid(product)
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

    def __make_product_recording(self, prid, portarget, poraction):
        """创建商品操作记录"""
        self.sproduct.add_model('ProductOperationRecord', **{
            'PORid': str(uuid.uuid1()),
            'PRid': prid,
            'PORcreatetime': get_db_time_str(),
            'SUid': request.user.id,
            'PORtarget': portarget,
            'PORaction': poraction
        })
