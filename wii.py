#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Libreria para controla wiimote usando cwiid
'''

# imports
import cwiid

# Constantes

MODOS = {
    0: 'None',
    cwiid.RPT_ACC: 'RPT ACC',
    cwiid.RPT_BALANCE: 'RPT BALANCE',
    cwiid.RPT_BTN: 'RPT BTN',
    cwiid.RPT_CLASSIC: 'RPT CLASSIC',
    cwiid.RPT_EXT: 'RPT EXT',
    cwiid.RPT_IR: 'RPT IR',
    cwiid.RPT_MOTIONPLUS: 'RPT MOTIONPLUS',
    cwiid.RPT_NUNCHUK: 'RPT NUNCHUK',
    cwiid.RPT_STATUS: 'RPT STATUS'
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
    cwiid.BTN_1: '1',
    cwiid.BTN_2: '2',
    cwiid.BTN_A: 'A',
    cwiid.BTN_B: 'B',
    cwiid.BTN_DOWN: 'Abajo',
    cwiid.BTN_HOME: 'Home',
    cwiid.BTN_LEFT: 'Izquierda',
    cwiid.BTN_MINUS: 'Menos',
    cwiid.BTN_PLUS: 'Mas',
    cwiid.BTN_RIGHT: 'Derecha',
    cwiid.BTN_UP: 'Arriba'
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
        return MODOS[self.wiimote.state['rpt_mode']]

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
