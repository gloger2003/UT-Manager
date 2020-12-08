import sqlite3
import datetime
import json

from . import CONSTANTS as const
from . import __Settings__



class DataManager:
    def __init__(self):
        self.__data__ = const.DATA
        self.__data__ = self.__getDataFromJson__()
        self.Settings = __Settings__.Settings(self.__data__['Settings'])


    def __getDataFromJson__(self):
        """Получает данные из файла"""
        # data = const.DATA
        data = self.__data__
        try:
            with open(const.FILENAME, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError or json.decoder.JSONDecodeError:
            self.save()
        return data


    def save(self):
        """Сохраняет все данные в файл или Создаёт новый файл с шаблоном"""
        with open(const.FILENAME, 'w', encoding='utf-8') as f:
            json.dump(self.__data__, f)