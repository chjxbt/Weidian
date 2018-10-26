# -*- coding:utf8 -*-
import re

from flask import request

from WeiDian.config.response import PARAMS_MISS, PARAMS_ERROR
from WeiDian import logger


def parameter_required(*required):
    """
    验证缺失的参数
    :param required:必须的参数列表
    :return:传入的参数
    """

    body_data = request.json or {}
    query_data = request.args.to_dict() or {}
    total_date = dict(body_data, **query_data)
    # data.update(query_data)

    if not total_date:
        raise PARAMS_MISS(u'未传入参数')
    if required:
        missed = filter(lambda x: x not in total_date, required)

        if missed:
            missed_params = '/'.join(missed)
            if isinstance(missed_params, str):
                missed_params = missed_params.decode("utf8")
            logger.debug('missed params is %s', missed_params)
            raise PARAMS_MISS(u'必要参数缺失: ' + missed_params)
    return body_data
    # TODO 校验参数待重新修改


def validate_phone(arg):
    regex_phone = "^1\d{10}$"
    return validate_arg(regex_phone, arg, str(arg) + u'不是手机号码')


def validate_arg(regex, arg, msg=None):
    if arg is None:
        return
    res = re.match(regex, str(arg))
    if not res:
        raise PARAMS_ERROR(msg)
    return arg

