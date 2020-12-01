import win32clipboard
import httpcore

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from googletrans import Translator

from .__Button__ import Button





class Window(QMainWindow):
    def __init__(self, App=QApplication):
        super().__init__()
        self.w_ = 600
        self.h_ = 400
        
        self.App = App

        self.desktop = QDesktopWidget()
        self.WIDTH   = self.desktop.width()
        self.HEIGHT  = self.desktop.height()


        win32clipboard.OpenClipboard()
        self.clipboard_text = ''
        try:
            self.clipboard_text = win32clipboard.GetClipboardData()
        except TypeError: pass
        win32clipboard.CloseClipboard()
        


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
        self.anim_size.setEndValue(QSize(600, 400))
        self.anim_size.setDuration(300)
        self.anim_size.valueChanged.connect(self.setFixedSize)

        self.show()
        self.load_gui()

        self.translator = Translator()



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
        if level == 1:
            self.translate_text()
        return super().setWindowOpacity(level)


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.hide()
        return super().keyPressEvent(event)

    def translate_text(self):
        text = self.text_line_edit.toPlainText()
        text = text.strip('\t')


        try:
            new_text = self.translator.translate(text, dest='ru')
            self.source_text_viewer.setText(new_text.text)
        except AttributeError as e:
            self.source_text_viewer.setText('')
        except httpcore._exceptions.ConnectError:
            self.source_text_viewer.setText('Ой, а я не могу подключиться к интернету ;(')
        pass

    def copy_to_clipboard(self):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(self.source_text_viewer.toPlainText(), win32clipboard.CF_UNICODETEXT)
        win32clipboard.CloseClipboard()
        pass

    def mousePressEvent(self, event):
           self.__mousePressPos = None
           self.__mouseMovePos = None
           if event.button() == Qt.LeftButton:
               self.__mousePressPos = event.globalPos()
               self.__mouseMovePos = event.globalPos()

           super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            # adjust offset from clicked point to origin of widget
            currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()
            diff = globalPos - self.__mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)
            self.__mouseMovePos = globalPos
        super().mouseMoveEvent(event)


    def mouseReleaseEvent(self, event):
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
        self.main_layout.setAlignment(Qt.AlignCenter)
        self.main_frame.setLayout(self.main_layout)


        blur = 20

        self.shadow_1 = QGraphicsDropShadowEffect()
        self.shadow_1.setBlurRadius(blur)
        self.shadow_1.setOffset(0, 0)
        self.shadow_1.setColor(QColor(0, 0, 0))

        self.shadow_2 = QGraphicsDropShadowEffect()
        self.shadow_2.setBlurRadius(blur)
        self.shadow_2.setOffset(0, 0)
        self.shadow_2.setColor(QColor(0, 0, 0))
        

        self.global_font = QFont('oblique', 12)

        self.text_line_edit = QTextEdit(self)
        self.text_line_edit.setStyleSheet('border-radius: 10px; border: 0px solid rgb(); background-color: rgb(30, 30, 30)')
        self.text_line_edit.setMaximumHeight(100)
        self.text_line_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text_line_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text_line_edit.setText(self.clipboard_text)
        self.text_line_edit.setAutoFormatting(QTextEdit.AutoAll)
        self.text_line_edit.setGraphicsEffect(self.shadow_1)
        self.text_line_edit.setFont(self.global_font)
        self.text_line_edit.setFocus()
        self.main_layout.addWidget(self.text_line_edit)

        self.source_text_viewer = QTextBrowser(self)
        self.source_text_viewer.setStyleSheet('border-radius: 10px; border: 0px solid rgb(); background-color: rgb(30, 30, 30)')
        self.source_text_viewer.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.source_text_viewer.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.source_text_viewer.setGraphicsEffect(self.shadow_2)
        self.source_text_viewer.setFont(self.global_font)
        self.main_layout.addWidget(self.source_text_viewer)


        self.button_layout = QHBoxLayout()
        self.button_layout.setAlignment(Qt.AlignCenter)
        self.button_layout.setSpacing(10)
        self.main_layout.addLayout(self.button_layout)

        self.copy_button = Button(self, 'Копировать')
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        self.button_layout.addWidget(self.copy_button)

        self.translate_button = Button(self, 'Перевести')
        self.translate_button.clicked.connect(self.translate_text)
        self.button_layout.addWidget(self.translate_button)

        self.clear_button = Button(self, 'Очистить')
        self.clear_button.clicked.connect(self.text_line_edit.clear)
        self.clear_button.clicked.connect(self.source_text_viewer.clear)
        self.button_layout.addWidget(self.clear_button)

        self.exit_button = Button(self, 'Закрыть')
        self.exit_button.clicked.connect(self.hide)
        self.button_layout.addWidget(self.exit_button)
        pass








# if __name__ == "__main__":
#     import sys
#     import time
    
#     App = QApplication([])

#     desktop = QDesktopWidget()
#     self.WIDTH   = desktop.self.width()
#     self.HEIGHT  = desktop.self.height()
    

#     while True:
#         if keyboard.is_pressed('ctrl+c+shift') or True:
#             print('clicked!')
#             window = Window()
#             App.exec_()
#             break
#         time.sleep(0.1)
#     sys.exit()
