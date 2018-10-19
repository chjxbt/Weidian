# *- coding:utf8 *-
import sys
import os
from contextlib import contextmanager
import DBSession
from WeiDian.common.loggers import generic_log
from WeiDian.common.weidian_error import dberror
import WeiDian.models.model as models
from WeiDian.models.base_model import BaseModel
from WeiDian import logger
sys.path.append(os.path.dirname(os.getcwd()))


def close_session(fn):
    def inner(self, *args, **kwargs):
        try:
            result = fn(self, *args, **kwargs)
            if isinstance(result, list) or isinstance(result, BaseModel):
                self.session.expunge_all()
            # if not 'update' in fn.__name__ and not 'delete' in fn.__name__ and not 'stop' in fn.__name__:
            #     self.session.expunge_all()
            self.session.commit()
            return result
        except Exception as e:
            print("DBERROR" + e.message)
            logger.exception("DBERROR")
            self.session.rollback()
            # raise e
            raise dberror()
        finally:
            self.session.close()
    return inner


# service 基础类
class SBase(object):
    def __init__(self):
        try:
            self.session = DBSession.db_session()
        except Exception as e:
            # raise e
            from WeiDian.common.loggers import generic_log
            generic_log(e)
            print(e.message)

    @close_session
    def add_model(self, model_name, **kwargs):
        print(model_name)
        if not getattr(models, model_name):
            print("model name = {0} error ".format(model_name))
            return
        model_bean = eval(" models.{0}()".format(model_name))
        for key in model_bean.__table__.columns.keys():
            if key in kwargs:
                setattr(model_bean, key, kwargs.get(key))
        self.session.add(model_bean)

    @contextmanager
    def auto_commit(self, func=None, args=[]):
        try:
            yield self.session
            self.session.commit()
        except Exception as e:
            if func is not None:
                func(*args)
            self.session.rollback()
            generic_log(e)
            raise e
        finally:
            self.session.close()
