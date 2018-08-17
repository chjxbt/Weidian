# *- coding:utf8 *-
from datetime import datetime

from WeiDian.common.timeformat import format_for_db


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

    # 自动设置创建时间, 无效代码, 待改进
    def auto_creatdatatime(self):
        createtimes = map(lambda k: 'createtime' in k, self.__dict__.keys())

        if createtimes:
            createtime = createtimes[0]
            # self.createtime = datetime.strftime(datetime.now(), format_for_db)
            setattr(self, createtime, datetime.strftime(datetime.now(), format_for_db))




