#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from view import Ui_MainWindow

import os
import csv

class Controller(QMainWindow):
    """
    Controller des CSV-Tools
    Steuert den Ablauf des gesamten Tools
    """


    def __init__(self, parent=None):
        """
        Initialisiert das CSV-Tool
        """
        super().__init__(parent)
        # Instanz von UI erstellen
        self.view = Ui_MainWindow()
        self.view.setupUi(self)
        # Fenster anzeigen
        self.show()

    def select_file(self):
        """
        Öffnet einen Dateimanager um dem User zu ermöglichen, ein CSV-File auszuwählen
        und schreibt den Pfad dieses Files in ein Textfeld in der GUI
        """
        self.view.path_input.setText(QFileDialog.getOpenFileName()[0])

    def read_file(self):
        """
        Liest einen Dateipfad eines CSV-Files von der GUI ein und gibt den Inhalt in
        einer Tabelle in der GUI aus.
        """
        # User-Input abfragen
        path = self.view.path_input.text()
        filename, file_extension = os.path.splitext(path)
        if not os.path.exists(path):
            # Error: File nicht existent
            self.view.label_error.setText("Error: File not found!")
        elif file_extension.lower() != ".csv":
            # Error: Kein CSV-File
            self.view.label_error.setText("Error: Not a CSV-File!")
        else:
            # File einlesen
            with open(path, 'r') as f:
                reader = csv.reader(f)
                # Header setzen
                header = next(reader)
                self.view.table.setColumnCount(len(header))
                self.view.table.setHorizontalHeaderLabels(header)
                # Tabelle füllen
                for row in reader:
                    rowPosition = self.view.table.rowCount()
                    self.view.table.insertRow(rowPosition)
                    column = 0
                    for item in row:
                        self.view.table.setItem(rowPosition, column, QTableWidgetItem(str(item)))
                        column += 1
                self.view.label_error.setText("Finished reading!")

