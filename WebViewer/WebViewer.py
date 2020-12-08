from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import __Window__
from . import  __TitleButton__

from __DataManager__ import DataManager



class Window(__Window__.Window):
    def __init__(self, App: QApplication, Data: DataManager.DataManager):
        screen = QDesktopWidget()
        w = screen.width()
        h = screen.height()
        super().__init__('WebViewer', App, Data, w, h)
        
        self.show()
        self.load_gui()
        pass


    # def mouseMoveEvent(self, a0: QMouseEvent):
    #     return QMainWindow(self).mouseMoveEvent(a0)

    def move_to_start_position(self):
        self.anim_move_to_start_position = QVariantAnimation()
        self.anim_move_to_start_position.setStartValue(self.pos())
        self.anim_move_to_start_position.setEndValue(QPoint(0, 0))
        self.anim_move_to_start_position.setDuration(100)
        self.anim_move_to_start_position.valueChanged.connect(self.move)
        self.anim_move_to_start_position.setDirection(QVariantAnimation.Forward)
        self.anim_move_to_start_position.start()
        pass


    def load_title_buttons(self):
        self.title_button_layout = QHBoxLayout()
        self.title_button_layout.setAlignment(Qt.AlignRight | Qt.AlignTop)
        self.title_button_layout.setContentsMargins(0, 5, 5, 0)
        self.title_button_layout.setSpacing(5)
        self.main_layout.addLayout(self.title_button_layout)

        self.start_position_title_button = __TitleButton__.TitleButton(self, '<>')
        self.start_position_title_button.clicked.connect(self.move_to_start_position)
        self.title_button_layout.addWidget(self.start_position_title_button)

        self.close_title_button = __TitleButton__.TitleButton(self, 'X')
        self.close_title_button.clicked.connect(self.hide)
        self.title_button_layout.addWidget(self.close_title_button)
        pass
    
    def load_gui(self):
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(20)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setAlignment(Qt.AlignTop)
        self.main_frame.setLayout(self.main_layout)

        self.load_title_buttons()
        pass








if __name__ == "__main__":
    import sys
    import time
    
    App = QApplication([])
    window = Window()
    App.exec_()
    sys.exit()