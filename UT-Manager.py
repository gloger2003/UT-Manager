import sys
import time
import keyboard

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import MainBlurWindow



if __name__ == "__main__":

    from Translater import Translater
    from ScreenClipper import ScreenClipperPro
    from Calculator import Calculator
    from WebViewer import WebViewer

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
            # window = __Window__.Window('Window', App, 600, 400)

            # window.show()
            # App.exec_()

            # window = MainBlurWindow.BlurWindow(App=App)
            # App.exec_()
            
            # if window.MODULE:
            #     if window.MODULE == 'TR':
            #         window = Translater.Window(App=App)
            #         App.exec_()
            #     elif window.MODULE == 'SC':
            #         window = ScreenClipperPro.Window(App=App)
            #         App.exec_()
            #     elif window.MODULE == 'CC':
            #         window = Calculator.Window(App=App)
            #         App.exec_()
            #     elif window.MODULE == 'WV':
            #         window = WebViewer.Window(App=App)
            #         App.exec_()
            window = WebViewer.Window(App=App)
            App.exec_() 
            break

        time.sleep(0.1)
    sys.exit()