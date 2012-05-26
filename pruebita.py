#!/usr/bin/env python
#-*- coding: utf-8 -*-

#imports
import cwiid, uinput
from time import sleep
from ev import MAPA

#Constantes
BOTONES = {
    cwiid.BTN_1 : uinput.KEY_L,
    cwiid.BTN_2 : uinput.KEY_U,
    cwiid.BTN_A : uinput.KEY_A,
    cwiid.BTN_B : uinput.KEY_B,
    cwiid.BTN_DOWN : 'boton abajo',
    cwiid.BTN_HOME : 'boton home',
    cwiid.BTN_LEFT : 'boton izquierda',
    cwiid.BTN_MINUS : uinput.KEY_D,
    cwiid.BTN_PLUS : uinput.KEY_R,
    cwiid.BTN_RIGHT : 'boton derecha',
    cwiid.BTN_UP : 'boton arriba'
    }



def apretartecla(device, tecla):
    device.emit(tecla, 1)
    #sleep(0.09)
    device.emit(tecla, 0)

def main():
    device = uinput.Device(MAPA)
    print 'Put Wiimote in discoverable mode now (press 1+2)...'
    w = cwiid.Wiimote()
    # Activar los botones
    w.rpt_mode = cwiid.RPT_BTN
    # Activo el led 1
    w.led = 1
    while( 1 ):
        if w.state['buttons'] != cwiid.BTN_HOME:
            tmp = w.state['buttons']
            try:
                apretartecla(device, BOTONES[tmp])
                for i in range(50):
                    if w.state['buttons'] == tmp:
                        sleep(.01)
                    else:
                        break
                while w.state['buttons'] == tmp:
                    apretartecla(device , BOTONES[tmp])
                    sleep(.01)
            except:
                sleep(.01)
        elif w.state['buttons'] == cwiid.BTN_HOME:
            exit(0)
        #sleep(0.09)
        
if __name__=='__main__':
    main()
