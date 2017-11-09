import machine, neopixel
import time
import uos
import usocket

np = neopixel.NeoPixel(machine.Pin(4), 16)
#button = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)

def demo(np):
    n = np.n

    # cycle
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)

    # bounce
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(60)

    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (0, val, 0)
        np.write()
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (0, 0, val)
        np.write()
    # random
    for j in range(40):
        for i in range(n):
            np[i] = (randrange(0, 128), randrange(0, 128), randrange(0, 128))
        np.write()
        time.sleep_ms(100)
    # rainbow
    for j in range(128):
        for i in range(n):
            np[i] = (j, 0, 128-j)
        np.write()
        time.sleep_ms(40)
    for j in range(128):
        for i in range(n):
            np[i] = (128-j, j, 0)
        np.write()
        time.sleep_ms(40)
    for j in range(128):
        for i in range(n):
            np[i] = (0, 128-j, j)
        np.write()
        time.sleep_ms(40)
    # clear
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()
    
def clear():
    n = np.n
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()
    
def randrange(min_value, max_value):
    # Simple randrange implementation for ESP8266 uos.urandom function.
    # Returns a random integer in the range min to max.  Supports only 32-bit
    # int values at most.
    magnitude = abs(max_value - min_value)
    randbytes = uos.urandom(4)
    offset = int((randbytes[3] << 24) | (randbytes[2] << 16) | (randbytes[1] << 8) | randbytes[0])
    offset %= (magnitude+1)  # Offset by one to allow max_value to be included.
    return min_value + offset

def f1start():
    clear()
    time.sleep_ms(2000)
    np[0] = (128,0,0)
    np[7] = (128,0,0)
    np.write()
    time.sleep_ms(1000)    
    np[1] = (128,0,0)
    np[6] = (128,0,0)
    np.write()
    time.sleep_ms(1000)    
    np[2] = (128,0,0)
    np[5] = (128,0,0)
    np.write()
    time.sleep_ms(1000)    
    np[3] = (128,0,0)
    np[4] = (128,0,0)
    np.write()
    time.sleep_ms(randrange(4, 7)*1000)    
    clear()

def drag():
    clear()
    time.sleep_ms(2000)
    np[0] = (128,128,0)
    np[7] = (128,128,0)
    np.write()
    time.sleep_ms(400)    
    np[1] = (128,128,0)
    np[6] = (128,128,0)
    np.write()
    time.sleep_ms(400)    
    np[2] = (128,128,0)
    np[5] = (128,128,0)
    np.write()
    time.sleep_ms(400)    
    np[3] = (0,128,0)
    np[4] = (0,128,0)
    np.write()
    time.sleep_ms(5000)    
    clear()


def yellow():
    clear()
    np[9] = (128,128,0)
    np[11] = (128,128,0)
    np.write()

def green():
    clear()
    np[9] = (0,128,0)
    np[11] = (0,128,0)
    np.write()   

def red():
    clear()
    np[9] = (128,0,0)
    np[11] = (128,0,0)
    np.write()   

def maxred():
    clear()
    n = np.n
    for i in range(n):
        np[i] = (255, 0, 0)
    np.write()
    time.sleep_ms(2000)
    clear()

def blinkwhite():
    clear()
    n = np.n
    for i in range(n):
        np[i] = (128, 128, 128)
    np.write()
    time.sleep_ms(200)
    clear()


def finish():
    for i in range(10):
        clear()
        np[0] = (128,128,128)
        np[2] = (128,128,128)
        np[4] = (128,128,128)
        np[6] = (128,128,128)
        np[8] = (128,128,128)
        np[10] = (128,128,128)
        np[12] = (128,128,128)
        np[14] = (128,128,128)
        np.write()   
        time.sleep_ms(500)    
        clear()
        np[1] = (128,128,128)
        np[3] = (128,128,128)
        np[5] = (128,128,128)
        np[7] = (128,128,128)
        np[9] = (128,128,128)
        np[11] = (128,128,128)
        np[13] = (128,128,128)
        np[15] = (128,128,128)
        np.write()   
        time.sleep_ms(500)    
'''    clear()
demo(np)
time.sleep_ms(2000)    
f1start()
time.sleep_ms(2000)    
for i in range(10):
    yellow()
for i in range(10):
    print (randrange(4, 7))
    time.sleep_ms(10)
'''    
def ok(socket, query):
    socket.write("HTTP/1.0 OK\r\n\r\n")
    socket.write("<!DOCTYPE html>\r\n<html>\r\n<head>\r\n<meta name='viewport' content='width=device-width', initial-scale='1'><title>Starting Light</title>")
    socket.write("<link rel='manifest' href='manifest.json'><meta name='mobile-web-app-capable' content='yes'><style>body {background-color:#333333;}.buttons{margin:10% auto;text-align:center;display:block;} a:active,a:link,a:visited{color:#44eb47;fonf:24px;}</style>\r\n</head>\r\n<body>\r\n<div class='buttons'><a class='click' href='/f1?'>f1</a></div>\r\n<div class='buttons'><a class='click' href='/drag?'>drag</a></div>\r\n<div class='buttons'><a class='click' href='/red?'>red</a></div>\r\n<div class='buttons'><a class='click' href='/yellow?'>yellow</a></div>\r\n<div class='buttons'><a class='click' href='/green?'>green</a></div>\r\n<div class='buttons'><a class='click' href='/finish?'>finish</a></div>\r\n<div class='buttons'><a class='click' href='/maxred?'>maxred</a></div>\r\n<div class='buttons'><a class='click' href='/clear?'>clear</a></div>\r\n<div class='buttons'><a class='click' href='/demo?'>demo</a></div>\r\n</body>\r\n</html>")

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
        elif path == b"/f1":
            f1start()
            ok(socket, query)
        elif path == b"/drag":
            drag()
            ok(socket, query)
        elif path == b"/yellow":
            yellow()
            ok(socket, query)
        elif path == b"/green":
            green()
            ok(socket, query)
        elif path == b"/red":
            red()
            ok(socket, query)
        elif path == b"/maxred":
            maxred()
            ok(socket, query)
        elif path == b"/finish":
            finish()
            ok(socket, query)
        elif path == b"/clear":
            clear()
            ok(socket, query)
        elif path == b"/demo":
            demo(np)
            ok(socket, query)
        else:
            err(socket, "404", "Not Found")
    else:
        err(socket, "501", "Not Implemented")

clear()
server = usocket.socket()
server.bind(('0.0.0.0', 80))
server.listen(2)
blinkwhite()
while True:
    try:
        (socket, sockaddr) = server.accept()
        handle(socket)
    except:
        socket.write("HTTP/1.0 500 Internal Server Error\r\n\r\n")
        socket.write("<h1>Internal Server Error</h1>")
    socket.close()
#    first = button.value()
#    time.sleep(0.01)
#    second = button.value()
#    if not first and not second:
#        f1start()
    
