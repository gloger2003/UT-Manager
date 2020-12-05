from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import __Window__
import __BlurWindow__
import __BlurButton__

from Noteser import Noteser



class BlurWindow(__BlurWindow__.BlurWindow):
    MODULE = False
    def __init__(self, App: QApplication):
        super().__init__(App)
        self.load_gui()
        self.show()
        pass

    def load_fast_menu_layout(self):
        self.fast_menu_layout = QVBoxLayout()
        self.main_layout.addLayout(self.fast_menu_layout)

        self.fast_menu_blur_widget = Noteser.Noteser(self)
        self.fast_menu_blur_widget.setMaximumHeight(self.WIDTH // 2)
        self.fast_menu_layout.addWidget(self.fast_menu_blur_widget)
        pass


    def load_button_layout(self):
        self.button_layout = QVBoxLayout()
        self.button_layout.setAlignment(Qt.AlignCenter)
        self.button_layout.setSpacing(20)
        self.main_layout.addLayout(self.button_layout)

        self.info_label = QLabel(self)
        self.info_label.setStyleSheet('background-color: rgba(0, 0, 0, 0); color: rgb(230, 115, 0); border: 0px; border-radius: 10px')
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setText('UT-Manager v0.2.8b')
        self.info_label.setFont(QFont('oblique', 20, QFont.Bold))
        self.info_label.setMinimumHeight(50)
        self.info_label.setMouseTracking(True)
        self.button_layout.addWidget(self.info_label)

        self.screenclipper_button = __BlurButton__.Button(self, 'Скриншотер')
        self.screenclipper_button.clicked.connect(lambda: self.hide('SC'))
        self.button_layout.addWidget(self.screenclipper_button)

        self.translater_button = __BlurButton__.Button(self, 'Переводчик')
        self.translater_button.clicked.connect(lambda: self.hide('TR'))
        self.button_layout.addWidget(self.translater_button)

        self.calculator_button = __BlurButton__.Button(self, 'Калькулятор')
        self.calculator_button.clicked.connect(lambda: self.hide('CC'))
        self.button_layout.addWidget(self.calculator_button)

        self.webviewer_button = __BlurButton__.Button(self, 'Веб-обозреватель')
        self.webviewer_button.clicked.connect(lambda: self.hide('WV'))
        self.button_layout.addWidget(self.webviewer_button)

        self.exit_button = __BlurButton__.Button(self, 'Закрыть')
        self.exit_button.clicked.connect(self.hide)
        self.button_layout.addWidget(self.exit_button)
        pass

    def load_noteser_layout(self):
        self.noteser_layout = QVBoxLayout()
        self.main_layout.addLayout(self.noteser_layout)

        self.noteser_blur_widget = Noteser.Noteser(self)
        self.noteser_blur_widget.setMaximumHeight(self.WIDTH // 2)
        self.noteser_layout.addWidget(self.noteser_blur_widget)
        pass

    def load_gui(self):
        self.main_layout = QHBoxLayout()
        self.main_layout.setContentsMargins(50, 50, 50, 50)
        self.front.setLayout(self.main_layout)

        self.load_fast_menu_layout()
        self.load_button_layout()
        self.load_noteser_layout()