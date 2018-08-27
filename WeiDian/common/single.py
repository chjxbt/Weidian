def singleton(cls, *args, **kw):
    """ singleton decorator """
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton