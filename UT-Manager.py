import sys
import keyboard

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Translater import Translater
from ScreenClipper import ScreenClipperPro



class Button(QPushButton):
    def __init__(self, parent=None, text='TEXT'):
        super().__init__(parent=parent)
        self.setStyleSheet('; color: white; border-radius: 10px; border: 1px solid rgb(30, 30, 30)')
        self.setText(text)
        # self.setMinimumSize(100, 50)
        self.setFixedSize(300, 100)
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
    




class Window(QMainWindow):
    MODULE = False

    def __init__(self, App=QApplication):
        super().__init__()
        self.App = App

        self.module = False

        self.desktop = QDesktopWidget()
        self.WIDTH   = self.desktop.width()
        self.HEIGHT  = self.desktop.height()
        
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SplashScreen)
        self.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        self.setWindowOpacity(0.001)
        self.setWindowIcon(QIcon(QPixmap('icon.png')))
        self.setWindowTitle('ScreenClipper Pro')

        self.sc = self.App.primaryScreen()
        self.image = self.sc.grabWindow(0)

        self.label = QLabel(self)
        self.label.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        self.label.setPixmap(self.image)
        self.setCentralWidget(self.label)

        self.blur = QGraphicsBlurEffect()
        self.blur.setBlurRadius(20)
        self.blur.setBlurHints(QGraphicsBlurEffect.QualityHint)
        self.label.setGraphicsEffect(self.blur)

        self.front = QWidget(self)
        self.front.setStyleSheet('background-color: rgba(0, 0, 0, 100)')
        self.front.setGeometry(0, 0, self.WIDTH, self.HEIGHT)


        self.anim_opacity = QVariantAnimation()
        self.anim_opacity.setStartValue(0.001)
        self.anim_opacity.setEndValue(1.0)
        self.anim_opacity.setDuration(200)
        self.anim_opacity.valueChanged.connect(self.setWindowOpacity)


        self.load_gui()
        self.show()
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

    def hide(self, module=False):
        self.MODULE = module
        self.anim_opacity.setDirection(QVariantAnimation.Backward)
        self.anim_opacity.start()

    def load_gui(self):
        self.main_layout = QHBoxLayout()
        self.front.setLayout(self.main_layout)

        self.button_layout = QVBoxLayout()
        self.button_layout.setAlignment(Qt.AlignCenter)
        self.button_layout.setSpacing(20)
        self.main_layout.addLayout(self.button_layout)

        self.screenclipper_button = Button(self, 'Вызвать скриншотер {PRINTSCREEN}')
        self.screenclipper_button.clicked.connect(lambda: self.hide('SC'))
        self.button_layout.addWidget(self.screenclipper_button)

        self.translater_button = Button(self, 'Перевести текст {CTRL + C + SHIFT}')
        self.translater_button.clicked.connect(lambda: self.hide('TR'))
        self.button_layout.addWidget(self.translater_button)

        self.exit_button = Button(self, 'Закрыть {ESC}')
        self.exit_button.clicked.connect(self.hide)
        self.button_layout.addWidget(self.exit_button)
        pass




if __name__ == "__main__":
    import sys
    import time
    
    App = QApplication([])

    MODULE = False

    while True:
        if keyboard.is_pressed('ctrl+c+shift'):
            print('Translater')
            window = Translater.Window(App=App)
            App.exec_()
            break

        if keyboard.is_pressed('prnt scrn'):
            print('ScreenClipper')
            window = ScreenClipperPro.Window(App=App)
            App.exec_()
            break
        
        if True:
            print('UT Manager')
            window = Window(App=App)
            App.exec_()
            
            if window.MODULE:
                if window.MODULE == 'TR':
                    window = Translater.Window(App=App)
                    App.exec_()
                elif window.MODULE == 'SC':
                    window = ScreenClipperPro.Window(App=App)
                    App.exec_()
            break

        time.sleep(0.1)
    sys.exit()