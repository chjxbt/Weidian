# *- coding:utf8 *-
import flask_restful
from WeiDian import create_app

from WeiDian.apis.v1 import AActivity

wd = create_app()
api = flask_restful.Api(wd)
api.add_resource(AActivity, "/activity/<string:activity>")


if __name__ == '__main__':
    wd.run(debug=True)
