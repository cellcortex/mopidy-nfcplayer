#!/usr/bin/env python
#coding utf-8

import signal
import time

from pirc522 import RFID
from array import array

import ndef

rdr = RFID()
util = rdr.util()
# Set util debug to true - it will print what's going on
util.debug = True

def write_url(rdr, url):
    record = ndef.UriRecord(url)
    encoder = ndef.message_encoder()
    print(record.data)
    encoder.send(None)
    encoder.send(record)
    results = list()
    results.append(encoder.send(None))
    b = bytearray()
    b = b.join(results)
    print(b)
    # chunk into 16 bytes
    n = 16
    chunks = [b[i:i + n] for i in xrange(0, len(b), n)]
    for i, chunk in enumerate(chunks):
        # extend a chunk of data to contain 16 bytes
        # XXX needed?
        if len(chunk) < 16:
            chunk.extend('\0' * (16 - len(chunk)))
        # XXX this should skip blocks 4, 8, 12, ..
        sector = 1 + (i // 3)
        block = sector * 4 + (i % 3)
        print("Writing %s on %d (%d) %d" % (chunk, block, sector, i))
        util.do_auth(block)
        rdr.write(block, chunk)


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
            # Now we can do some "lower-level" stuff with block 9
            #rdr.write(9, [0x01, 0x23, 0x45, 0x67, 0x89, 0x98, 0x76, 0x54, 0x32, 0x10, 0x69, 0x27, 0x46, 0x66, 0x66, 0x64])
            # We can rewrite specific bytes in block using this method. None means "don't change this byte"
            # Note that this won't do authorization, because we've already called do_auth for block 9
           # util.rewrite(9, [None, None, 0xAB, 0xCD, 0xEF])
            # This will write S2B1: [0x01, 0x23, 0xAB, 0xCD, 0xEF, 0x98, 0x76......] because we've rewritten third, fourth and fifth byte
            
            write_url(rdr, "https://stackoverflow.com/questions/183853/in-python-2-what-is-the-difference-between-and-when-used-for-division")
            util.deauth()

            time.sleep(1)

            exit()

