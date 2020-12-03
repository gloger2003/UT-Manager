from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from googletrans.client import Translator


from .__Button__ import Button
from math import *


import __Window__


class Window(__Window__.Window):
    def __init__(self, App: QApplication):
        super().__init__('Translater', App, 400, 600)
        self.show()
        self.load_gui()
        pass

    def get_result(self):
        text = self.line_edit.text()
        try:
            result = eval(text.lower())  # Изменил text ->  text.lower()
        except:
            result = 'Упс...'
        self.line_edit.setText(str(result))

    def load_gui(self):
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(20)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.main_frame.setLayout(self.main_layout)

        blur = 20

        self.shadow_1 = QGraphicsDropShadowEffect()
        self.shadow_1.setBlurRadius(blur)
        self.shadow_1.setOffset(0, 0)
        self.shadow_1.setColor(QColor(0, 0, 0))

        self.shadow_2 = QGraphicsDropShadowEffect()
        self.shadow_2.setBlurRadius(blur)
        self.shadow_2.setOffset(0, 0)
        self.shadow_2.setColor(QColor(0, 0, 0))
        
        self.global_font = QFont('oblique', 12, QFont.Bold)

        self.line_edit = QLineEdit(self)
        self.line_edit.setStyleSheet('border-radius: 10px; border: 0px; background-color: rgb(30, 30, 30); color: rgb(210, 210, 210)')
        self.line_edit.setGraphicsEffect(self.shadow_1)
        self.line_edit.setMinimumHeight(50)
        self.line_edit.setFont(self.global_font)
        self.line_edit.returnPressed.connect(self.get_result)
        self.line_edit.setFocus()
        self.main_layout.addWidget(self.line_edit)


if __name__ == "__main__":
    import sys
    import time
    
    App = QApplication([])
    window = Window()
    App.exec_()
    sys.exit()
