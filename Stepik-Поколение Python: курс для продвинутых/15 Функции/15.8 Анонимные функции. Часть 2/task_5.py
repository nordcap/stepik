'''
Напишите программу, которая с помощью встроенных функций filter() и sorted() выводит слова из списка words, имеющие длину ровно 66 символов. Слова следует вывести в алфавитном порядке на одной строке, разделив символом пробела.

Примечание. Используйте анонимную функцию в качестве критерия фильтрации.
'''

words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able',
         'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound',
         'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday',
         'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry',
         'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']

filter_result = filter(lambda x: len(x) == 6, words)
print(*sorted(filter_result))
