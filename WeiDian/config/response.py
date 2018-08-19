# *- coding:utf8 *-
PARAMS_MISS = {
    "status": 405,
    "status_code": 405001,
    "message": "参数缺失"
}

TOKEN_ERROR = {
    "status": 405,
    "status_code": 405001,
    "message": "未登录"
}

AUTHORITY_ERROR = {
    "status": 405,
    "status_code": 405001,
    "message": "无权限"
}
SYSTEM_ERROR = {
    "status": 404,
    "message": "系统异常"
}

APIS_WRONG = {
    "status": 405,
    "status_code": 405002,
    "message": "接口未注册"
}

TIME_ERROR = {
    "status": 405,
    "status_code": 405003,
    "message": "敬请期待"
}
