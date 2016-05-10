"""Module that contains the file tailer configuration class.

.. moduleauthor:: Thanos Vassilakis <thanosv@gmail.com>

"""

import json
import os
import sys
import tempfile

import six
import six
import argparser

class O(object):
    """
    test object
    """


class Configurable(argparser.Namespace):
    """
    a configurable class
    """
    config_file = None
    config_url = None

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
        config = six.configparser.ConfigParser()
        config.read(config_file_name)
        return config._sections

    @classmethod
    def config_from_url(cls, url):
        return requests.get(url).json()

    @classmethod
    def override(cls, obj, **kwargs):
        for k in kwargs:
            setattr(obj, k, kwargs[k])


def test_config_by_args():
    class MyConfig(Configurable):
        timeout = 1
        highwater = .4
        watermark = 'tv'

    o = O()
    MyConfig.configure(o, timeouut=1, highwater=.7)
    assert (o.watermark == MyConfig.watermark)
    assert (o.timeout == 1)
    assert (o.highwater == .7)


def test_config_by_json():
    class MyConfig(Configurable):
        timeout = 1
        highwater = .4
        watermark = 'tv'

    o = O()
    with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as json_file:
        name = json_file.name
        json.dump(dict(timeouut=1, highwater=.7), json_file)
    MyConfig.configure(o, config_file=name)
    assert (o.watermark == MyConfig.watermark)
    assert (o.timeout == 1)
    assert (o.highwater == .7)


def test_config_from_url():
    class MyConfig(Configurable):
        only_backfill = False
        dont_backfill = False
        read_period = 1
        config_url = 'http://107.21.150.202:5984/config/tailchaser-test'

    o = O()
    MyConfig.configure(o)
    assert (o.dont_backfill == False)
    assert (o.read_period == 2)


def test_config_from_python():
    class MyConfig(Configurable):
        body = 'hello'
        objectType = 'Nothing'
        config_file = 'src\\tailchaser\\tailer.py'

    o = O()
    MyConfig.configure(o)
    assert (o.SIG_SZ == 256)
    assert (o.Tailer.READ_PERIOD == 1)


def test_config_by_cfg():
    class MyConfig(Configurable):
        timeout = 1
        highwater = .4
        watermark = 'tv'

    o = O()
    with tempfile.NamedTemporaryFile(suffix='.cfg', delete=False) as cfg_file:
        name = cfg_file.name
        cfg_file.write("""
[dev]
timeout = 21
highwater = .7
""")

    MyConfig.configure(o, config_file=name)
    assert (o.watermark == MyConfig.watermark)
    assert (o.dev['timeout'] == 21)
    assert (o.dev['highwater'] == .7)

