# *- coding:utf8 *-
import datetime
from collections import namedtuple

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from flask import current_app, request

from WeiDian.service.DBSession import db_session


def usid_to_token(id, model='User', expiration=''):
        """生成令牌
        id: 用户id
        scope: 用户类型(user 或者 superuser)
        expiration: 过期时间
        """
        if not expiration:
            expiration = current_app.config['TOKEN_EXPIRATION']
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return s.dumps({
            'id': id,
            'model': model,
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
    id = data['id']
    time = data['time']
    model = data['model']
    return id


def verify_token_decorator(func):
    """验证token装饰器, 并将用户对象放入request.user中"""
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
        id = data['id']
        time = data['time']
        model = data['model']
        if model != 'User' and model != 'SuperUser':
            return func(self, *args, **kwargs)
        sessions = db_session()
        try:
            if model == 'User':
                from WeiDian.models.model import User
                user = sessions.query(User).filter_by(USid=id).first()
                user.id = user.USid
                user.scope = 'User'
            if model == 'SuperUser':
                from WeiDian.models.model import SuperUser
                user = sessions.query(SuperUser).filter_by(SUid=id).first()
                user.id = user.SUid
                user.scope = 'SuperUser'
            sessions.expunge_all()
            sessions.commit()
            if user:
                request.user = user
            return func(self, *args, **kwargs)
        finally:
            sessions.close()
    return inner


# if __name__ == '__main__':
#     from WeiDian import create_app
#     app = create_app()
#     res = usid_to_token('6882ad09-bf5f-4607-8ad1-1cd46b6158e0', current_app=app)
#     print(res)

