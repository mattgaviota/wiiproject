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
    6: cwiid.RPT_UNKNOWN
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
        self.wiimote = cwiid.Wiimote(address)

    def get_state(self):
        return self.wm.state

    def get_mode(self):
        return self.wm.state['rpt_mode']

    def set_mode(self, mode):
        self.wm.state['rpt_mode'] = mode
    
    def get_type(self):
        return self.wm.state['rpt_mode']

    def set_type(self, ext_type):
        self.wm.state['rpt_mode'] = ext_type

    def get_battery(self):
        return self.wm.state['battery'] * 100 / cwiid.BATTERY_MAX
wm
    def set_led(self, number=1):
        self.wm.led = number

    def get_led(self):
        return self.wm.state['led']
        
    def toggle_rumble(self):
        if self.wm.state['rumble']:
            self.wm.rumble = 0
        else:
            self.wm.rumble = 1

    def get_error(self):
        return self.wm.state['error']

    def get_ir_pos(self):
        if self.wm.state['ir_src'] == cwiid.RPT_IR:
            return self.wm.state['ir_src']['pos']
        else:
            return (-1, -1)

    
