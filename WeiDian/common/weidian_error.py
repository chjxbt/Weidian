# *- coding:utf8 *-
from WeiDian.common.base_error import BaseError


class dberror(BaseError):
    code = 200
    message = '系统错误'
    status = 404