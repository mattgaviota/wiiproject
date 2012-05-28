import cwiid
import time

wm = cwiid.Wiimote()

wm.rpt_mode = cwiid.RPT_IR

print wm.state['ir_src']

while True:
	if wm.state['ir_src'][0] != None:
		print " " * ( 97 - wm.state['ir_src'][0]['pos'][0] // 11 ) + "0"
		time.sleep(.2)
print 'fin'
