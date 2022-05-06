'''
Статистика по файлу
Вам доступен текстовый файл file.txt, набранный латиницей. Напишите программу, которая выводит количество букв латинского алфавита, слов и строк. Выведите три найденных числа в формате, приведенном в примере.
'''
import string

with open('file.txt', encoding='utf-8') as file:
    num_lines = len(file.readlines())
    file.seek(0)
    content = file.read()
    clean_content = content.replace('.', '').replace(',', '').replace(';', '').replace(':', '').replace('-', '').replace('?', '').replace('!', '').replace('(', '').replace(')', '').replace('"','').replace('\n', ' ')
    arr_words = [w for w in clean_content.split(' ')]

    sum_letters = 0
    for word in arr_words:
        for i in word:
            if i in string.ascii_letters:
                sum_letters += 1

    print("Input file contains:")
    print(f'{sum_letters} letters')
    print(f'{len(arr_words)} words')
    print(f'{num_lines} lines')