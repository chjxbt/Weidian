# *- coding:utf8 *-
from datetime import date

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
# from flask_cors import CORS
from werkzeug.exceptions import HTTPException
from WeiDian.apis.v1 import AActivity, AHotMessage, ABanner, ASearchField, ATopNav, \
    ASuperUser, AProduct, ARecommendBanner, AShoppingCart, AActivityComment, AUser, ARecommend, AOrder, AProductLike, \
    ARecommendLike, AActivityLike, AMyCenter
from test.test_maketoken import create_test_url


class JSONEncoder(_JSONEncoder):
    """重写对象序列化, 当默认jsonify无法序列化对象的时候将调用这里的default"""
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            res = dict(o)
            for k in res.keys():
                if k[0].isupper():
                    # 字段转小写
                    res[k.lower()] = res[k]
                    res.pop(k)
            return res
        if isinstance(o, date):
            # 也可以序列化时间类型的对象
            return o.strftime('%Y-%m-%d')
        if isinstance(o, type):
            raise o()
        if isinstance(o, HTTPException):
            raise o
        raise Exception()


class Flask(_Flask):
    json_encoder = JSONEncoder


# def register_route(app):
#     """添加路由"""
#     api = flask_restful.Api(app)
#     api.add_resource(AActivity, '/activity/<string:activity>')
#     api.add_resource(AHotMessage, '/hotmessage/<string:hotmessage>')
#     api.add_resource(ABanner, '/banner/<string:banner>')
#     api.add_resource(ATopNav, '/topnav/<string:topnav>')
#     api.add_resource(ASearchField, '/searchfield/<string:searchfield>')
#     api.add_resource(ASuperUser, '/super/<string:super>')
#     api.add_resource(AProduct, '/product/<string:product>')
#     api.add_resource(ARecommendBanner, '/recommendbanner/<string:recommendbanner>')
#     api.add_resource(AShoppingCart, '/shoppingcart/<string:shoppingcart>')


def register_route(app):
    """添加路由"""
    app.add_url_rule('/activity/<string:activity>', view_func=AActivity.as_view('activity'))
    app.add_url_rule('/hotmessage/<string:hotmessage>', view_func=AHotMessage.as_view('hotmesage'))
    app.add_url_rule('/banner/<string:banner>', view_func=ABanner.as_view('banner'))
    app.add_url_rule('/topnav/<string:topnav>', view_func=ATopNav.as_view('topnav'))
    app.add_url_rule('/searchfield/<string:searchfield>', view_func=ASearchField.as_view('searchfield'))
    app.add_url_rule('/super/<string:super>', view_func=ASuperUser.as_view('super'))
    app.add_url_rule('/product/<string:product>', view_func=AProduct.as_view('product'))
    app.add_url_rule('/recommendbanner/<string:recommendbanner>', view_func=ARecommendBanner.as_view('recommendbanner'))
    app.add_url_rule('/shoppingcart/<string:shoppingcart>', view_func=AShoppingCart.as_view('shoppingcart'))
    app.add_url_rule('/recommend/<string:recommend>', view_func=ARecommend.as_view('recommend'))
    app.add_url_rule('/activitycomment/<string:activitycomment>', view_func=AActivityComment.as_view('activitycomment'))
    app.add_url_rule('/user/<string:user>', view_func=AUser.as_view('user'))
    app.add_url_rule('/order/<string:order>', view_func=AOrder.as_view('order'))
    app.add_url_rule('/productlike/<string:productlike>', view_func=AProductLike.as_view('productlike'))
    app.add_url_rule('/recommendlike/<string:recommendlike>', view_func=ARecommendLike.as_view('recommendlike'))
    app.add_url_rule('/activitylike/<string:activitylike>', view_func=AActivityLike.as_view('activitylike'))
    app.add_url_rule('/mycenter/<string:myinfo>', view_func=AMyCenter.as_view('mycenter'))


def create_app():
    app = Flask(__name__)
    app.config.from_object('WeiDian.config.setting')
    register_route(app)
    create_test_url(app)  # 测试用
    # CORS(app, supports_credentials=True)
    return app
