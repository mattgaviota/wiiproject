#!/usr/bin/env python
#-*- coding: utf-8 -*-

#imports
import cwiid
from time import sleep

def main():
    print 'Put Wiimote in discoverable mode now (press 1+2)...'
    w = cwiid.Wiimote()
    # Request nunchuk to be active.
    w.rpt_mode = cwiid.RPT_EXT
    # Turn on LED1 so we know we're connected.
    w.led = 1
    while( 1 ):
    # If nunchuk is active then dump the values.
        if w.state.has_key('nunchuk'):
            print 'Nunchuk: btns=%.2X stick=%r acc.x=%d acc.y=%d acc.z=%d' % (
                w.state['nunchuk']['buttons'], w.state['nunchuk']['stick'],
                w.state['nunchuk']['acc'][cwiid.X],
                w.state['nunchuk']['acc'][cwiid.Y],
                w.state['nunchuk']['acc'][cwiid.Z])
            if w.state['nunchuk']['buttons']:
                print "Exit button detected."
                exit( 0 )
            sleep( 0.5 )
        else:
            print "No Nunchuk"
            sleep( 0.5 )

if __name__=='__main__':
    main()
