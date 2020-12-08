from . import __DataSubClass__




class Notes(__DataSubClass__.DataSubClass):
    def __init__(self, data: dict):
        super().__init__(data)
        pass

    def __getNotes__(self, ):
        return {'1': {'date_create': '21.01.2020','date_event': '22.01.2020','message': 'Нужно что-то сделать','state': True},

                '2': {'date_create': '21.01.2020','date_event': '22.01.2020','message': 'Нужно что-то сделать','state': True},

                '3': {'date_create': '21.01.2020','date_event' : '22.01.2020','message': 'Нужно что-то сделать','state': True}}