# *- coding:utf8 *-
import flask_restful
from WeiDian import create_app

from WeiDian.apis.v1 import AActivity, AHotMessage, ABanner, ASearchField, ATopNav

wd = create_app()
api = flask_restful.Api(wd)
api.add_resource(AActivity, '/activity/<string:activity>')
api.add_resource(AHotMessage, '/hotmessage/<string:hotmessage>')
api.add_resource(ABanner, '/banner/<string:banner>')
api.add_resource(ATopNav, '/topnav/<string:topnav>')
api.add_resource(ASearchField, '/searchfield/<string:searchfield>')


if __name__ == '__main__':
    wd.run(debug=True, )
