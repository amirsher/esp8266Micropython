
import usocket as socket
import machine
import time

GPIO_NUM = 4

#HTML to send to browsers
html = """<!DOCTYPE html>
<html>
<head>
<meta name='viewport' content='width=device-width', initial-scale='1'>
<title>Garage Door</title>
<style>
body {background-color:#333333;}.buttons{margin:15% auto;text-align:center;display:block;} a:active,a:link,a:visited{color:#333333;}svg{width:128px;height:128px;border:none;} use.ic-1{fill:#44eb47;}svg path{fill:inherit;}
</style>
</head>
<body>
<svg style='display:none;'><symbol id='ic'><path fill='#000000' d='m64 10.228-31.25 16.225-31.25 16.225h9.8371v70.858h-4.0636v4.2365h113.44v-4.2365h-4.054v-70.858h9.8371l-31.25-16.225-31.25-16.225zm-43.181 32.451h43.181 43.172v70.858h-86.353v-70.858zm4.0155 8.9629v6.6573h78.322v-6.6573h-78.322zm0 16.321v6.6573h78.322v-6.6573h-78.322zm0 15.14v6.6573h78.322v-6.6573h-78.322zm0 15.322v6.6669h78.322v-6.6669h-78.322z'/></svg>
<div class='buttons'>
<a class='click' href='/toggle?'><svg viewBox='0 0 128 128' xmlns:xlink='http://www.w3.org/1999/xlink'><use class='ic-1' xlink:href='#ic' x='0' y='0' /></svg></a>
</div>
</body>
</html>
"""

#Setup PINS

pin = machine.Pin(GPIO_NUM, machine.Pin.OUT)
pin.high()

#Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(2)
while True:
    conn, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)
    print("Content = %s" % str(request))
    request = str(request)
    ToggleDoor = request.find('/toggle?')
    print(ToggleDoor)
    #print("Data: " + str(ToggleDoor))
    if ToggleDoor == 6:
        print('Toggle Door')
        pin.low()
        time.sleep_ms(500)
        pin.high()
    response = html
    conn.send(response)
    conn.close()
