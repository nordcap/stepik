"""
10-8. Кошки и собаки: создайте два файла с именами cats.txt и dogs.txt. Сохраните минимум
три клички кошек в  первом файле и  три клички собак во втором. Напишите программу,
которая пытается прочитать эти файлы и  выводит их содержимое на экран. Заключите
свой код в блок try-except для перехвата исключения FileNotFoundError и вывода понятного
сообщения об отсутствии файла. Переместите один из файлов в  другое место файловой
системы; убедитесь в том, что код блока except выполняется, как и положено.
"""
try:
    with open('cats.txt') as cat_f:
        for line in cat_f:
            print(line.strip())
except FileNotFoundError:
    print('cats.txt не найден')
try:
    with open('dogs.txt') as dog_f:
        for line in dog_f:
            print(line.strip())
except FileNotFoundError:
    print('dogs.txt не найден')
