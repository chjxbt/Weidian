# *- coding:utf8 *-
import sys
import os
import urlparse
import urllib
sys.path.append(os.path.dirname(os.getcwd()))


class GetUrlParams(object):
    
    @staticmethod
    def url_params_to_dict(url):
        query = urlparse.urlparse(url).query
        return dict([(k, v[0]) for k, v in urlparse.parse_qs(query).items()])

    @staticmethod
    def dict_to_url_params(paramsdict):
        return urllib.urlencode(paramsdict, doseq=True)