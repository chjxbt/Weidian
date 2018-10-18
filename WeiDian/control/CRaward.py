# -*- coding:utf8 -*-
import re
import sys
import os
import uuid
from flask import request
from WeiDian import logger
from datetime import datetime, timedelta
from WeiDian.common.params_require import parameter_required
from WeiDian.common.import_status import import_status
from WeiDian.common.timeformat import get_db_time_str, get_web_time_str, format_for_web_second, format_for_db
from WeiDian.common.token_required import verify_token_decorator, is_admin, is_tourist
from WeiDian.config.response import PARAMS_MISS, TOKEN_ERROR, AUTHORITY_ERROR, SYSTEM_ERROR, NOT_FOUND, PARAMS_ERROR
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
            raise PARAMS_MISS(u'ratype, 参数异常')
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
        ranumber = int(data.get('ranumber'), 1)  # 该优惠券分发数量
        is_hold = self.sraward.is_user_hold_reward({'USid': usid, 'RAid': raid})
        if is_hold:
            logger.info("The user already has this type of reward ")
            update_info = self.sraward.update_user_reward({'URid': is_hold.URid}, {'RAnumber': is_hold.RAnumber + ranumber})
            if not update_info:
                raise SYSTEM_ERROR(u'更新数据错误')
        else:
            logger.info("New reward to user")
            self.sraward.add_model('UserRaward', **{
            'URid': str(uuid.uuid1()),
            'USid': usid,
            'RAid': raid,
            'RAnumber': ranumber
        })
        data = import_status("hand_out_reward_success", "OK")
        data['data'] = {'usid': usid,
                        'raid': raid
                        }
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
        is_hold = self.sraward.is_user_hold_reward({'USid': usid, 'RAid': raid})
        if is_hold:
            logger.info("The user already has this type of reward ")
            reward_info = self.sraward.get_raward_by_id(raid)
            urid = is_hold.URid
            if is_hold.RAnumber < reward_info.RAmaxholdnum:
                self.sraward.update_user_reward({'RAid': raid}, {'RAnumber': is_hold.RAnumber + 1})
            else:
                raise SYSTEM_ERROR(u'已拥有该券最大可持有数量')
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






    # TODO 用户转赠优惠券 / 获取平台发放页面内的优惠券 / 后台获取所有优惠券(发现在Task里) /




    @verify_token_decorator
    def get_user_reward(self):
        """用户查看优惠券"""
        if is_tourist():
            raise TOKEN_ERROR(u'未登录')
        logger.debug("get reward usid is %s", request.user.id)
        reward_info = self.sraward.get_reward_by_usid(request.user.id)
        if not reward_info:
            raise NOT_FOUND(u'用户暂无优惠券')
        try:
            for reward in reward_info:
                reward_detail = self.sraward.get_raward_by_id(reward.RAid)
                reward.fill(reward_detail, 'reward_detail')
            data = import_status('messages_get_item_ok', "OK")
            data['data'] = reward_info
        except Exception as e:
            logger.exception("get user reward error")
            raise SYSTEM_ERROR(u'获取数据错误')

    @staticmethod
    def fill_reward_detail(raward):
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
            raward.rewardstr = reward_str
            raward.add('rewardstr')
        return raward