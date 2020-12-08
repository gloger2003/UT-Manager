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



# Как работают Блюр-окна (БО)
"""
Условия запуска:
[ Нажатие пользователем соответствующей кнопки ]


Наследование:
[ __BlurWindow__ ]


Описание чистого __BlurWindow__:
[ Окно на весь экран с размытым изображением на заднем фоне и параллакс-эффектом ]

"""



# Анимации (Анимы)
"""
Для анимаций используется класс QVariantAnimation


Анимации начинаются с anim_{далее ключевое слово, обозначающее, что мы анимируем}
Например: 
    anim_shadow - анимируем тень
    anim_border - анимируем края


Все анимации работают в условиях цикла событий с помощью метода QVariantAnimation.start()

"""



# DataManager
"""
Задача DataManager - обработка информации всей программы (получение, хранение, обновление)


DataManager взаимодействует с БД Data.sqlite 
Ее можно открыть с помощью DB Browser for SQLite


DataManager должен уметь хранить данные как в виде словаря, так и виде атрибутов класса, например:
    В виде словаря: 
        DataManager.data['settings']['Calculator']['button_style']
    В виде атрибута:
        DataManager.Settings.Calculator.button_style


DataManager должен иметь метод save(), который будет сохранять ВСЕ данные в БД
После сохранения DataManager должен автоматически обновлять атрибуты, чтобы не оставались старые значения

"""



# Вспомогательные либки
import sys
import time
import keyboard

# Либки от PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Модуль Главного окна UT-Manager
import MainBlurWindow
from __DataManager__ import DataManager


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

    Data = DataManager.DataManager()


    # Основной цикл, его задача отслеживать нажатия клавиш в фоне (задержка 0.1 сек, чтобы не нагружать ЦП)
    while True:
        if keyboard.is_pressed('ctrl+c+shift'):
            print('Translater')
            window = Translater.Window(App=App, Data = Data)
            App.exec_()
            break

        if keyboard.is_pressed('prnt scrn'):
            print('ScreenClipper')
            window = ScreenClipperPro.Window(App=App, Data = Data)
            App.exec_()
            break
        
        if True:
            print('UT Manager')

            window = MainBlurWindow.MainBlurWindow(App=App, Data = Data)
            App.exec_()
            
            if window.MODULE: # Если MODULE не False, то:
                if window.MODULE == 'TR':
                    window = Translater.Window(App=App, Data = Data)
                    App.exec_()
                elif window.MODULE == 'SC':
                    window = ScreenClipperPro.Window(App=App, Data = Data)
                    App.exec_()
                elif window.MODULE == 'CC':
                    window = Calculator.Window(App=App, Data = Data)
                    App.exec_()
                elif window.MODULE == 'WV':
                    window = WebViewer.Window(App=App, Data = Data)
                    App.exec_()
            break

        time.sleep(0.1)
    sys.exit()