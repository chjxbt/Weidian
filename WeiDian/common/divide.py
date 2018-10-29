# *- coding:utf8 *-
import sys
import os
import ConfigParser
sys.path.append(os.path.dirname(os.getcwd()))
from WeiDian import logger

class Partner(object):
    """佣金分成设置, 后续设置"""
    def __init__(self, config_file_path='WeiDian/config/divide_config.cfg'):
        self.cf = ConfigParser.ConfigParser()
        self.config_file_path = config_file_path
        self.cf.read(self.config_file_path)

    @property
    def one_level_divide(self):
        return float(self.cf.get('divide', 'one_level'))

    @one_level_divide.setter
    def one_level_divide(self, raw):
        self.cf.set('divide', 'one_level', raw)
        self.write_file()
    @property
    def two_level_divide(self):
        return float(self.cf.get('divide', 'two_level'))

    @two_level_divide.setter
    def two_level_divide(self, raw):
        self.cf.set('divide', 'two_level', raw)
        self.write_file()

    @property
    def three_level_divide(self):
        return float(self.cf.get('divide', 'three_level'))

    @three_level_divide.setter
    def three_level_divide(self, raw):
        self.cf.set('divide', 'three_level', raw)
        self.write_file()

    @property
    def access_token(self):
        return [
            self.cf.get("access_token", "access_token"),
            self.cf.get("access_token", "jsapiticket"),
            self.cf.get("access_token", "lasttime")]

    @access_token.setter
    def access_token(self, args):
        logger.info('set access token start')
        token, jsapiticket, updatetime = args[0], args[1], args[2]
        self.cf.set('access_token', 'access_token', token)
        self.cf.set("access_token", "lasttime", updatetime)
        self.cf.set("access_token", "jsapiticket", jsapiticket)
        self.write_file()
        logger.info('set access token start')

    def get_item(self, section, option):
        value = self.cf.get(section, option)
        return value

    def set_item(self, section, option, value):
        logger.info('set item start')
        if not isinstance(value, basestring):
            value = str(value).encode('utf8')
        elif isinstance(value, unicode):
            value = value.encode('utf8')
        self.cf.set(section, option, value)
        self.write_file()
        logger.info('set item success')
        return 'ok'

    def write_file(self):
        with open(self.config_file_path, "w") as cfg:
            self.cf.write(cfg)
        logger.info('file is closed')


if __name__ == '__main__':
    pass