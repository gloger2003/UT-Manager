from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from __DataManager__ import DataManager



class BlurWindowWidget(QFrame):
    def __init__(self, parent: QWidget, Data: DataManager.DataManager):
        super().__init__(parent=parent)
        self.Data = Data

        self.setStyleSheet('background-color: rgb(50, 50, 50); border: 1px solid rgb(50, 50, 50); border-radius: 15px')
        self.setMouseTracking(True)

        self.anim_border = QVariantAnimation()
        self.anim_border.setStartValue(QColor(50, 50, 50))
        self.anim_border.setEndValue(QColor(60, 250, 20))
        self.anim_border.setDuration(200)
        self.anim_border.valueChanged.connect(self.restyle_border)
        pass

    def restyle_border(self, color: QColor):
        self.setStyleSheet(f'''
            background-color: rgb(50, 50, 50); 
            border: 1px solid {color.name()}; 
            border-radius: 15px''')
        pass

    def enterEvent(self, event: QEvent):
        self.anim_border.setDirection(QVariantAnimation.Forward)
        self.anim_border.start()
        return super().enterEvent(event)

    def leaveEvent(self, event: QEvent):
        self.anim_border.setDirection(QVariantAnimation.Backward)
        self.anim_border.start()
        return super().leaveEvent(event)