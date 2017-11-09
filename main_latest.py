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

pin = machine.Pin(GPIO_NUM)
pin.init(pin.OUT)
pin.low()

ap_if = network.WLAN(network.AP_IF)
if ap_if.active(): ap_if.active(False)
sta_if = network.WLAN(network.STA_IF)
if not ap_if.active(): sta_if.active(True)
if not sta_if.isconnected(): sta_if.connect(STA_SSID, STA_PSK)

def ok(socket, query):
    socket.write("HTTP/1.0 OK\r\n\r\n")
    socket.write("<!DOCTYPE html><html><head><meta name='viewport' content='width=device-width', initial-scale='1'><title>Garage Door</title><link rel='manifest' href='manifest.json'><meta name='mobile-web-app-capable' content='yes'><style>body {background-color:#333333;} .buttons {margin:15% auto;text-align:center;display:block;} a:active,a:link,a:visited {color:#333333;} svg {width:128px;height:128px;border:none;} use.ic-1 {fill:#44eb47;}svg path {fill:inherit;} </style></head><body><svg style='display: none;'><symbol id='ic'><path fill='#000000' d='m64 10.228-31.25 16.225-31.25 16.225h9.8371v70.858h-4.0636v4.2365h113.44v-4.2365h-4.054v-70.858h9.8371l-31.25-16.225-31.25-16.225zm-43.181 32.451h43.181 43.172v70.858h-86.353v-70.858zm4.0155 8.9629v6.6573h78.322v-6.6573h-78.322zm0 16.321v6.6573h78.322v-6.6573h-78.322zm0 15.14v6.6573h78.322v-6.6573h-78.322zm0 15.322v6.6669h78.322v-6.6669h-78.322z'/></svg><div class='buttons'><a class='click' href='/toggle?"+query.decode()+"'><svg viewBox='0 0 128 128' xmlns:xlink='http://www.w3.org/1999/xlink'><use class='ic-1' xlink:href='#ic' x='0' y='0' /></svg></a></div></body></html>")

def err(socket, code, message):
    socket.write("HTTP/1.0 "+code+" "+message+"\r\n\r\n")
    socket.write("<h1>"+message+"</h1>")

def handle(socket):
    (method, url, version) = socket.readline().split(b" ")
    if b"?" in url:
        (path, query) = url.split(b"?", 2)
    else:
        (path, query) = (url, b"")
    while True:
        header = socket.readline()
        if header == b"":
            return
        if header == b"\r\n":
            break

    if version != b"HTTP/1.0\r\n" and version != b"HTTP/1.1\r\n":
        err(socket, "505", "Version Not Supported")
    elif method == b"GET":
        if path == b"/":
            ok(socket, query)
        elif path == b"/toggle":
            pin.high()
            time.sleep_ms(500)
            pin.low()
            ok(socket, query)
        else:
            err(socket, "404", "Not Found")
    else:
        err(socket, "501", "Not Implemented")

server = usocket.socket()
server.bind(('0.0.0.0', 80))
server.listen(1)
while True:
    try:
        (socket, sockaddr) = server.accept()
        handle(socket)
    except:
        socket.write("HTTP/1.0 500 Internal Server Error\r\n\r\n")
        socket.write("<h1>Internal Server Error</h1>")
    socket.close()
    
    
    
