'''
Pretty print
Напишите функцию pretty_print(), которая выводит содержимое списка с рамкой.

Функция должна получать на вход один обязательный аргумент data – список, который следует вывести и два необязательных строковых односимвольных  аргумента side и delimiter и выводить содержимое списка в соответствии с примерами.

В случае если отсутствует аргумент side, то полагаем side='-', а если отсутствует аргумент delimiter, то полагаем delimiter='|'.
'''

def pretty_print(data, side='-', delimiter='|'):
    s = f' {delimiter} '.join(map(str, data))
    print(' ', end='')
    for _ in range(len(s)+2):
        print(side, end='')
    print()
    print(delimiter, end=' ')
    print(s, end=' ')
    print(delimiter)

    print(' ', end='')
    for _ in range(len(s)+2):
        print(side, end='')
    print()






pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')