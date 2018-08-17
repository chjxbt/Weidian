# *- coding:utf8 *-
from datetime import datetime

from WeiDian.common.timeformat import format_for_db

class BaseModel:
    def __getitem__(self, item):
        return getattr(self, item)

    def keys(self):
        if self.fields == '__all__':
            self.fields = self.__dict__.keys()
            self.fields.remove('_sa_instance_state')
            self.fields.remove('fields')
        return self.fields

    def hide(self, *keys):
        for key in keys:
            self.fields.remove(key)
        return self

    def add(self, *keys):
        for key in keys:
            self.fields.append(key)

    # 自动设置创建时间, 无效代码, 待改进
    def __init__(self):
        createtimes = map(lambda k: 'createtime' in k, self.__dict__.keys())
        import ipdb
        ipdb.set_trace()
        if createtimes:
            createtime = createtimes[0]
            # self.createtime = datetime.strftime(datetime.now(), format_for_db)
            setattr(self, createtime, datetime.strftime(datetime.now(), format_for_db))

