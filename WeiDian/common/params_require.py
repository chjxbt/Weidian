# *- coding:utf8 *-
from flask import request

from WeiDian.config.response import PARAMS_MISS


def parameter_required(*required):
    """
    验证缺失的参数
    :param required:必须的参数列表
    :return:传入的参数
    """
    data = request.json or request.args.to_dict()
    if not data:
        raise PARAMS_MISS(u'未传入参数')
    if required:
        missed = filter(lambda x: x not in data, required)
        if missed:
            raise PARAMS_MISS(u'必要参数缺失: ' + '/'.join(missed))
    return data
