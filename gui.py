#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import sys

# Importamos los módulos de Qt
from PyQt4 import QtCore, QtGui, uic, Qt

# Importamos el modulo de Wii
from wii import Wiiremote, MODOS


class Main(QtGui.QDialog):
    """La ventana principal de la aplicación."""
    def __init__(self):
        QtGui.QDialog.__init__(self)

        # Cargamos la interfaz desde el archivo .ui
        uifile = os.path.join(os.path.abspath(
            os.path.dirname(__file__)), 'gui.ui')
        uic.loadUi(uifile, self)

        # ComboBox de los modos y su conexión
        self.cb_rpt_mode.addItems(MODOS)
        self.cb_rpt_mode.setCurrentIndex(0)
        self.cb_rpt_mode.activated.connect(self.cb_rpt_mode_changed)

    @QtCore.pyqtSlot()
    def on_btn_conectar_clicked(self):
        QtGui.QMessageBox.information(self, u'Conectar', u'Presiona 1 + 2')
        self.wm = Wiiremote()
        self.set_initial_state()
        self.btn_conectar.setEnabled(False)
        self.btn_habilitar.setEnabled(True)

    def set_initial_state(self):
        self.wm.set_led(1)
        self.spinbox_led.setValue(1)
        self.lcd_bateria.display(self.wm.get_battery())

    @QtCore.pyqtSlot()
    def on_spinbox_led_valueChanged(self):
        self.wm.set_led(self.spinbox_led.value())

    @QtCore.pyqtSlot()
    def cb_rpt_mode_changed(self):
        self.wm.set_mode(str(self.cb_rpt_mode.currentText()))

    @QtCore.pyqtSlot()
    def on_btn_cerrar_clicked(self):
        self.wm.cerrar_conexion()
        quit()

    @QtCore.pyqtSlot()
    def on_btn_habilitar_clicked(self):
        self.wm.cerrar_conexion()
        self.btn_conectar.setEnabled(True)
        self.btn_habilitar.setEnabled(False)

    @QtCore.pyqtSlot()
    def on_btn_rumble_clicked(self):
        self.wm.toggle_rumble()

def main():
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
