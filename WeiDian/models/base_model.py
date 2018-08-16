class BaseModel:
    def __getitem__(self, item):
        return getattr(self, item)

    def keys(self):
        return self.fields



