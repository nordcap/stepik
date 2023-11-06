'''
Подвиг 4. Вводится четырехзначное целое положительное число. Подумайте, как можно определить итератор для перебора его цифр. Выведите цифры этого введенного числа (с помощью итератора) в одну строчку через пробел.
'''

numbers=input()
iterable = iter(numbers)
print(next(iterable), end=' ')
print(next(iterable), end=' ')
print(next(iterable), end=' ')
print(next(iterable))
