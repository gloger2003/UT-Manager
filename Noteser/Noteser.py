from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import __BlurWindowWidget__
from __DataManager__ import DataManager


class Noteser(__BlurWindowWidget__.BlurWindowWidget):
    def __init__(self, parent: QWidget, data_manager: DataManager.DataManager):
        super().__init__(parent=parent)
        self.data  = data_manager
        self.notes = self.data.get_notes()

        self.load_gui()

    def load_gui(self):
        
        pass