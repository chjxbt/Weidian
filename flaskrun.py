# *- coding:utf8 *-
from WeiDian import create_app
from WeiDian.common.base_error import BaseError

wd = create_app()


# @wd.errorhandler(Exception)
# def framework_error(e):
#     if isinstance(e, BaseError):
#         return e
#     if not wd.config['DEBUG']:
#         raise BaseError()
#     raise e


if __name__ == '__main__':
    wd.run('0.0.0.0', 7443, debug=True)
