from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from __DataManager__ import DataManager

class BlurWindow(QMainWindow):
    MODULE = False

    def __init__(self, App: QApplication, Data: DataManager.DataManager):
        super().__init__()
        self.App    = App
        self.module = False
        self.Data   = Data
        
        scale = 200
        self.desktop = QDesktopWidget()
        self.WIDTH   = self.desktop.width() + scale
        self.HEIGHT  = self.desktop.height() + scale
        
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SplashScreen)
        self.setGeometry(-100, -100, self.WIDTH, self.HEIGHT)
        self.setWindowOpacity(0.001)
        self.setWindowIcon(QIcon(QPixmap('icon.png')))
        self.setWindowTitle('ScreenClipper Pro')

        self.sc           = self.App.primaryScreen()
        self.image        = self.sc.grabWindow(0)
        self.image        = self.image.scaled(self.WIDTH, self.HEIGHT)
        self.source_image = self.image

        self.image_label = QLabel(self)
        self.image_label.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        self.image_label.setPixmap(self.image)
        self.image_label.setAlignment(Qt.AlignCenter)
        # self.image_label.setScaledContents(True)
        self.setCentralWidget(self.image_label)

        self.front = QWidget(self)
        self.front.setStyleSheet('''
            background-color: rgba(10, 10, 10, 100); 
            color: white; 
            border-top: 1px solid qlineargradient(
                spread:pad, x1:0, y1:0, x2:1, y2:0, 
                stop:0 rgba(255, 0, 0, 255), 
                stop:0.166 rgba(255, 255, 0, 255), 
                stop:0.333 rgba(0, 255, 0, 255), 
                stop:0.5 rgba(0, 255, 255, 255), 
                stop:0.666 rgba(0, 0, 255, 255), 
                stop:0.833 rgba(255, 0, 255, 255), 
                stop:1 rgba(255, 0, 0, 255));
            border-bottom: 1px solid qlineargradient(
                spread:pad, x1:0, y1:0, x2:1, y2:0, 
                stop:0 rgba(255, 0, 0, 255), 
                stop:0.166 rgba(255, 255, 0, 255), 
                stop:0.333 rgba(0, 255, 0, 255), 
                stop:0.5 rgba(0, 255, 255, 255), 
                stop:0.666 rgba(0, 0, 255, 255), 
                stop:0.833 rgba(255, 0, 255, 255), 
                stop:1 rgba(255, 0, 0, 255));
            border-right: 1px solid qlineargradient(
                spread:pad, x1:0, y1:0, x2:0, y2:1, 
                stop:0 rgba(255, 0, 0, 255), 
                stop:0.166 rgba(255, 255, 0, 255), 
                stop:0.333 rgba(0, 255, 0, 255), 
                stop:0.5 rgba(0, 255, 255, 255), 
                stop:0.666 rgba(0, 0, 255, 255), 
                stop:0.833 rgba(255, 0, 255, 255), 
                stop:1 rgba(255, 0, 0, 255));
            border-left: 1px solid qlineargradient(
                spread:pad, x1:0, y1:0, x2:0, y2:1, 
                stop:0 rgba(255, 0, 0, 255), 
                stop:0.166 rgba(255, 255, 0, 255), 
                stop:0.333 rgba(0, 255, 0, 255), 
                stop:0.5 rgba(0, 255, 255, 255), 
                stop:0.666 rgba(0, 0, 255, 255), 
                stop:0.833 rgba(255, 0, 255, 255), 
                stop:1 rgba(255, 0, 0, 255));
        ''')
        self.front.setGeometry(scale // 2, scale // 2, self.WIDTH - scale, self.HEIGHT - scale)


        self.anim_opacity = QVariantAnimation()
        self.anim_opacity.setStartValue(0.001)
        self.anim_opacity.setEndValue(1.0)
        self.anim_opacity.setDuration(200)
        self.anim_opacity.valueChanged.connect(self.setWindowOpacity)
        
        self.front.setMouseTracking(True)
        self.front.mouseMoveEvent = self.mouseMove
        
        self.move_image(self.cursor().pos().x(), self.cursor().pos().y())
        pass


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.hide()
        return super().keyPressEvent(event)

    def setWindowOpacity(self, level):
        if level == 0.001:
            self.close()
            self.App.quit()
        return super().setWindowOpacity(level)


    def show(self):
        self.anim_opacity.setDirection(QVariantAnimation.Forward)
        self.anim_opacity.start()
        super().show()
        pass

    def hide(self, module=False):
        self.MODULE = module
        self.anim_opacity.setDirection(QVariantAnimation.Backward)
        self.anim_opacity.start()
        pass

    def move_image(self, x: int, y: int):
        move_speed = 0.05
        self.image = self.source_image.copy(QRect(
                self.image.rect().x() + int(x * move_speed),
                self.image.rect().y() + int(y * move_speed),
                self.image.width(),
                self.image.height()
            )
        )
        self.image_label.setPixmap(self.image)
        pass

    def mouseMove(self, event: QMouseEvent):
        self.move_image(event.x(), event.y())
        # print(self.image.size())
        # return super().mouseMoveEvent(event)
    