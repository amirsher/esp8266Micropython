# Begin configuration
TITLE    = "Garage door"
GPIO_NUM = 4
STA_SSID = "baffi"
STA_PSK  = "ddiiaannaa"
# End configuration

import network
import machine
import usocket
import time

ap_if = network.WLAN(network.AP_IF)
if ap_if.active(): ap_if.active(False)
sta_if = network.WLAN(network.STA_IF)
if not ap_if.active(): sta_if.active(True)
if not sta_if.isconnected(): sta_if.connect(STA_SSID, STA_PSK)

pins = [machine.Pin(i, machine.Pin.IN) for i in (0, 2, 4, 5, 12, 13, 14, 15)]

html = """<!DOCTYPE html>
<html>
    <head> <title>ESP8266 Pins</title> </head>
    <body> <h1>ESP8266 Pins</h1>
        <table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>
    </body>
</html>
"""

import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break
    rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
    response = html % '\n'.join(rows)
    cl.send(response)
    cl.close()
