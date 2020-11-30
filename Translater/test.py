from googletrans import Translator

translator = Translator()
print(translator.translate('Hello', dest='ru').text)