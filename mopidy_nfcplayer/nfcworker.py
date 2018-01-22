import threading
from pirc522 import RFID
import signal
import time
import logging

logger = logging.getLogger(__name__)

class NFCWorker():
    def __init__(self, frontend):
        self.frontend = frontend
        config = frontend.config
        self.rfid = RFID(pin_rst=config['pin_rst'],
                         pin_irq=config['pin_irq'],
                         pin_ce=0)
        self.util = self.rfid.util()
        self.util.debug = True
        self.running = True
        self.thread = threading.Thread(target=self.worker)
        self.thread.start()

    def worker(self):
        while self.running:
            self.rfid.wait_for_tag()

            (error, data) = self.rfid.request()
            if not error:
                logger.info("Tag Detected.")
        logger.warn("worker finished.")
