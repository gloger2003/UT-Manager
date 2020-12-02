from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import __Window__
import __BlurWindow__
import __BlurButton__



class BlurWindow(__BlurWindow__.Window):
    MODULE = False

    def __init__(self, App: QApplication):
        super().__init__(App)

        self.load_gui()
        self.show()
        pass


    def load_gui(self):
        self.main_layout = QHBoxLayout()
        self.front.setLayout(self.main_layout)

        self.button_layout = QVBoxLayout()
        self.button_layout.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)
        self.button_layout.setSpacing(20)
        self.main_layout.addLayout(self.button_layout)

        self.info_label = QLabel(self)
        self.info_label.setStyleSheet('background-color: rgba(0, 0, 0, 0); color: rgb(230, 115, 0); border: 0px')
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setText('UT-Manager v0.2.7b')
        self.info_label.setFont(QFont('oblique', 20, QFont.Bold))
        self.info_label.setMouseTracking(True)
        self.button_layout.addWidget(self.info_label)

        self.screenclipper_button = __BlurButton__.Button(self, 'Скриншотер {PRINTSCREEN}')
        self.screenclipper_button.clicked.connect(lambda: self.hide('SC'))
        self.button_layout.addWidget(self.screenclipper_button)

        self.translater_button = __BlurButton__.Button(self, 'Переводчик {CTRL + C + SHIFT}')
        self.translater_button.clicked.connect(lambda: self.hide('TR'))
        self.button_layout.addWidget(self.translater_button)

        self.calculator_button = __BlurButton__.Button(self, 'Калькулятор {CTRL + ALT + SHIFT}')
        self.calculator_button.clicked.connect(lambda: self.hide('CC'))
        self.button_layout.addWidget(self.calculator_button)

        self.webviewer_button = __BlurButton__.Button(self, 'Веб-обозреватель {CTRL + SHIFT + P}')
        self.webviewer_button.clicked.connect(lambda: self.hide('WV'))
        self.button_layout.addWidget(self.webviewer_button)

        self.exit_button = __BlurButton__.Button(self, 'Закрыть {ESC}')
        self.exit_button.clicked.connect(self.hide)
        self.button_layout.addWidget(self.exit_button)
        pass