# *- coding:utf8 *-
import sys
import os
import ConfigParser
from WeiDian.common.single import singleton
sys.path.append(os.path.dirname(os.getcwd()))


@singleton
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
        self.cf.write(open(self.config_file_path, "w"))

    @property
    def two_level_divide(self):
        return float(self.cf.get('divide', 'two_level'))

    @two_level_divide.setter
    def two_level_divide(self, raw):
        self.cf.set('divide', 'two_level', raw)
        self.cf.write(open(self.config_file_path, "w"))

    @property
    def three_level_divide(self):
        return float(self.cf.get('divide', 'three_level'))

    @three_level_divide.setter
    def three_level_divide(self, raw):
        self.cf.set('divide', 'three_level', raw)
        self.cf.write(open(self.config_file_path, "w"))


if __name__ == '__main__':
    pass