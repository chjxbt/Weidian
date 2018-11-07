# -*- coding: utf-8 -*-
from decimal import Decimal
from WeiDian import logger
from WeiDian.common.timeformat import get_db_time_str
from flask import request
from WeiDian.common.loggers import generic_log
from WeiDian.common.token_required import verify_token_decorator, is_tourist, is_partner, is_admin
from WeiDian.config.response import TOKEN_ERROR, AUTHORITY_ERROR, PARAMS_ERROR
from WeiDian.common.import_status import import_status


class CCommision(object):

    def __init__(self):
        from WeiDian.service.SCommision import SCommision
        self.scommion = SCommision()
        from WeiDian.service.SUser import SUser
        self.suser = SUser()
        from WeiDian.control.Cuser import CUser
        self.cuser = CUser()
        from WeiDian.common.divide import Partner
        self.pn = Partner()
        self.empty = ['', {}, [], None]

    @verify_token_decorator
    def get_commsion_list(self):
        """后台获取佣金统计表格"""
        if not is_admin():
            raise AUTHORITY_ERROR(u'请使用管理员账号重新登录')
        args = request.args.to_dict()
        logger.debug("Get commsion list args is %s", args)
        kw = args.get('kw')
        kw = kw.encode('utf8') if kw not in self.empty else None
        time_start = args.get('time_start')
        time_start = get_db_time_str(time_start) if time_start not in self.empty else None
        time_end = args.get('time_end')
        time_end = get_db_time_str(time_end) if time_end not in self.empty else None
        pagenum, pagesize = self.cuser.get_pagesize_pagenum(args)
        user_list, count = self.suser.get_all_partner_by_filter(pagenum, pagesize, kw)
        commision_list = []
        try:
            for user in user_list:
                usid = user.USid
                data = {
                    'usname': user.USname,
                    'usphone': user.USphone,
                    'total': self._total_commision(usid),                                     # 总额
                    'sold_income': self._user_commision(usid, 0, time_start, time_end),       # !销售佣金
                    'invite_open': self._user_commision(usid, 10, time_start, time_end),      # !邀请开店佣金
                    'fans_outincome': self._user_commision(usid, 20, time_start, time_end),   # !专粉佣金
                    'group_income': self._team_commision(usid),                               # 团队佣金
                    'remain': self._remain_commision(usid),                                   # 余额
                    'reward_income': self._user_commision(usid, 40, time_start, time_end),    # 周周奖佣金
                    'novice_reward': self._user_commision(usid, 45, time_start, time_end),    # !新手任务佣金
                    'priview': self._privew_commision(usid),                                  # 预估到帐
                    'extracting': self._extract_commision(usid)                               # 正在提现的佣金
                }
                commision_list.append(data)
        except Exception as e:
            generic_log(e)
            raise e
        response = import_status('get_success', 'OK')
        response['data'] = commision_list
        response['count'] = count
        return response

    @verify_token_decorator
    def get_commission_overview(self):
        """后台佣金概况"""
        if not is_admin():
            raise AUTHORITY_ERROR(u'请使用管理员账号重新登录')
        args = request.args.to_dict()
        logger.debug("Get commsion overview args is %s", args)
        time_start, time_end = None, None
        from WeiDian.models.model import User
        user_dict = {
            'primary': 1,
            'middle': 2,
            'advanced': 3
        }
        for k, v in user_dict.items():
            user_dict[k] = self.suser.get_all_user_without_pagecut((User.USlevel == user_dict[k],))

        p_sold_income, p_invite_open, p_week_reward, p_extra_reward, p_fans_outincome, p_novice_reward = 0, 0, 0, 0, 0, 0
        for user in user_dict['primary']:
            usid = user.USid
            sold_income = self._user_commision(usid, 0, time_start, time_end)  # 销售佣金（商品佣金支出）
            p_sold_income += sold_income
            invite_open = self._user_commision(usid, 10, time_start, time_end)  # 邀请开店佣金
            p_invite_open += invite_open
            reward_income = self._user_commision(usid, 40, time_start, time_end)  # 周周奖
            p_week_reward += reward_income
            extra_reward = self._user_commision(usid, 41, time_start, time_end)  # 额外奖励
            p_extra_reward += extra_reward
            fans_outincome = self._user_commision(usid, 20, time_start, time_end)  # 专粉佣金支出
            p_fans_outincome += fans_outincome
            novice_reward = self._user_commision(usid, 45, time_start, time_end)  # 新店主任务奖励佣金
            p_novice_reward += novice_reward
        primary = {
            "levelname": u'1级',
            "sold_income": p_sold_income,
            "invite_open": p_invite_open,
            "week_reward": p_week_reward,
            "reward_income": p_extra_reward,
            "fans_outincome": p_fans_outincome,
            "novice_reward": p_novice_reward
        }

        m_sold_income, m_invite_open, m_week_reward, m_extra_reward, m_fans_outincome, m_novice_reward = 0, 0, 0, 0, 0, 0
        for user in user_dict['middle']:
            usid = user.USid
            sold_income = self._user_commision(usid, 0, time_start, time_end)  # 销售佣金（商品佣金支出）
            m_sold_income += sold_income
            invite_open = self._user_commision(usid, 10, time_start, time_end)  # 邀请开店佣金
            m_invite_open += invite_open
            reward_income = self._user_commision(usid, 40, time_start, time_end)  # 周周奖
            m_week_reward += reward_income
            extra_reward = self._user_commision(usid, 41, time_start, time_end)  # 额外奖励
            m_extra_reward += extra_reward
            fans_outincome = self._user_commision(usid, 20, time_start, time_end)  # 专粉佣金支出
            m_fans_outincome += fans_outincome
            novice_reward = self._user_commision(usid, 45, time_start, time_end)  # 新店主任务奖励佣金
            m_novice_reward += novice_reward
        middle = {
            "levelname": u'2级',
            "sold_income": m_sold_income,
            "invite_open": m_invite_open,
            "week_reward": m_week_reward,
            "reward_income": m_extra_reward,
            "fans_outincome": m_fans_outincome,
            "novice_reward": m_novice_reward
        }

        a_sold_income, a_invite_open, a_week_reward, a_extra_reward, a_fans_outincome, a_novice_reward = 0, 0, 0, 0, 0, 0
        for user in user_dict['advanced']:
            usid = user.USid
            sold_income = self._user_commision(usid, 0, time_start, time_end)  # 销售佣金（商品佣金支出）
            a_sold_income += sold_income
            invite_open = self._user_commision(usid, 10, time_start, time_end)  # 邀请开店佣金
            a_invite_open += invite_open
            reward_income = self._user_commision(usid, 40, time_start, time_end)  # 周周奖
            a_week_reward += reward_income
            extra_reward = self._user_commision(usid, 41, time_start, time_end)  # 额外奖励
            a_extra_reward += extra_reward
            fans_outincome = self._user_commision(usid, 20, time_start, time_end)  # 专粉佣金支出
            a_fans_outincome += fans_outincome
            novice_reward = self._user_commision(usid, 45, time_start, time_end)  # 新店主任务奖励佣金
            a_novice_reward += novice_reward
        advanced = {
            "levelname": u'3级',
            "sold_income": a_sold_income,
            "invite_open": a_invite_open,
            "week_reward": a_week_reward,
            "reward_income": a_extra_reward,
            "fans_outincome": a_fans_outincome,
            "novice_reward": a_novice_reward
        }
        total = {
            "levelname": u'全部',
            "sold_income": primary['sold_income'] + middle['sold_income'] + advanced['sold_income'],
            "invite_open": primary['invite_open'] + middle['invite_open'] + advanced['invite_open'],
            "week_reward": primary['week_reward'] + middle['week_reward'] + advanced['week_reward'],
            "reward_income": primary['reward_income'] + middle['reward_income'] + advanced['reward_income'],
            "fans_outincome": primary['fans_outincome'] + middle['fans_outincome'] + advanced['fans_outincome'],
            "novice_reward": primary['novice_reward'] + middle['novice_reward'] + advanced['novice_reward']
        }
        data = [total, primary, middle, advanced]
        response = import_status('get_success', 'OK')
        response['data'] = data
        return response

    @verify_token_decorator
    def set_commission(self):
        """佣金设置"""
        if not is_admin():
            raise AUTHORITY_ERROR(u'请使用管理员账号重新登录')
        # todo 设置周周奖 (开始时间/结束时间 分周)
        # todo 设置额外活动
        data = request.json
        logger.debug("SET commission data is %s", data)
        # 设置合伙人三级佣金比例
        divide_one = data.get('divide_one')
        if divide_one not in self.empty and divide_one.isdigit():
            divide_one = float(divide_one) / 100
            self.pn.one_level_divide = str(divide_one)
        divide_two = data.get('divide_two')
        if divide_two not in self.empty and divide_two.isdigit():
            divide_two = float(divide_two) / 100
            self.pn.two_level_divide = str(divide_two)
        divide_three = data.get('divide_three')
        if divide_three not in self.empty and divide_three.isdigit():
            divide_three = float(divide_three) / 100
            self.pn.three_level_divide = str(divide_three)
        # 设置专粉单数及佣金限制
        limit_time_one = data.get('time_one')  # [1,5]
        fans_price_one = data.get('fans_price_one')  # 30
        if fans_price_one not in self.empty:
            fans_price_one = float(fans_price_one) / 100
            self.pn.set_item("level_limit_1", "profit", fans_price_one)
        if limit_time_one not in self.empty:
            self.pn.set_item("level_limit_1", "min", limit_time_one[0])
            self.pn.set_item("level_limit_1", "max", limit_time_one[-1])

        limit_time_two = data.get('time_two')  # [6, 20]
        fans_price_two = data.get('fans_price_two')  # 30
        if fans_price_two not in self.empty:
            fans_price_two = float(fans_price_two) / 100
            self.pn.set_item("level_limit_1", "profit", fans_price_two)
        if limit_time_two not in self.empty:
            if limit_time_two[0] - limit_time_one[-1] != 1:
                raise PARAMS_ERROR(u'timeone 参数错误')
            self.pn.set_item("level_limit_2", "min", limit_time_two[0])
            self.pn.set_item("level_limit_2", "max", limit_time_two[-1])

        limit_time_three = data.get('time_three')  # 21
        fans_price_three = data.get('fans_price_three')  # 30
        if fans_price_three not in self.empty:
            fans_price_three = float(fans_price_three) / 100
            self.pn.set_item("level_limit_1", "profit", fans_price_three)
        if limit_time_three not in self.empty:
            if limit_time_three[0] - limit_time_two[-1] != 1:
                raise PARAMS_ERROR(u'timeone 参数错误')
            self.pn.set_item("level_limit_3", "min", limit_time_three)

        response = import_status("set_success", "OK")
        response['data'] = {
            "divide_one": self.pn.one_level_divide,
            "divide_two": self.pn.two_level_divide,
            "divide_three": self.pn.three_level_divide
        }
        return response


    def _user_commision(self, usid, type, time_start, time_end):
        """用户佣金类型"""
        commsion = self.scommion.get_usercommsion_flow_filter({
            'USid': usid,
            'UCFtype': type
        }, time_start, time_end)
        mount = sum(Decimal(x.UCFnums) for x in commsion) if commsion else 0
        return float(mount)

    def _remain_commision(self, usid):
        """佣金余额"""
        user_commision = self.scommion.get_usercommsion_by_usid(usid)
        user_commision_num = getattr(user_commision, 'UCnum', 0)
        return user_commision_num

    def _total_commision(self, usid):
        """总获得"""
        user_commision = self.scommion.get_usercommsion_by_usid(usid)
        user_commision_num = getattr(user_commision, 'UCtotal', 0)
        return user_commision_num

    def _privew_commision(self, usid):
        """预估佣金"""
        commsion_privews = self.scommion.get_commision_preview_by_usid(usid)
        priview_mount = sum(Decimal(x.UCPnums) for x in commsion_privews) if commsion_privews else 0
        return float(priview_mount)

    def _team_commision(self, usid):
        """团队佣金"""
        team_commision = self.scommion.get_teamcommision_by_usid(usid)
        team_amout = sum(Decimal(x.TCtotal) for x in team_commision) if team_commision else 0
        return float(team_amout)

    def _extract_commision(self, usid):
        """正提现佣金"""
        extract_commision = self.scommion.get_extractcommision_by_filter({'USid': usid,
                                                                          'CTCstatus': 0
                                                                          })
        extract_amout = sum(Decimal(x.CTCamount) for x in extract_commision) if extract_commision else 0
        return float(extract_amout)
