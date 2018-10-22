# -*- coding:utf8 -*-
import re
import sys
import os
import uuid

from WeiDian.config.enums import REWARD_TYPE
from flask import request
from WeiDian import logger
from datetime import datetime, timedelta
from WeiDian.common.params_require import parameter_required
from WeiDian.common.import_status import import_status
from WeiDian.common.timeformat import get_db_time_str, get_web_time_str, format_for_web_second, format_for_db
from WeiDian.common.token_required import verify_token_decorator, is_admin, is_tourist
from WeiDian.config.response import TOKEN_ERROR, AUTHORITY_ERROR, SYSTEM_ERROR, NOT_FOUND, PARAMS_ERROR, \
    PARAMS_REDUNDANCE

sys.path.append(os.path.dirname(os.getcwd()))

class CRaward():
    def __init__(self):
        from WeiDian.service.SRaward import SRaward
        self.sraward = SRaward()


    @verify_token_decorator
    def create_reward(self):
        """创建优惠券"""
        if not is_admin():
            raise AUTHORITY_ERROR(u'当前账号权限不足')
        data = request.json
        logger.debug("create reward data is %s", data)
        parameter_required('ratype', 'raname')
        raid = str(uuid.uuid1())
        ratype = data.get('ratype')
        if not re.match(r'^[0-4]$', str(ratype)):
            raise PARAMS_ERROR(u'ratype, 参数异常')
        now_time = get_db_time_str()
        nowtime_str_to_time = datetime.strptime(now_time, format_for_db)
        days_later = datetime.strftime(nowtime_str_to_time + timedelta(days=30), format_for_web_second)
        reendtime = get_db_time_str(data.get('raendtime', days_later))
        ratransfer = data.get('ratransfer', False)
        reward_dict = {
            'RAid': raid,
            'RAtype': ratype,
            'RAmaxusenum': data.get('ramaxusenum', 1),
            'RAmaxholdnum': data.get('ramaxholdnum', 1),
            'RAendtime': reendtime,
            'RAname': data.get('raname'),
            'RAtransfer': ratransfer,
        }
        if re.match(r'^[0-2]$', str(ratype)):
            if str(ratype) == '0':
                logger.info('This reward type 0 is created')
                reward_dict['RAfilter'] = data.get('rafilter')
                reward_dict['RAamount'] = data.get('raamount')
            elif str(ratype) == '1':
                logger.info('This reward type 1 is created')
                reward_dict['RAratio'] = data.get('raratio')
            else:
                logger.info('This reward type 2 is created')
                reward_dict['RAfilter'] = 0
                reward_dict['RAamount'] = data.get('raamount')
        if ratransfer == True:
            reward_dict['RAtransfereffectivetime'] = data.get('ratransfereffectivetime', 24)
        self.sraward.add_model('Raward', **reward_dict)

        data = import_status("create_reward_success", "OK")
        data['data'] = {'raid': raid}
        return data

    @verify_token_decorator
    def admin_giving_reward(self):
        """后台赠送用户优惠券"""
        if not is_admin():
            raise AUTHORITY_ERROR(u'当前账号权限不足')
        data = request.json
        logger.debug("admin giving reward data is %s", data)
        parameter_required('raid', 'usid')
        usid = data.get('usid')
        raid = data.get('raid')
        ranumber = int(data.get('ranumber', 1))  # 该优惠券分发数量
        is_hold = self.sraward.is_user_hold_reward({'USid': usid, 'RAid': raid})
        if is_hold:
            urid = is_hold.URid
            logger.info("The user already has this type of reward ")
            update_info = self.sraward.update_user_reward({'URid': is_hold.URid}, {'RAnumber': is_hold.RAnumber + ranumber})
            if not update_info:
                raise SYSTEM_ERROR(u'更新数据错误')
        else:
            logger.info("New reward to user")
            urid = str(uuid.uuid1())
            self.sraward.add_model('UserRaward', **{
            'URid': urid,
            'USid': usid,
            'RAid': raid,
            'RAnumber': ranumber
        })
        data = import_status("hand_out_reward_success", "OK")
        data['data'] = {'urid': urid }
        return data

    @verify_token_decorator
    def user_receive_reward(self):
        """用户自己领取页面内的优惠券"""
        if is_tourist():
            raise TOKEN_ERROR(u'未登录')
        data = request.json
        parameter_required('raid')
        logger.debug("user recevive data is", data)
        usid = request.user.id
        raid = data.get('raid')

        # 判断发放的优惠券是否还有领取数量
        hang_out = self.sraward.is_hand_out({'RAid': raid})
        if hang_out:
            if hang_out.RTcount <= 0:
                raise NOT_FOUND(u'该优惠券已领取完毕')
            else:
                self.sraward.update_is_hand_out({'RAid': hang_out.RAid}, {'RTcount': hang_out.RTcount - 1})

        # 判断用户是否已持有
        is_hold = self.sraward.is_user_hold_reward({'USid': usid, 'RAid': raid})
        if is_hold:
            logger.info("The user already has this type of reward ")
            reward_info = self.sraward.get_raward_by_id(raid)
            urid = is_hold.URid
            if is_hold.RAnumber < reward_info.RAmaxholdnum:
                self.sraward.update_user_reward({'RAid': raid}, {'RAnumber': is_hold.RAnumber + 1})
            else:
                raise PARAMS_REDUNDANCE(u'已拥有该券最大可持有数量')
        else:
            logger.info("New reward to user")
            urid = str(uuid.uuid1())
            self.sraward.add_model('UserRaward', **{
                'URid': urid,
                'USid': usid,
                'RAid': raid,
            })

        data = import_status("receive_reward_success", "OK")
        data['data'] = {'urid': urid
                        }
        return data

    @verify_token_decorator
    def get_one_reward(self):
        """获取单张优惠券详情"""
        if is_tourist():
            raise TOKEN_ERROR(u'未登录')
        parameter_required('raid')
        args = request.args.to_dict()
        raid = args.get('raid')
        logger.debug("get reward info is %s", args)
        reward_info = self.sraward.get_raward_by_id(raid)
        if not reward_info:
            raise NOT_FOUND(u'无此券信息')
        reward_detail = self.fill_reward_detail(reward_info)
        data = import_status("messages_get_item_ok", "OK")
        data['data'] = reward_detail
        return data

    @verify_token_decorator
    def hand_out_reward(self):
        """平台发放在页面内的优惠券"""
        if not is_admin():
            raise AUTHORITY_ERROR(u'非管理员权限')
        data = request.json
        logger.debug("hand out data is %s", data)
        raid = data.get('raid')
        rtid = str(uuid.uuid1())
        is_hand_out = self.sraward.is_hand_out({'RAid': raid})
        if is_hand_out:
            raise PARAMS_REDUNDANCE(u'该优惠券已在页面发放')
        else:
            self.sraward.add_model('RewardToUser', **{
                'RTid': rtid,
                'RAid': raid,
                'RTcount': data.get('rtcount', 10)
            })
        data = import_status("hand_out_reward_success", "OK")
        data['data'] = {'rtid': rtid}
        return data

    @verify_token_decorator
    def get_hand_out_reward(self):
        """获取平台发放在页面中的优惠券"""
        if is_tourist():
            raise TOKEN_ERROR(u'未登录')
        horewards = self.sraward.get_all_hand_out()
        for horeward in horewards:
            reward = self.sraward.get_raward_by_id(horeward.RAid)
            reward_detail = self.fill_reward_detail(reward)
            horeward.fill(reward_detail, 'reward_detail')

        data = import_status("messages_get_item_ok", "OK")
        data['data'] = horewards
        return data

    @verify_token_decorator
    def give_reward_to_others(self):
        """转赠优惠券"""
        if is_tourist():
            raise TOKEN_ERROR(u'未登录')
        data = request.json
        usid = data.get('usid')
        urid = data.get('urid')
        # 在自己的普通券表中拥有
        is_own_hold = self.sraward.is_user_hold_reward({'USid': request.user.id, 'URid': urid})

        # 送出去过，但是已退回，可以继续转赠
        is_own_gift_hold = self.sraward.is_user_hold_reward_in_gift({'RFfrom': request.user.id, 'RFid': urid, 'RFstatus': 1})

        if is_own_hold:
            raid = is_own_hold.RAid
        elif is_own_gift_hold:
            raid = is_own_gift_hold.RAid
        else:
            raise NOT_FOUND(u'用户无此优惠券')
        reward_info = self.sraward.get_raward_by_id(raid)
        if reward_info.RAtransfer == False:
            raise SYSTEM_ERROR(u'该券不允许转赠')
        return_time = reward_info.RAtransfereffectivetime  # 转赠有效时间，退回时间

        # 已经赠送了该券给接收者，接收者还没用，且未到退回时间
        is_recivice_gift_hold = self.sraward.is_user_hold_reward_in_gift({'RAid': raid, 'USid': usid, 'RFstatus': 0, 'RFfrom': request.user.id})
        if is_recivice_gift_hold:
            raise SYSTEM_ERROR(u'您已赠送过该券给用户')

        # 接收者已经拥有其他人送的该券, 不影响, 忽略
        # is_recivice_hold_from_other = self.sraward.is_user_hold_reward({'USid': usid, 'RAid': raid})

        # 接收者原来已经拥有此券了
        is_recivice_hold = self.sraward.is_user_hold_reward({'RAid': raid})

        if is_own_gift_hold:
            up_reward_info = self.sraward.update_reward_transfer_info({'RFfrom': request.user.id, 'RFid': urid, 'RFstatus': 1}, {'USid':usid, 'RFstatus': 0})
            if not up_reward_info:
                raise SYSTEM_ERROR(u'再次转送失败')

        if is_own_hold and is_recivice_hold:
            if is_own_hold.RAnumber > 0 and is_recivice_hold.RAnumber < reward_info.RAmaxholdnum:
                logger.info("The user already has this type of reward ")
                update_reward = self.sraward.update_user_reward({'URid': is_own_hold.URid}, {'RAnumber': is_own_hold.RAnumber - 1})
                # self.sraward.update_user_reward({'RAid': raid}, {'RAnumber': is_recivice_hold.RAnumber + 1})
                rfid = str(uuid.uuid1())
                self.sraward.add_model('RewardTransfer', **{
                    'RFid': rfid,
                    'USid': usid,
                    'RAid': raid,
                    'URFrom': request.user.id,
                    'RAnumber': 1,
                    'RFendtime': (datetime.now() + timedelta(hours=int(return_time))).strftime(format_for_db),
                    'RFstatus': 0
                })

                if not update_reward:
                    raise PARAMS_ERROR(u'更新参数错误')
            else:
                raise NOT_FOUND(u'您已没有可赠送数量或赠送用户已拥有该券最大可持有数')
        elif is_own_hold and not is_recivice_hold:
            if is_own_hold.RAnumber > 0:
                logger.info("New reward to user")
                rfid = str(uuid.uuid1())
                self.sraward.add_model('RewardTransfer', **{
                    'RFid': rfid,
                    'USid': usid,
                    'RAid': raid,
                    'URFrom': request.user.id,
                    'RAnumber': 1,
                    'RFendtime': (datetime.now() + timedelta(hours=int(return_time))).strftime(format_for_db),
                    'RFstatus': 0
                })
            else:
                raise NOT_FOUND(u'您已没有可赠送的数量')
        else:
            raise NOT_FOUND(u'您已没有可赠送的数量')
        data = import_status("give_to_others_success", "OK")
        data['data'] = {'urid': urid}
        return data

    # TODO 持有数为零时的显示 / 是否允许删除失效券
    # TODO 大礼包晋升时直接给创建

    @verify_token_decorator
    def get_user_reward(self):
        """用户查看优惠券"""
        if is_tourist():
            raise TOKEN_ERROR(u'未登录')
        args = request.args.to_dict()
        logger.debug("get reward args is %s", args)
        topay = args.get('topay')
        allow_transfer = args.get('transfer')
        reward_info = self.sraward.get_reward_by_usid(request.user.id)
        if not reward_info:
            raise NOT_FOUND(u'用户暂无优惠券')
        try:
            for reward in reward_info:
                reward_detail = self.sraward.get_raward_by_id(reward.RAid)
                reward_detail = self.fill_reward_detail(reward_detail)
                reward.fill(reward_detail, 'reward_detail')
                reward.URcreatetime = get_web_time_str(reward.URcreatetime)

            if str(topay) == 'true':
                reward_info = filter(lambda r: r.reward_detail['RAtype'] in [0, 2], reward_info)

            if str(allow_transfer) == 'true':
                reward_info = filter(lambda r: r.reward_detail['RAtransfer'] == True, reward_info)

            data = import_status('messages_get_item_ok', "OK")
            data['data'] = reward_info
            return data
        except Exception as e:
            logger.exception("get user reward error")
            raise SYSTEM_ERROR(u'获取数据错误')

    @verify_token_decorator
    def get_user_pay_reward(self):
        """查看用户支付时的优惠券"""
        if is_tourist():
            raise TOKEN_ERROR(u'未登录')
        data = request.json
        logger.debug("get pay reward data is %s", data)
        skus = data.get('sku')
        # parameter_required('sku')
        from WeiDian.service.SProductSkuKey import SProductSkuKey
        if skus:
            total_price = 0
            for sku in skus:
                price = SProductSkuKey().get_true_price(sku.get('pskid')) * int(sku.get('num'))
                total_price = total_price + price

        reward_info = self.sraward.get_reward_by_usid(request.user.id)
        from WeiDian.models.model import RewardTransfer
        gift_reward_info = self.sraward.get_gifts_by_usfrom_or_usid((RewardTransfer.USid==request.user.id, RewardTransfer.RFfrom==request.user.id))

        try:
            reward_list = []
            for reward in reward_info:
                reward_detail = self.sraward.get_raward_by_id(reward.RAid)
                reward_detail = self.fill_reward_detail(reward_detail, total_price)
                reward.fill(reward_detail, 'reward_detail')
                reward = dict(reward)

                for i, j in reward.items():
                    reward[i.lower()] = j

                reward_list.append(reward)
                reward['urcreatetime'] = get_web_time_str(reward.get('urcreatetime'))
            for gift in gift_reward_info:
