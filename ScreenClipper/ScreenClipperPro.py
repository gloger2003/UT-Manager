from io import BytesIO
from PyQt5.QtWidgets import QApplication

import os
import keyboard
import win32clipboard

from PIL import Image
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *

from __DataManager__ import DataManager


class Window(QtWidgets.QWidget):
    def __init__(self, App: QApplication, Data: DataManager.DataManager):
        super().__init__()
        self.App  = App
        self.Data = Data
        
        self.desktop = QtWidgets.QDesktopWidget()
        self.WIDTH   = self.desktop.width()
        self.HEIGHT  = self.desktop.height()
        
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SplashScreen)
        self.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        self.setWindowOpacity(0.001)
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap('icon.png')))
        self.setWindowTitle('ScreenClipper Pro')
        

        self.start = False
        self.im = [0, 0, 0, 0]

        self.sc = self.App.primaryScreen()

        self.image = self.sc.grabWindow(0)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        self.label.setPixmap(self.image)

        self.front = QtWidgets.QWidget(self)
        self.front.setStyleSheet('background-color: rgba(0, 0, 0, 100)')
        self.front.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        

        self.old_x = 0
        self.old_y = 0
        
        self.rectangable = QtWidgets.QLabel(self)
        self.rectangable.setStyleSheet('border: 2px solid red')
        self.rectangable.hide()

        self.byte_array = QByteArray()
        self.buffer = QBuffer(self.byte_array)
        self.buffer.open(self.buffer.ReadWrite)

        
        self.show()


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_rect = [event.x(), event.y()]
            self.start = True
        return super().mousePressEvent(event)



    def mouseMoveEvent(self, event):
        if self.start:
            self.update()
            self.rectangable.setGeometry(
                self.old_rect[0],
                self.old_rect[1],
                event.x() - self.old_rect[0] + 1,
                event.y() - self.old_rect[1] + 1
            )
            im = self.image.copy(
                self.old_rect[0] + 2,
                self.old_rect[1],
                event.x() - self.old_rect[0] + 1,
                event.y() - self.old_rect[1] + 1
            )
            self.rectangable.setPixmap(im)
            self.rectangable.show()

        return super().mouseMoveEvent(event)






    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
        
            self.start    = False
            self.new_rect = [event.x(), event.y()]
            
            self.im = [
                self.old_rect[0],
                self.old_rect[1],
                self.new_rect[0] - self.old_rect[0],
                self.new_rect[1] - self.old_rect[1]
            ]
            if self.im[2] >= 10 and self.im[3] >= 10:
    
                self.rectangable.setGeometry(
                    self.im[0],
                    self.im[1],
                    self.im[2],
                    self.im[3]
                )
                self.rectangable.show()
                self.image = self.image.copy(
                    self.im[0],
                    self.im[1],
                    self.im[2],
                    self.im[3]
                )

                self.image = self.image.toImage()
                self.image.save(f'./file.png', "PNG")


                image = Image.open(f'./file.png')

                output = BytesIO()
                image.convert("RGB").save(output, "BMP")
                data = output.getvalue()[14:]
                output.close()

                win32clipboard.OpenClipboard()
                win32clipboard.EmptyClipboard()
                win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
                win32clipboard.CloseClipboard()
                self.hide()

        return super().mouseReleaseEvent(event)


    def show(self):
        self.anim = QVariantAnimation()
        self.anim.setStartValue(0.001)
        self.anim.setEndValue(1.0)
        self.anim.setDuration(200)
        self.anim.valueChanged.connect(self.setWindowOpacity)
        self.anim.start()
        super().show()


    def hide(self):
        self.anim = QVariantAnimation()
        self.anim.setStartValue(1.0)
        self.anim.setEndValue(0.0)
        self.anim.setDuration(200)
        self.anim.valueChanged.connect(self.setWindowOpacity)
        self.anim.start()


    def setWindowOpacity(self, level):
        if level == 0:
            self.close()
            self.App.quit()
            os.system('del file.png')
        return super().setWindowOpacity(level)


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.hide()
        return super().keyPressEvent(event)






if __name__ == "__main__":
    import sys
    import time
    
    App = QtWidgets.QApplication([])
    
    try:
        with open('config.ini', 'r', encoding='utf-8') as f:
            PATH = f.readlines()[0]
    except FileNotFoundError:
        with open('config.ini', 'w', encoding='utf-8') as f:
            PATH = '.'
            f.write(PATH)

    while True:
        if keyboard.is_pressed('prnt scrn'):
            window = Window()
            window.close()
            App.exec_()
        
        time.sleep(0.1)

    sys.exit()
