from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import __StyleSetter__


class Button(QPushButton):
    def __init__(self, parent=None, text='TEXT'):
        super().__init__(parent=parent)
        self.background_color_style = 'rgba(50, 50, 50, 250)'
        self.setStyleSheet(f'background-color: {self.background_color_style}; color: white; border-radius: 10px; border: 1px solid rgb(30, 30, 30)')
        self.setText(text)
        # self.setMinimumSize(100, 50)
        self.setFixedSize(300, 100)
        # self.setMaximumHeight(200)
        self.setMouseTracking(True)

        self.setFont(QFont('oblique', 10, QFont.Bold))

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setColor(QColor(0, 0, 0))
        self.shadow.setBlurRadius(0)
        self.shadow.setOffset(0, 0)
        self.setGraphicsEffect(self.shadow)

        duration = 100

        self.anim_border = QVariantAnimation()
        self.anim_border.setStartValue(QColor(30, 30, 30))
        self.anim_border.setEndValue(QColor(210, 130, 0))
        self.anim_border.setDuration(duration)
        self.anim_border.valueChanged.connect(self.restyle_border)

        self.anim_shadow = QVariantAnimation()
        self.anim_shadow.setStartValue(0)
        self.anim_shadow.setEndValue(30)
        self.anim_shadow.setDuration(duration)
        self.anim_shadow.valueChanged.connect(self.shadow.setBlurRadius)


    def restyle_border(self, color: QColor):
        self.setStyleSheet(f'''
            background-color: {self.background_color_style};
            color: white; 
            border-radius: 10px; 
            border: 1px solid rgb({color.red()}, {color.green()}, {color.blue()})
        ''')
        # self.setStyleSheet(__StyleSetter__.set_style(self, 'border', f'1px solid rgb({color.red()}, {color.green()}, {color.blue()})'))
        pass


    def enterEvent(self, a0):
        self.anim_border.setDirection(QVariantAnimation.Forward)
        self.anim_border.start()

        self.anim_shadow.setDirection(QVariantAnimation.Forward)
        self.anim_shadow.start()
        return super().enterEvent(a0)

    def leaveEvent(self, a0):
        self.anim_border.setDirection(QVariantAnimation.Backward)
        self.anim_border.start()

        self.anim_shadow.setDirection(QVariantAnimation.Backward)
        self.anim_shadow.start()
        return super().leaveEvent(a0)