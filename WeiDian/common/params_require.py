# *- coding:utf8 *-
from flask import request

from WeiDian.config.response import PARAMS_MISS
from WeiDian import logger

def parameter_required(*required):
    """
    验证缺失的参数
    :param required:必须的参数列表
    :return:传入的参数
    """
    data = request.json
    logger.debug('get request data %s', data)
    if not data:
        raise PARAMS_MISS('未传入参数')
    if required:
        missed = filter(lambda x: x not in data, required)
        if missed:
            missed_params = '/'.join(missed)
            if isinstance(missed_params, unicode):
                missed_params = missed_params.encode("utf8")
            logger.debug('missed params is %s', missed_params)
            raise PARAMS_MISS('必要参数缺失: ' + missed_params)
    return data