<<<<<<< HEAD
                if gift.RFfrom == request.user.id:
                    # todo 是赠送者获取状态，同时也有他人赠送自己的券
                    pass # pass防报错
=======
>>>>>>> 2bbc3d4e966ad1eaf8fb2fa754e14784cb465123
                gift = self.fill_transfer_detail(gift)
                gift_detail = self.sraward.get_raward_by_id(gift.RAid)
                gift_detail = self.fill_reward_detail(gift_detail, total_price)
                gift.fill(gift_detail, 'reward_detail')
                gift.RFcreatetime = get_web_time_str(gift.RFcreatetime)
                gift.RFendtime = get_web_time_str(gift.RFendtime)
                gift_dict = {
                    'urid': gift.RFid,
                    'usid': gift.USid,
                    'raid': gift.RAid,
                    'ranumber': gift.RAnumber,
                    'urcreatetime': gift.RFcreatetime,
                    'reendtime': gift.RFendtime,
                    'rffrom': gift.RFfrom,
                    'rfstatus': gift.RFstatus,
                    'urusetime': gift.RFusetime,
                    'remarks': gift.remarks,
                    'tag': gift.tag,
                    'usheader': gift.usheader,
                    'reward_detail': gift.reward_detail
                }
                reward_list.append(gift_dict)

            reward_info = filter(lambda r: r.get('reward_detail')['RAtype'] in [0, 2], reward_list)
            reward_info = filter(lambda k: k.get('ranumber') != 0, reward_info)

            data = import_status('messages_get_item_ok', "OK")
            data['data'] = reward_info
            return data
        except Exception as e:
            logger.exception("get user reward error")
            raise SYSTEM_ERROR(u'获取数据错误')


    def fill_reward_detail(self, raward, price=None):
        reward_number = '{0}张'
        reward_number_ratio = '前{0}单'
        filter_str = '满{0}-{1}新衣币'
        ratio_str = '佣金上涨{0}%'
        amout_str = '{0}元无门槛新衣币'
        if re.match(r'^[0-2]$', str(raward.RAtype)):
            if raward.RAtype == 0:
                reward_str = filter_str.format(int(raward.RAfilter), int(raward.RAamount))
            elif raward.RAtype == 1:
                reward_str = ratio_str.format(int(raward.RAratio))
            else:
                reward_str = amout_str.format(int(raward.RAamount))
        zh_ratype = REWARD_TYPE.get(str(raward.RAtype))
        raward.fill(zh_ratype, 'zh_ratype')
        raward.fill(reward_str, 'rewardstr')
        time_valid = raward.RAcreatetime < get_db_time_str() < raward.RAendtime
        if price:
            if raward.RAtype == 0:
                price_use = price > raward.RAfilter
            elif raward.RAtype == 2:
                price_use = True
            valid = time_valid and price_use
        else:
            valid = time_valid
        raward.fill(valid, 'valid')
        raward.RAendtime = get_web_time_str(raward.RAendtime)
        raward.RAcreatetime = get_web_time_str(raward.RAcreatetime)
        return raward

    def fill_transfer_detail(self, raward):
        from WeiDian.service.SUser import SUser
        if hasattr(raward, 'RFstatus'):
            reward_info = self.sraward.get_raward_by_id(raward.RAid)
            if reward_info.RAtransfer == False:
                raise SYSTEM_ERROR(u'信息错误，该券不能被赠送')
            if raward.RFstatus == 0:
                presenter = SUser().get_user_by_user_id(raward.RFfrom)
                recipient = SUser().get_user_by_user_id(raward.USid)
                if raward.USid == request.user.id:
                    usheader = presenter.USheader
                    remarks = '由{0}赠送'.format((presenter.USname).encode('utf8'))
                    tag = '赠送'
                elif raward.RFfrom == request.user.id:
                    usheader = recipient.USheader
                    remarks = '已赠送给{0}'.format((recipient.USname).encode('utf8'))
                    tag = '赠送'
            elif raward.RFstatus == 1:
                recipient = SUser().get_user_by_user_id(raward.USid)
                presenter = SUser().get_user_by_user_id(raward.RFfrom)
                if raward.USid == request.user.id:
                    usheader = presenter.USheader
                    remarks = '因领取后{0}小时未使用已退还给{1}'.format(reward_info.RAtransfereffectivetime, (presenter.USname).encode('utf8'))
                    tag = '已退回'
                elif raward.RFfrom == request.user.id:
                    usheader = recipient.USheader
                    remarks = '{0}领取后{1}小时未使用还回'.format((recipient.USname).encode('utf8'), reward_info.RAtransfereffectivetime)
                    tag = '已退回'
            elif raward.RFstatus == 2:
                recipient = SUser().get_user_by_user_id(raward.USid)
                usheader = recipient.USheader
                remarks = '{0}已使用'.format(str(recipient.USname))
                tag = '已使用'
        raward.fill(usheader, 'usheader')
        raward.fill(remarks, 'remarks')
        raward.fill(tag, 'tag')
        return raward

    def check_holdnum_is_exceeded(self, reward):
        """检查持有的优惠券是否超出可拥有数量"""
        pass