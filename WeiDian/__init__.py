# *- coding:utf8 *-
from datetime import date

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder


class JSONEncoder(_JSONEncoder):
    """重写对象序列化, 当默认jsonify无法序列化对象的时候将调用这里的default"""
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            res = dict(o)
            for k in res.keys():
                if k[0].isupper():
                    res[k.lower()] = res[k]
                    res.pop(k)
            return res
        if isinstance(o, date):
            # 也可以序列化时间类型的对象
            return o.strftime('%Y-%m-%d')
        raise Exception()


class Flask(_Flask):
    json_encoder = JSONEncoder


def create_app():
    app = Flask(__name__)
    return app
