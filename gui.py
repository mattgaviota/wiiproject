#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import sys

# Importamos los módulos de Qt
from PyQt4 import QtCore, QtGui, uic, Qt

# Importamos el modulo de Wii
from wii import Wiiremote



class Main(QtGui.QDialog):
    """La ventana principal de la aplicación."""
    def __init__(self):
        QtGui.QDialog.__init__(self)

        # Cargamos la interfaz desde el archivo .ui
        uifile = os.path.join(os.path.abspath(
            os.path.dirname(__file__)), 'gui.ui')
        uic.loadUi(uifile, self)

    @QtCore.pyqtSlot()
    def on_btn_conectar_clicked(self):
        QtGui.QMessageBox.information(self, u'Conectar', u'Presiona 1 + 2')
        self.wm = Wiiremote()
        self.wm.set_led = 1
        self.spinbox_led.setValue = 1

def main():
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
