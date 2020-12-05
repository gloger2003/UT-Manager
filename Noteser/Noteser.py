from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import __BlurWindowWidget__



class Noteser(__BlurWindowWidget__.BlurWindowWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent=parent)