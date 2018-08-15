# *- coding:utf8 *-
import flask_restful
from flask import Flask

from WeiDian.apis.AActivity import AActivity

wd = Flask(__name__)
api = flask_restful.Api(wd)
api.add_resource(AActivity, "/activity/<string:activity>")


if __name__ == '__main__':
    wd.run(debug=True)
