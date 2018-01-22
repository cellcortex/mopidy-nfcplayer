from __future__ import unicode_literals
import pykka
from mopidy import core
import logging
from pirc522 import RFID
import threading

from .nfcworker import NFCWorker

logger = logging.getLogger(__name__)

class NFCPlayerFrontend(pykka.ThreadingActor, core.CoreListener):
    def __init__(self, config, core):
        super(NFCPlayerFrontend, self).__init__()
        logger.info(core.playlists.get_uri_schemes())
        lists = core.playlists.playlists.get()
        names = map(lambda x: x.uri, lists)
        logger.info(names)
        self.core = core
        self.config = config['nfcplayer']
        self.worker = NFCWorker(self)

    # Your frontend implementation
