from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class Button(QPushButton):
    def __init__(self, parent=None, text='TEXT'):
        super().__init__(parent=parent)
        self.setStyleSheet('background-color: rgb(40, 40, 40); color: white; border-radius: 10px; border: 1px solid rgb(30, 30, 30)')
        self.setText(text)
        self.setMinimumSize(100, 50)
        # self.setMaximumHeight(200)

        self.setFont(QFont('oblique', 10, QFont.Bold))

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setColor(QColor(30, 30, 30))
        self.shadow.setBlurRadius(10)
        self.shadow.setOffset(0, 0)
        self.setGraphicsEffect(self.shadow)

        duration = 200

        self.anim_border = QVariantAnimation()
        self.anim_border.setStartValue(QColor(30, 30, 30))
        self.anim_border.setEndValue(QColor(210, 130, 0))
        self.anim_border.setDuration(duration)
        self.anim_border.valueChanged.connect(self.restyle_border)

        self.anim_shadow = QVariantAnimation()
        self.anim_shadow.setStartValue(QColor(40, 40, 40))
        self.anim_shadow.setEndValue(QColor(210, 130, 0))
        self.anim_shadow.setDuration(duration)
        self.anim_shadow.valueChanged.connect(self.shadow.setColor)


    def restyle_border(self, color=QColor):
        self.setStyleSheet(f'''
            color: white; 
            border-radius: 10px; 
            border: 1px solid rgb({color.red()}, {color.green()}, {color.blue()})
        ''')
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

        # self.setCursor()
        return super().leaveEvent(a0)