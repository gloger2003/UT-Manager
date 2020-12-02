from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class TitleButton(QPushButton):
    def __init__(self, parent: QWidget, text: str):
        super().__init__(parent=parent)
        self.setText(text)
        self.setFixedSize(50, 40)
        self.setStyleSheet('''
            background-color: rgb(40, 40, 40);
            border          : 0px solid rgb(30, 30, 30);
            color           : rgb(210, 210, 210);
            border-radius   : 10px;
        ''')
        self.setFont(QFont('oblique', 12, QFont.Bold))

        duration = 200

        self.anim_font_size = QVariantAnimation()
        self.anim_font_size.setStartValue(12.0)
        self.anim_font_size.setEndValue(18.0)
        self.anim_font_size.setDuration(duration)
        self.anim_font_size.valueChanged.connect(self.resize_font)
        
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setColor(QColor(210, 150, 0))
        self.shadow.setBlurRadius(0)
        self.shadow.setOffset(0, 0)
        self.setGraphicsEffect(self.shadow)

        self.anim_shadow = QVariantAnimation()
        self.anim_shadow.setStartValue(0)
        self.anim_shadow.setEndValue(10)
        self.anim_shadow.setDuration(duration)
        self.anim_shadow.valueChanged.connect(self.shadow.setBlurRadius)
        pass


    def enterEvent(self, event: QEvent):
        # self.anim_font_size.setDirection(QVariantAnimation.Forward)
        # self.anim_font_size.start()

        self.anim_shadow.setDirection(QVariantAnimation.Forward)
        self.anim_shadow.start()
        return super().enterEvent(event)

    def leaveEvent(self, event: QEvent):
        # self.anim_font_size.setDirection(QVariantAnimation.Backward)
        # self.anim_font_size.start()

        self.anim_shadow.setDirection(QVariantAnimation.Backward)
        self.anim_shadow.start()
        return super().leaveEvent(event)

    def resize_font(self, num: int):
        self.setFont(QFont('oblique', num, QFont.Bold))
        pass
