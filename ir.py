from wii import Wiiremote, MODOS
import time


print 'presione 1 y 2'
time.sleep(1)
wm = Wiiremote()

wm.set_mode(MODOS[6])
wm.set_led(1)

print wm.get_ir_pos()

while True:
    if wm.get_ir_pos() != None:
        print " " * ( 97 - wm.get_ir_pos()[0] // 11 ) + "0"
        time.sleep(.2)
print 'fin'
