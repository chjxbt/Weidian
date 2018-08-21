# *- coding:utf8 *-
from datetime import datetime

from sqlalchemy import orm

from WeiDian.common.timeformat import format_for_db


def auto_createtime(f):
    def inner(self, *args, **kwargs):
        res = f(self, *args, **kwargs)
        self.auto_creatdatatime()
        return res
    return inner


class BaseModel:

    def __getitem__(self, item):
        return getattr(self, item)

    def keys(self):
        return self.fields

    def hide(self, *keys):
        for key in keys:
            self.fields.remove(key)
        return self

    def add(self, *keys):
        for key in keys:
            self.fields.append(key)

    @property
    def all(self):
        return self.__table__.columns.keys()

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = []

    def auto_creatdatatime(self):
        createtimes = filter(lambda k: 'createtime' in k, self.__table__.columns.keys())
        if createtimes:
            createtime = createtimes[0]
            existsed_time = getattr(self, createtime)
            if not existsed_time:
                setattr(self, createtime, datetime.strftime(datetime.now(), format_for_db))

