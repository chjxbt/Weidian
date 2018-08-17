from datetime import datetime

from WeiDian.common.timeformat import format_for_db


class BaseModel:
    def __getitem__(self, item):
        return getattr(self, item)

    def keys(self):
        return self.fields

    def __init__(self):
        self.create_time = datetime.strftime(datetime.now(), format_for_db)


