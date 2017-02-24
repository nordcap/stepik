'''Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

https://stepic.org/media/attachments/course67/3.6.3/699991.txt

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
'''

import requests

r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
name_next_file = r.text
count = 0
while True:
    count += 1
    url_next_file = 'https://stepic.org/media/attachments/course67/3.6.3/' + name_next_file
    print(count, ':', url_next_file)
    r = requests.get(url_next_file)
    name_next_file = r.text
    if name_next_file.startswith('We'):
        print(name_next_file)
        break
