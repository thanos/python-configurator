========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
        | |landscape| |scrutinizer| |codeclimate|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/python-configurator/badge/?style=flat
    :target: https://readthedocs.org/projects/python-configurator
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/thanos/python-configurator.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/thanos/python-configurator

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/thanos/python-configurator?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/thanos/python-configurator

.. |requires| image:: https://requires.io/github/thanos/python-configurator/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/thanos/python-configurator/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/thanos/python-configurator/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/thanos/python-configurator

.. |landscape| image:: https://landscape.io/github/thanos/python-configurator/master/landscape.svg?style=flat
    :target: https://landscape.io/github/thanos/python-configurator/master
    :alt: Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/thanos/python-configurator/badges/gpa.svg
   :target: https://codeclimate.com/github/thanos/python-configurator
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/configurator.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/configurator

.. |downloads| image:: https://img.shields.io/pypi/dm/configurator.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/configurator

.. |wheel| image:: https://img.shields.io/pypi/wheel/configurator.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/configurator

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/configurator.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/configurator

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/configurator.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/configurator

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/thanos/python-configurator/master.svg?style=flat
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/thanos/python-configurator/


.. end-badges

A simple configuration library in python.

* Free software: BSD license

Installation
============

::

    pip install configurator

Documentation
=============

https://python-configurator.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
