# -*- coding: utf-8 -*-
from decimal import Decimal
from WeiDian import logger
from flask import request
from WeiDian.common.loggers import generic_log
from WeiDian.common.token_required import verify_token_decorator, is_tourist, is_partner, is_admin
from WeiDian.config.response import TOKEN_ERROR, AUTHORITY_ERROR
from WeiDian.common.import_status import import_status


class CCommision(object):

    def __init__(self):
        from WeiDian.service.SCommision import SCommision
        self.scommion = SCommision()
        from WeiDian.service.SUser import SUser
        self.suser = SUser()
        from WeiDian.control.Cuser import CUser
        self.cuser = CUser()
        self.empty = ['', {}, [], None]

    @verify_token_decorator
    def get_commsion_list(self):
        """后台获取佣金统计"""
        if not is_admin():
            raise AUTHORITY_ERROR(u'请使用管理员账号重新登录')
        args = request.args.to_dict()
        logger.debug("Get commsion list args is %s", args)
        kw = args.get('kw')
        kw = kw.encode('utf8') if kw not in self.empty else None
        time_start = args.get('time_start')
        time_end = args.get('time_end')
        pagenum, pagesize = self.cuser.get_pagesize_pagenum(args)
        user_list, count = self.suser.get_all_partner_by_filter(pagenum, pagesize, kw)
        commision_list = []
        try:
            for user in user_list:
                usid = user.USid
                data = {
                    'usname': user.USname,
                    'usphone': user.USphone,
                    'total': self._total_commision(usid),               # 总额
                    'sold_income': self._user_commision(usid, 0),       # 销售佣金
                    'invite_open': self._user_commision(usid, 10),      # 邀请开店佣金
                    'fans_outincome': self._user_commision(usid, 20),   # 专粉佣金
                    'group_income': self._team_commision(usid),         # 团队佣金
                    'remain': self._remain_commision(usid),             # 余额
                    'reward_income': self._user_commision(usid, 40),    # 奖励佣金
                    'priview': self._privew_commision(usid),            # 预估到帐
                    'extracting': self._extract_commision(usid)         # 正在提现的佣金
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
    def get_userlist_with_commision(self):
        """用户-佣金列表"""
        if not is_admin():
            raise TOKEN_ERROR(u'请使用管理员登录')
        # partner_list = self


    def _user_commision(self, usid, type):
        """用户佣金类型"""
        commsion = self.scommion.get_usercommsion_flow_filter({
            'USid': usid,
            'UCFtype': type
        })
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