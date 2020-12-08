from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import __BlurWindowWidget__
from __DataManager__ import DataManager


class Noteser(__BlurWindowWidget__.BlurWindowWidget):
    def __init__(self, parent: QWidget, Data: DataManager.DataManager):
        super().__init__(parent, Data)
        # self.notes = self.data_manager.get_notes()
        
        self.load_gui()
        pass


    def load_gui(self):
        self.main_layout = QVBoxLayout()
        # self.main_layout.setContentsMargins()
        pass