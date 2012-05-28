#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Libreria para controla wiimote usando cwiid
'''

# imports
import cwiid

# Constantes

MODOS = {
    1: cwiid.RPT_ACC,
    2: cwiid.RPT_BALANCE,
    3: cwiid.RPT_BTN,
    4: cwiid.RPT_CLASSIC,
    5: cwiid.RPT_EXT,
    6: cwiid.RPT_IR,
    7: cwiid.RPT_MOTIONPLUS,
    8: cwiid.RPT_NUNCHUK,
    9: cwiid.RPT_STATUS
}

TIPOS = {
    1: cwiid.EXT_BALANCE,
    2: cwiid.EXT_CLASSIC,
    3: cwiid.EXT_MOTIONPLUS,
    4: cwiid.EXT_NONE,
    5: cwiid.EXT_NUNCHUK,
    6: cwiid.EXT_UNKNOWN
}

BOTONES = {
    1:  cwiid.BTN_1,
    2:  cwiid.BTN_2,
    3:  cwiid.BTN_A,
    4:  cwiid.BTN_B,
    5:  cwiid.BTN_DOWN,
    6:  cwiid.BTN_HOME,
    7:  cwiid.BTN_LEFT,
    8:  cwiid.BTN_MINUS,
    9:  cwiid.BTN_PLUS,
    10: cwiid.BTN_RIGHT,
    11: cwiid.BTN_UP
}


# Clases

class Wiiremote():
    
    def __init__(self, address=''):
        try:
            self.wiimote = cwiid.Wiimote(address)
        except RuntimeError:
            print 'no se pudo realizar la conexion'

    def get_state(self):
        return self.wiimote.state

    def get_mode(self):
        return self.wiimote.state['rpt_mode']

    def set_mode(self, mode):
        self.wiimote.rpt_mode = mode
    
    def get_type(self):
        return self.wiimote.state['rpt_mode']

    def set_type(self, ext_type):
        self.wiimote.ext_type = ext_type

    def get_battery(self):
        return self.wiimote.state['battery'] * 100 / cwiid.BATTERY_MAX

    def set_led(self, number=1):
        self.wiimote.led = number

    def get_led(self):
        return self.wiimote.state['led']
        
    def toggle_rumble(self):
        if self.wiimote.state['rumble']:
            self.wiimote.rumble = 0
        else:
            self.wiimote.rumble = 1

    def get_error(self):
        return self.wiimote.state['error']

    def get_ir_pos(self, source=0):
        if self.get_mode() == cwiid.RPT_IR:
            if self.wiimote.state['ir_src'][source]:
                return self.wiimote.state['ir_src'][source]['pos']
            else:
                return None
        else:
            return None
