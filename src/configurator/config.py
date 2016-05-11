"""Module that contains the file tailer configuration class.

.. moduleauthor:: Thanos Vassilakis <thanosv@gmail.com>

"""

import argparse
import json
import os
import sys

import requests
import six


class Configurable(argparse.Namespace):
    """
    a configurable class
    """
    config_file = None
    config_url = None
    APP_PREFIX = ''

    def __init__(self, app_prefix=None):
        self.app_prefix = app_prefix if app_prefix else self.APP_PREFIX
        for k in os.environ:
            if k.startswith(self.app_prefix + '_'):
                setattr(self, k[len(self.app_prefix) + 1 if self.app_prefix else 0], os.environ[k])

    @classmethod
    def configure(cls, obj, **kwargs):
        cls.override(obj, **vars(cls))
        config_file = kwargs.pop('config_file', cls.config_file)
        if config_file:
            cls.override(obj, **cls.config_from_file(config_file))
        config_url = kwargs.pop('config_url', cls.config_url)
        if config_url:
            cls.override(obj, **cls.config_from_url(config_url))
        cls.override(obj, **kwargs)
        return obj

    @classmethod
    def config_from_file(cls, config_file_name):
        file_name, ext = os.path.splitext(os.path.abspath(config_file_name))
        configure_from_xxx = getattr(cls, 'config_from_' + ext[1:], cls.config_from_cfg)
        return configure_from_xxx(config_file_name)

    @classmethod
    def config_from_json(cls, config_file_name):
        return json.load(open(config_file_name, 'rb'))

    @classmethod
    def config_from_py(cls, pathname):
        if not os.path.isfile(pathname):
            raise IOError('File {0} not found.'.format(pathname))

        if sys.version_info[0] == 3 and sys.version_info[1] > 2:  # Python >= 3.3
            import importlib.machinery
            loader = importlib.machinery.SourceFileLoader('', pathname)
            mod = loader.load_module('')
        else:  # 2.6 >= Python <= 3.2
            import imp
            mod = imp.load_source('', pathname)
        return vars(mod)

    @classmethod
    def config_from_cfg(cls, config_file_name):
        config = six.moves.configparser.ConfigParser()
        config.read(config_file_name)
        return config._sections

    @classmethod
    def config_from_url(cls, url):
        return requests.get(url).json()

    @classmethod
    def override(cls, obj, **kwargs):
        for k in kwargs:
            setattr(obj, k, kwargs[k])
