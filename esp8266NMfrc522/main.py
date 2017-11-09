import mfrc522
from os import uname
import utime
try:
    import usocket as socket
except:
    import socket
try:
    import ustruct as struct
except:
    import struct

# (date(2000, 1, 1) - date(1900, 1, 1)).days * 24*60*60
NTP_DELTA = 3155673600

host = "pool.ntp.org"

rdr = mfrc522.MFRC522(0, 2, 4, 5, 14)

def time():
    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1b
    addr = socket.getaddrinfo(host, 123)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(1)
    res = s.sendto(NTP_QUERY, addr)
    msg = s.recv(48)
    s.close()
    val = struct.unpack("!I", msg[40:44])[0]
    tm = val - NTP_DELTA
    return utime.localtime(tm)



def do_read():
    (stat, tag_type) = rdr.request(rdr.REQIDL)

    if stat == rdr.OK:

        (stat, raw_uid) = rdr.anticoll()

        if stat == rdr.OK:
            print("New card detected")
            print("  - tag type: 0x%02x" % tag_type)
            return raw_uid

try:
    while True:
        ccc = do_read()
        print("%s  - uid     : 0x%02x%02x%02x%02x" % (time(), ccc[0], ccc[1], ccc[2], ccc[3]))

except KeyboardInterrupt:
    print("Bye")
