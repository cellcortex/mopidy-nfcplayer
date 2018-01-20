from __future__ import unicode_literals
import pykka
from mopidy import core
import logging
from pirc522 import RFID

logger = logging.getLogger(__name__)

class NFCPlayerFrontend(pykka.ThreadingActor, core.CoreListener):
    def __init__(self, config, core):
        super(NFCPlayerFrontend, self).__init__()
        logger.log(PlaylistsController.get_uri_schemes())
        self.core = core
        self.rfid = RFID()
        self.util = self.rfid.util()
        self.util.debug = True

    # Your frontend implementation
