from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *




class Window(QMainWindow):
    def __init__(self, name: str, App: QApplication, w: int, h: int):
        super().__init__()
        self.w_ = w
        self.h_ = h
        
        self.App = App

        self.desktop = QDesktopWidget()
        self.WIDTH   = self.desktop.width()
        self.HEIGHT  = self.desktop.height()

        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SplashScreen)
        self.setGeometry(self.WIDTH - self.w_, 0, 0, 0)
        self.setWindowOpacity(0.001)
        self.setWindowIcon(QIcon(QPixmap('icon.png')))
        self.setWindowTitle(name)

        self.main_frame = QFrame(self)
        self.main_frame.setObjectName('main_frame')
        self.main_frame.setStyleSheet('''
            QFrame {
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
            }
        ''')
        self.setCentralWidget(self.main_frame)


        # from qstylizer import parser

        # qss = parser.parse(self.main_frame.styleSheet())
        # qss.QFrame.backgroundColor.setValue((4, 4, 4,))
        # print(qss.toString())
        # self.main_frame.setStyleSheet(qss.toString())

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

        self.anim_move = QVariantAnimation()
        self.anim_move.setStartValue(QPoint(self.x() - 500, -500))
        self.anim_move.setEndValue(QPoint(self.x(), 0))
        self.anim_move.setDuration(300)
        self.anim_move.valueChanged.connect(self.move)
        pass


    def show(self):
        self.anim.setDirection(QVariantAnimation.Forward)
        self.anim.start()

        self.anim_size.setDirection(QVariantAnimation.Forward)
        self.anim_size.start()

        self.anim_move.setDirection(QVariantAnimation.Forward)
        self.anim_move.start()
        super().show()

    def hide(self):
        self.anim.setDirection(QVariantAnimation.Backward)
        self.anim.start()

        self.anim_size.setDirection(QVariantAnimation.Backward)
        self.anim_size.start()

        self.anim_move.setStartValue(QPoint(self.x() - 500, -500))
        self.anim_move.setEndValue(QPoint(self.x(), self.y()))
        self.anim_move.setDirection(QVariantAnimation.Backward)
        self.anim_move.start()

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
            try:
                diff  = globalPos - self.__mouseMovePos
            except AttributeError:
                return super().mouseMoveEvent(event)
            newPos    = self.mapFromGlobal(currPos + diff)
            self.move(newPos)
            self.__mouseMovePos = globalPos
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        try:
            if self.__mousePressPos is not None:
                moved = event.globalPos() - self.__mousePressPos
                if moved.manhattanLength() > 3:
                    event.ignore()
                    return
        except AttributeError:
            super().mouseReleaseEvent(event)
        super().mouseReleaseEvent(event)