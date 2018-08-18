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
        self.fields = self.__dict__.keys()
        if '_sa_instance_state' in self.fields:
            self.fields.remove('_sa_instance_state')
        if 'fields' in self.fields:
            self.fields.remove('fields')
        return self.fields

    @auto_createtime
    @orm.reconstructor
    def __init__(self):
        pass

    def auto_creatdatatime(self):
        createtimes = filter(lambda k: 'createtime' in k, dir(self))
        if createtimes:
            createtime = createtimes[0]
            exists_time = getattr(self, createtime)
            if not exists_time:
                setattr(self, createtime, datetime.strftime(datetime.now(), format_for_db))

