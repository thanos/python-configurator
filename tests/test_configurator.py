import json
import tempfile

from configurator.cli import main
from configurator.config import Configurable


class O(object):
    """
    test object
    """


def test_main():
    assert main([]) == 0


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
    assert (o.dont_backfill is False)
    assert (o.read_period == 2)


def test_config_from_python():
    code = """
SZ=10
SIG_SZ=10*SZ
class Tailer:
    READ_PERIOD = 1
"""

    class MyConfig(Configurable):
        body = 'hello'
        objectType = 'Nothing'

    with tempfile.NamedTemporaryFile(suffix='.py', delete=False) as python_file:
        name = python_file.name
        python_file.write(code)

    o = O()
    MyConfig.configure(o, config_file=name)
    assert (o.SIG_SZ == 100)
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
    assert (o.dev['timeout'] == '21')
    assert (o.dev['highwater'] == '.7')
