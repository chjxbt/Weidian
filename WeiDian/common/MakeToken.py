# *- coding:utf8 *-
import datetime
from collections import namedtuple

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from flask import current_app, request
User = namedtuple("User", ['USid', 'Scope', 'time'])


def usid_to_token(usid, scope='user', expiration=current_app['TOKEN_EXPIRATION']):
        """生成令牌
        usid: 用户USid
        scope: 用户类型(user 或者 superuser)
        expiration: 过期时间
        """
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return s.dumps({
            'usid': usid,
            'scope': scope,
            'time': time_now
        })


def token_to_usid(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature as e:
        return '不合法的token'
    except SignatureExpired as e:
        return 'token is expired'
    except Exception as e:
        raise e
    usid = data['usid']
    time = data['time']
    scope = data['scope']
    return usid


def verify_token_decorator(func):
    def inner(self, *args, **kwargs):
        parameter = request.args.to_dict()
        token = parameter.get('token')
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except BadSignature as e:
            # 无法解析的token
            return func(self, *args, **kwargs)
        except SignatureExpired as e:
            # 过期的token
            return func(self, *args, **kwargs)
        except Exception, e:
            # 无法解析的token
            return func(self, *args, **kwargs)
        usid = data['usid']
        time = data['time']
        scope = data['scope']
        user = User(usid, scope, time)
        request.user = user
        return func(self, *args, **kwargs)
    return inner

