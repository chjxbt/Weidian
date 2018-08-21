# *- coding:utf8 *-
from flask import request, json
from werkzeug.exceptions import HTTPException


class BaseError(HTTPException):
    code = 200
    message = '系统错误'
    status = 404

    def __init__(self, code=None, message=None, status=None, status_code=None, header=None):
        if code:
            self.code = code
        if message:
            self.message = message
        if status_code:
            self.status_code = status_code
        if status:
            self.status = status
        super(BaseError, self).__init__(message, None)

    def get_body(self, environ=None):
        if hasattr(self, 'status_code'):
            body = dict(
                status=self.status,
                status_code=self.status_code,
                message=self.message,
            )
        else:
            body = dict(
                status=self.status,
                message=self.message,
            )
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]