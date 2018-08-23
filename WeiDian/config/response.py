# *- coding:utf8 *-
from WeiDian.common.base_error import BaseError


class PARAMS_MISS(BaseError):
    status = 405
    status_code = 405001
    message = '参数缺失'


class TOKEN_ERROR(BaseError):
    status = 405
    status_code = 405001
    message = "未登录"


class AUTHORITY_ERROR(BaseError):
    status = 405
    status_code = 405001
    message = "无权限"


class SYSTEM_ERROR(BaseError):
    status_code = 200
    message = '系统错误'
    status = 404


class APIS_WRONG(BaseError):
    status = 405
    status_code = 405002
    message = "接口未注册"

class TIME_ERROR(BaseError):
    status = 405
    status_code = 405003
    message = "敬请期待"




# PARAMS_MISS = {
#     "status": 405,
#     "status_code": 405001,
#     "message": "参数缺失"
# }
#
# TOKEN_ERROR = {
#     "status": 405,
#     "status_code": 405001,
#     "message": "未登录"
# }
#
# AUTHORITY_ERROR = {
#     "status": 405,
#     "status_code": 405001,
#     "message": "无权限"
# }
# SYSTEM_ERROR = {
#     "status": 404,
#     "message": "系统异常"
# }
#
# APIS_WRONG = {
#     "status": 405,
#     "status_code": 405002,
#     "message": "接口未注册"
# }
#
# TIME_ERROR = {
#     "status": 405,
#     "status_code": 405003,
#     "message": "敬请期待"
# }

#