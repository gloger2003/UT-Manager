import sqlite3
import datetime


class DataManager:
    def __init__(self):
        self.connect = sqlite3.connect("Data.sqlite")  # Подключение к БД


    def get_settings_dict(self):
        """Метод возвращает настройки в виде словаря"""
        pass


    def add_event(self, message, date_event, state=False):
        """Метод добавляет события по нескольким параметрам в таблицу"""

        cur = self.connect.cursor()  # Курсор БД

        # Обрабатываем дату под европейский формат
        date_create = '.'.join(str(datetime.date.today()).split('-')[::-1])

        # Вносим информацию о событие в БД
        cur.execute("""INSERT INTO event(date_create, date_event, message, state)
                       VALUES(?, ?, ?, ?)""",
                    (date_create, date_event, message, state))

        self.connect.commit()
