'''
Необычные страны
Вам доступен текстовый файл population.txt с названиями стран и численностью их населения, разделенными символом табуляции '\t'.

Напишите программу выводящую все страны, название которых начинается с буквы 'G', численность населения которых больше чем 500 \, 000500000 человек, не меняя их порядок.
'''

with open('population.txt', encoding='utf-8') as file:
    arr = [city.strip().split('\t') for city in file.readlines()]
    result = list(filter(lambda x: x[0].startswith('G') and int(x[1]) > 500000, arr))
    for land in result:
        print(land[0])
