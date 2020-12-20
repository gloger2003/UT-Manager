from datetime import datetime

import __BlurWindowWidget__
from __DataManager__ import DataManager

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from . import __NoteFrame__



class Noteser(__BlurWindowWidget__.BlurWindowWidget):
    def __init__(self, parent: QWidget, Data: DataManager.DataManager):
        super().__init__(parent, Data)
        # self.notes = self.data_manager.get_notes()
        self.load_gui()
        pass


    def set_datetime(self):
        date = datetime.now()
        self.datetime_label.setText(date.strftime('%Y/%m/%d %A %H:%M:%S'))
        pass

    def load_datatime_label(self):
        self.datetime_label = QLabel()
        self.datetime_label.setAlignment(Qt.AlignCenter)
        self.datetime_label.setStyleSheet('border: 0px')
        self.datetime_label.setFont(QFont('oblique', 18, QFont.Bold))
        self.datetime_label.setMouseTracking(True)
        self.main_layout.addWidget(self.datetime_label)
        self.set_datetime()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.set_datetime)
        self.timer.start()
        pass


    def load_note_frames(self):
        for k in range(10):
            frame = __NoteFrame__.NoteFrame(None, self.Data, {})
            self.main_layout.addWidget(frame)
        # self.main_layout.setContentsMargins()
        pass
    
    
    def load_gui(self):
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.load_datatime_label()
        self.load_note_frames()
        pass
