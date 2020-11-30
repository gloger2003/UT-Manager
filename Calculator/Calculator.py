from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


from .__Button__ import Button





class Window(QMainWindow):
    def __init__(self, App=QApplication):
        super().__init__()
        self.w_ = 400
        self.h_ = 600
        
        self.App = App

        self.desktop = QDesktopWidget()
        self.WIDTH   = self.desktop.width()
        self.HEIGHT  = self.desktop.height()

        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SplashScreen)
        self.setGeometry(self.WIDTH - self.w_, 0, 0, 0)
        self.setWindowOpacity(0.001)
        self.setWindowIcon(QIcon(QPixmap('icon.png')))
        self.setWindowTitle('Translater')

        self.main_frame = QFrame(self)
        self.main_frame.setStyleSheet('''
            background-color: rgb(40, 40, 40); 
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
        self.setCentralWidget(self.main_frame)

        self.anim = QVariantAnimation()
        self.anim.setStartValue(0.001)
        self.anim.setEndValue(1.0)
        self.anim.setDuration(500)
        self.anim.valueChanged.connect(self.setWindowOpacity)

        self.anim_size = QVariantAnimation()
        self.anim_size.setStartValue(QSize(0, 0))
        self.anim_size.setEndValue(QSize(self.w_, self.h_))
        self.anim_size.setDuration(300)
        self.anim_size.valueChanged.connect(self.setFixedSize)

        self.show()
        self.load_gui()



    def show(self):
        self.anim.setDirection(QVariantAnimation.Forward)
        self.anim.start()

        self.anim_size.setDirection(QVariantAnimation.Forward)
        self.anim_size.start()
        super().show()

    def hide(self):
        self.anim.setDirection(QVariantAnimation.Backward)
        self.anim.start()

        self.anim_size.setDirection(QVariantAnimation.Backward)
        self.anim_size.start()

    def setWindowOpacity(self, level):
        if level <= 0.01:
            self.close()
            self.App.quit()
        return super().setWindowOpacity(level)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.hide()
        return super().keyPressEvent(event)

    def mousePressEvent(self, event):
        self.__mousePressPos = None
        self.__mouseMovePos  = None
        if event.button() == Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos  = event.globalPos()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            currPos   = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()
            diff      = globalPos - self.__mouseMovePos
            newPos    = self.mapFromGlobal(currPos + diff)
            self.move(newPos)
            self.__mouseMovePos = globalPos
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos
            if moved.manhattanLength() > 3:
                event.ignore()
                return
        super().mouseReleaseEvent(event)


    def load_gui(self):
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(20)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.main_frame.setLayout(self.main_layout)

        blur = 10

        self.shadow_1 = QGraphicsDropShadowEffect()
        self.shadow_1.setBlurRadius(blur)
        self.shadow_1.setOffset(0, 0)
        self.shadow_1.setBlurRadius
        self.shadow_1.setColor(QColor(110, 250, 0))

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
        self.line_edit.setFocus()
        self.main_layout.addWidget(self.line_edit)
        pass








if __name__ == "__main__":
    import sys
    import time
    
    App = QApplication([])
    window = Window()
    App.exec_()
    sys.exit()