from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from __DataManager__ import DataManager



class NoteFrame(QFrame):
    def __init__(self, parent: QWidget, data_manager: DataManager.DataManager, note_data: dict):
        super().__init__(parent=parent)
        self.data_manager = data_manager
        self.note_data    = note_data
        self.setMouseTracking(True)
        # self.setFixedHeight(self.parent().height() // 5)

        self.setStyleSheet('''
            background-color: rgb(30, 30, 30);
            border: 1px solid rgb(30, 30, 30);
            border-bottom-right-radius: 20px;
            border-bottom-left-radius : 20px;
        ''')

        self.anim_border = QVariantAnimation()
        self.anim_border.setStartValue(QColor(30, 30, 30))
        self.anim_border.setEndValue(QColor(230, 150, 0))
        self.anim_border.setDuration(100)
        self.anim_border.valueChanged.connect(self.restyle_border)

    def restyle_border(self, color):
        self.setStyleSheet(f'''
            border: 1px solid rgb({color.red()}, {color.green()}, {color.blue()});
            background-color: rgb(30, 30, 30);
            border-bottom-right-radius: 20px;
            border-bottom-left-radius : 20px;
        ''')
        pass

    def enterEvent(self, a0: QEvent):
        self.anim_border.setDirection(QVariantAnimation.Forward)
        self.anim_border.start()
        return super().enterEvent(a0)

    def leaveEvent(self, a0: QEvent):
        self.anim_border.setDirection(QVariantAnimation.Backward)
        self.anim_border.start()
        return super().leaveEvent(a0)