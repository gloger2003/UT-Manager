from typing import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QStyle

from qstylizer import parser




def set_style(widget: QWidget, attrib: str, value: Any):
    """
    Изменяет нужный атрибут qss-стиля и автоматически устанавливает его в виджет

    """

    qss = parser.parse(widget.styleSheet())
    qss['*'].border.setValue(value)
    return str(qss)