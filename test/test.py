import ConfigParser,  os
import sys

print(sys.path)

def test(config_file_path):
    cf = ConfigParser.ConfigParser()
    cf.read(config_file_path)
    res = cf.get('divide', 'one_level')
    print res
    print cf.items('divide')
    cf.set('divide', 'one_level', 'ne3w')
    cf.write(open(config_file_path, "w"))


if __name__ == '__main__':
    # test('../WeiDian.common.divide_config.ini')
    test('./divide_config.ini')