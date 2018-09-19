# *- coding:utf8 *-
from flask import request

from WeiDian.config.response import PARAMS_MISS


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
            raise PARAMS_MISS(u'必要参数缺失: ' + '/'.join(missed))
    return body_data
    # TODO 校验参数待重新修改
