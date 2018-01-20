****************************
Mopidy-NFCPlayer
****************************

.. image:: https://img.shields.io/pypi/v/Mopidy-NFCPlayer.svg?style=flat
    :target: https://pypi.python.org/pypi/Mopidy-NFCPlayer/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/travis/cellcortex/mopidy-nfcplayer/master.svg?style=flat
    :target: https://travis-ci.org/cellcortex/mopidy-nfcplayer
    :alt: Travis CI build status

.. image:: https://img.shields.io/coveralls/cellcortex/mopidy-nfcplayer/master.svg?style=flat
   :target: https://coveralls.io/r/cellcortex/mopidy-nfcplayer
   :alt: Test coverage

Mopidy frontend extension for using an RC522 NFC reader to trigger playlists


Installation
============

Install by running::

    pip install Mopidy-NFCPlayer

Or, if available, install the Debian/Ubuntu package from `apt.mopidy.com
<http://apt.mopidy.com/>`_.


Configuration
=============

Before starting Mopidy, you must add configuration for
Mopidy-NFCPlayer to your Mopidy configuration file::

    [nfcplayer]
    # TODO: Add example of extension config


Project resources
=================

- `Source code <https://github.com/cellcortex/mopidy-nfcplayer>`_
- `Issue tracker <https://github.com/cellcortex/mopidy-nfcplayer/issues>`_

Troubleshooting
===============
The user running mopidy on Raspberry Pi needs to be in the 'spi' group.


Credits
=======

- Original author: `Thomas Kroeber <https://github.com/cellcortex`__
- Current maintainer: `Thomas Kroeber <https://github.com/cellcortex`__
- `Contributors <https://github.com/cellcortex/mopidy-nfcplayer/graphs/contributors>`_


Changelog
=========

v0.1.0 (UNRELEASED)
----------------------------------------

- Initial release.
