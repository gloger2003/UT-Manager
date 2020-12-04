# UT-Manager docs-string:
"""
Программа запускается при включении ОС, т.к. ее ярлык лежит в папке Автозагрузки.

Суть в том, что запускается изначально она в фоне (но на момент разработки это отключено в пользу тестов)
И при нажатии клавиши/сочетания клавиш будет открываться оверлей MainBlurWindow
В котором можно будет уже что то выбрать, либо, некоторые модули, можно будет запустить тоже через сочетание клавиш 

"""


# Как работают Главные модули (ГМ):
"""

Условия запуска:
[ Пользователь, например, решает открыть калькулятор (Calculator) ] 
=>
[ Переменная MODULE принимает значение 'CC' - это говорит о том, что нужно открыть ГМ Calculator ] 
=> 
[ Далее создаётся окно ГМ Window и запускается цикл событий App.exec_() ]
=>
[ Когда окно ГМ закрывается, то цикл событий завершается App.quit() ]
=>
[ Программа вновь слушает нажатия клавиш в фоне]


Наследование: 
[ __Window__ ]


Описание чистого __Window__:
[ Окно с тёмным фоном и rgb-краями, появляющееся в правом углу экрана и которое можно передвигать ]

"""




# Другие либки
import sys
import time
import keyboard

# Либки от PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Модуль Главного окна UT-Manager
import MainBlurWindow


# Если этот скрипт является основным (а не модулем), то импортируются ГМ и запускается цикл
if __name__ == "__main__":

    # =============================================================================
    from Translater import Translater           # Главный модуль переводчика
    from ScreenClipper import ScreenClipperPro  # Главный модуль скриншотера
    from Calculator import Calculator           # Главный модуль калькулятора
    from WebViewer import WebViewer             # Главный модуль веб-обозревателя
    # =============================================================================

    # Тут просто создаю приложение, которое потом буду передавать главным модулям, ибо они могут остановить цикл событий
    App = QApplication([])


    # =============================================================================
    MODULE = False  # Переменная, которая указывает какой модуль открыть:
                    # TR - Translater
                    # SC - ScreenClipper
                    # CC - Calculator
                    # WV - WebViewer
    # =============================================================================


    # Основной цикл, его задача отслеживать нажатия клавиш в фоне (задержка 0.1 сек, чтобы не нагружать ЦП)
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

            window = MainBlurWindow.BlurWindow(App=App)
            App.exec_()
            
            if window.MODULE: # Если MODULE не False, то:
                if window.MODULE == 'TR':
                    window = Translater.Window(App=App)
                    App.exec_()
                elif window.MODULE == 'SC':
                    window = ScreenClipperPro.Window(App=App)
                    App.exec_()
                elif window.MODULE == 'CC':
                    window = Calculator.Window(App=App)
                    App.exec_()
                elif window.MODULE == 'WV':
                    window = WebViewer.Window(App=App)
                    App.exec_()
            # window = WebViewer.Window(App=App)
            # App.exec_() 
            break

        time.sleep(0.1)
    sys.exit()