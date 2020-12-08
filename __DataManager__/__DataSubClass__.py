from __DataManager__ import DataManager




class DataSubClass:
    def __init__(self, data: dict):
        self.__data__ = data
        self.__dict__.update(data)
        pass

    def get_all_data(self):
        return self.__data__