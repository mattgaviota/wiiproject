#!/usr/bin/env python
#-*- coding: utf-8 -*-

#imports
import cwiid, uinput
from time import sleep

#Constantes
BOTONES = {
    cwiid.BTN_1 : 'boton 1',
    cwiid.BTN_2 : 'boton 2',
    cwiid.BTN_A : 'boton A',
    cwiid.BTN_B : 'boton B',
    cwiid.BTN_DOWN : 'boton abajo',
    cwiid.BTN_HOME : 'boton home',
    cwiid.BTN_LEFT : 'boton izquierda',
    cwiid.BTN_MINUS : 'boton menos',
    cwiid.BTN_PLUS : 'boton más',
    cwiid.BTN_RIGHT : 'boton derecha',
    cwiid.BTN_UP : 'boton arriba'
    }

TECLAS = (
    uinput.KEY_A,
    uinput.KEY_B,
    uinput.KEY_L,
    uinput.KEY_R,
    uinput.KEY_U,
    uinput.KEY_D
    )

def apretartecla(device, tecla):
    device.emit(tecla, 1)
    sleep(0.09)
    device.emit(tecla, 0)

def main():
    device = uinput.Device(TECLAS)
    print 'Put Wiimote in discoverable mode now (press 1+2)...'
    w = cwiid.Wiimote()
    # Activar los botones
    w.rpt_mode = cwiid.RPT_BTN
    # Activo el led 1
    w.led = 1
    while( 1 ):
        if w.state['buttons'] == cwiid.BTN_A:
            apretartecla(device, uinput.KEY_A)
        elif w.state['buttons'] == cwiid.BTN_B:
            apretartecla(device, uinput.KEY_B)
        elif w.state['buttons'] == cwiid.BTN_HOME:
            exit(0)
        #sleep(0.09)
        
if __name__=='__main__':
    main()
