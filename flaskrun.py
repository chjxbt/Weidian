# *- coding:utf8 *-
import flask_restful
from WeiDian import create_app

from WeiDian.apis.v1 import AActivity, AHotMessage, ABanner, ASearchField, ATopNav, ASuperUser, AProduct, AShoppingCart
from WeiDian.common.base_error import BaseError
from werkzeug.exceptions import HTTPException
from test.test_maketoken import create_test_url

wd = create_app()
api = flask_restful.Api(wd)
api.add_resource(AActivity, '/activity/<string:activity>')
api.add_resource(AHotMessage, '/hotmessage/<string:hotmessage>')
api.add_resource(ABanner, '/banner/<string:banner>')
api.add_resource(ATopNav, '/topnav/<string:topnav>')
api.add_resource(ASearchField, '/searchfield/<string:searchfield>')
api.add_resource(ASuperUser, '/super/<string:super>')
api.add_resource(AProduct, '/product/<string:product>')
api.add_resource(AShoppingCart, '/shoppingcart/<string:shoppingcart>')


# 测试
create_test_url(wd)


@wd.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, BaseError):
        return e
    if isinstance(e, HTTPException):
        raise BaseError()
    if not wd.config['DEBUG']:
        raise BaseError()
    raise e


if __name__ == '__main__':
    wd.run(debug=True)
