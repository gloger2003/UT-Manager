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

        self.anim_style = QVariantAnimation()
        self.anim_style.setStartValue(QColor(40, 40, 40))
        self.anim_style.setEndValue(QColor(40, 40, 40))
        self.anim_style.setDuration(duration)
        self.anim_style.valueChanged.connect(self.restyle)
        
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setColor(QColor(0, 0, 0))
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
        self.anim_style.setDirection(QVariantAnimation.Forward)
        self.anim_style.start()

        self.anim_shadow.setDirection(QVariantAnimation.Forward)
        self.anim_shadow.start()
        return super().enterEvent(event)

    def leaveEvent(self, event: QEvent):
        self.anim_style.setDirection(QVariantAnimation.Backward)
        self.anim_style.start()

        self.anim_shadow.setDirection(QVariantAnimation.Backward)
        self.anim_shadow.start()
        return super().leaveEvent(event)

    def restyle(self, color: QColor):
        self.setStyleSheet(f'''
            background-color: rgb({color.red()}, {color.green()}, {color.blue()});
            border          : 0px solid rgb(30, 30, 30);
            color           : rgb(210, 210, 210);
            border-radius   : 10px;
        ''')
        pass
