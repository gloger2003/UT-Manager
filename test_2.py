from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from datetime import datetime


date = datetime.now()

print(date.strftime('%Y/%m/%d %A %H:%M:%S'))