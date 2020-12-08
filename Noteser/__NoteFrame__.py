from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from __DataManager__ import DataManager



class NoteFrame(QFrame):
    def __init__(self, parent: QWidget, data_manager: DataManager.DataManager, note_data: dict):
        super().__init__(parent=parent)
        self.data_manager = data_manager
        self.note_data    = note_data
        
        self.setStyleSheet('''
            border-top: 1px solid qlineargradient(
                spread: reflect,
                x1    : 0,
                y1    : 0,
                x2    : 1,
                y2    : 0,
                stop  : 0 rgba(50, 50, 50, 255),
                stop  : 0.494318 rgba(250, 130, 0, 255),
                stop  : 1 rgba(50, 50, 50, 255)
            );

            background-color: qlineargradient(
                spread: pad,
                x1    : 0,
                y1    : 0,
                x2    : 0,
                y2    : 1,
                stop  : 0 rgba(10, 10, 10, 255),
                stop  : 1 rgba(50, 50, 50, 255)
            );

            border-bottom-right-radius: 20px;
            border-bottom-left-radius : 20px;
        ''')