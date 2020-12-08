import os
import sys
from pprint import pprint


dirs = [
    '__DataManager__',
    'Calculator',
    'Noteser',
    'ScreenClipper',
    'Translater',
    'WebViewer',
    '.'
]

row = 0

for dir in dirs:
    files = os.listdir(dir)
    
    for file in files:
        if file[-3:] == '.py':
            print(file)

            with open(f'{dir}/{file}', 'r', encoding='utf-8') as f:
                text_list = f.readlines()

                for k in text_list:
                    if k != '' and k != '\n':
                        row += 1
                        print(k)
                pass

print(row)
