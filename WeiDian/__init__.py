# *- coding:utf8 *-
from datetime import date

import flask_restful
from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from WeiDian.apis.v1 import AActivity, AHotMessage, ABanner, ASearchField, ATopNav, \
    ASuperUser, AProduct, ARecommendBanner, AShoppingCart
from WeiDian.common.base_error import BaseError


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


def register_route(app):
    api = flask_restful.Api(app)
    api.add_resource(AActivity, '/activity/<string:activity>')
    api.add_resource(AHotMessage, '/hotmessage/<string:hotmessage>')
    api.add_resource(ABanner, '/banner/<string:banner>')
    api.add_resource(ATopNav, '/topnav/<string:topnav>')
    api.add_resource(ASearchField, '/searchfield/<string:searchfield>')
    api.add_resource(ASuperUser, '/super/<string:super>')
    api.add_resource(AProduct, '/product/<string:product>')
    api.add_resource(ARecommendBanner, '/recommendbanner/<string:recommendbanner>')
    api.add_resource(AShoppingCart, '/shoppingcart/<string:shoppingcart>')
    # 测试
    from test.test_maketoken import create_test_url
    create_test_url(app)



def create_app():
    app = Flask(__name__)
    app.config.from_object('WeiDian.config.setting')
    register_route(app=app)
    return app
