#!/usr/bin/env python

import signal
import time
import array

from pirc522 import RFID
import ndef
from array import array

rdr = RFID()
util = rdr.util()
# Set util debug to true - it will print what's going on
util.debug = True

def dump(util, sectors=16):
    rdr = util.rfid
    if not util.is_tag_set_auth():
        print("NO AUTH, ERROR")
        return
    for i in range(1, sectors):
        for b in range(3):
            block = i * 4 + b
            error = util.do_auth(block)
            if not error:
                (error, line) = rdr.read(block)
                print("reading %d: '%s' / %s\n" % (block, str(bytearray(line)), str(line)))
            #print(str(bytearray(line)))
            else:
                print("Error on " + util.sector_string(block))

def read(util, sectors=16):
    rdr = util.rfid
    result = bytearray([])
    if not util.is_tag_set_auth():
        print("NO AUTH, ERROR")
        return
    for i in range(1, sectors):
        for b in range(3):
            block = i * 4 + b
            error = util.do_auth(block)
            if not error:
                (error, line) = rdr.read(block)
                #print("reading %d: '%s' / %s\n" % (block, str(bytearray(line)), str(line)))
                result = result + bytearray(line)
            #print(str(bytearray(line)))
            else:
                print("Error on " + util.sector_string(block))
    return result



while True:
    # Wait for tag
    rdr.wait_for_tag()

    # Request tag
    (error, data) = rdr.request()
    if not error:
        print("\nDetected")

        (error, uid) = rdr.anticoll()
        if not error:
            # Print UID
            print("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))

            # Set tag as used in util. This will call RFID.select_tag(uid)
            util.set_tag(uid)
            # Save authorization info (key B) to util. It doesn't call RFID.card_auth(), that's called when needed
            util.auth(rdr.auth_b, [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF])
            # Print contents of block 4 in format "S1B0: [contents in decimal]". RFID.card_auth() will be called now
            octets = read(util)
            print(octets)
            print(''.join('{:02x}'.format(x) for x in octets))
            for record in ndef.message_decoder(octets, errors='ignore'):
                print(record)
            # We must stop crypto
            util.deauth()

            time.sleep(1)

            exit()

