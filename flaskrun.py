# *- coding:utf8 *-
from WeiDian import create_app
wd = create_app()


# @wd.errorhandler(Exception)
# def framework_error(e):
#     if isinstance(e, BaseError):
#         return e
#     if isinstance(e, HTTPException):
#         raise BaseError()
#     if not wd.config['DEBUG']:
#         raise BaseError()
#     raise e


if __name__ == '__main__':
    wd.run(debug=True)
