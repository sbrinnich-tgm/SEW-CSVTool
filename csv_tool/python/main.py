#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

from controller import Controller

if __name__ == "__main__":
    # QT Applikation erstellen
    app = QApplication(sys.argv)
    # Controller instanziieren
    c = Controller()
    # Programm beenden
    sys.exit(app.exec_())
