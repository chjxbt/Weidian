# *- coding:utf8 *-
from datetime import datetime

from flask.json import JSONEncoder as _JSONEncoder
class JSONEncoder(_JSONEncoder):
    """重写对象序列化, 当默认jsonify无法序列化对象的时候将调用这里的default"""
    def default(self, o):
        try:
            if isinstance(o, datetime):
                # 也可以序列化时间类型的对象
                return o.strftime('%Y%m%d')
            raise Exception()
        except Exception as e:
            return o.__dict__
