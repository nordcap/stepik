'''
Найти всех
Напомним, что строковый метод find('a') возвращает местоположение первого вхождения символа a в строке. Проблема заключается в том, что данный метод не находит местоположение всех символов а.

Напишите функцию с именем find_all(target, symbol), которая принимает два аргумента: строку target и символ symbol и возвращает список, содержащий все местоположения этого символа в строке.

Примечание 1. Если указанный символ не встречается в строке, то следует вернуть пустой список.
'''


# объявление функции
def find_all(target, symbol):
    arr = []
    n = target.count(symbol)
    start_ind = 0
    for _ in range(n):
        ind = target.find(symbol, start_ind)
        arr.append(ind)
        start_ind = ind + 1
    return arr


print(find_all('abcdabcaaa', 'a'))
print(find_all('abcadbcaaa', 'e'))
print(find_all('abcadbcaaa', 'd'))
