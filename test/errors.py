
from flask import request, json, jsonify
from flask._compat import implements_to_string
from werkzeug.exceptions import HTTPException


class ApiException(HTTPException):
    code = 200
    msg = 'sorry, we make a mistake'
    error_code = 999

    def __init__(self, code=None, msg=None, error_code=None, header=None):
        if code:
            self.code = code
        if msg:
            self.msg = msg
        if error_code:
            self.error_code = error_code
        super(ApiException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            error_code=self.error_code,
            # request="POST v1/client/register"
            request=request.method + ' ' + self.get_url_no_param()
        )
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]

    def get_response(self, environ=None):
        from werkzeug.wrappers import Response
        headers = self.get_headers(environ)
        return Response(self.get_body(environ), self.code, headers)

    @staticmethod
    def get_url_no_param():
        full_url = str(request.full_path)
        main_path = full_url.split('?')
        return main_path[0]

