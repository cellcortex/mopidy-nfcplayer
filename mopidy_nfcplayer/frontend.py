from __future__ import unicode_literals
import pykka
from mopidy import core

logger = logging.getLogger(__name__)

class NFCPlayerFrontend(pykka.ThreadingActor, core.CoreListener):
    def __init__(self, config, core):
        super(NFCPlayerFrontend, self).__init__()
        self.core = core

    # Your frontend implementation
