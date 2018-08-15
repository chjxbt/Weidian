# *- coding:utf8 *-
from datetime import datetime


def filter_lasting(o):
    """
    是否正在进行
    """
    start_time = datetime.strptime(o.ACstarttime, '%Y%m%d%H%M%S')
    end_time = datetime.strptime(o.ACendtime, '%Y%m%d%H%M%S')
    if start_time < datetime.now() < end_time:
        return True
    else:
        return False

