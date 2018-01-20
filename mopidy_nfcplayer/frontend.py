from __future__ import unicode_literals
import pykka
from mopidy import core
import logging
from pirc522 import RFID

logger = logging.getLogger(__name__)

class NFCPlayerFrontend(pykka.ThreadingActor, core.CoreListener):
    def __init__(self, config, core):
        super(NFCPlayerFrontend, self).__init__()
        logger.info(core.playlists.get_uri_schemes())
        lists = core.playlists.playlists.get()
        names = map(lambda x: x.uri, lists)
        logger.info(names)
        self.core = core
        self.rfid = RFID(pin_rst=config['nfcplayer']['pin_rst'],
                         pin_irq=config['nfcplayer']['pin_irq'],
                         pin_ce=0)
        self.util = self.rfid.util()
        self.util.debug = True

    # Your frontend implementation
