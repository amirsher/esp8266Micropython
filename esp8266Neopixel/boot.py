# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)
import network
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
#    sta_if.connect('baffi','ddiiaannaa')
    sta_if.connect('MotoG4','12345678')
    while not sta_if.isconnected():
        pass
print('network config:', sta_if.ifconfig())
import gc
#import webrepl
#webrepl.start()
gc.collect()
