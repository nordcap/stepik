'''
Подвиг 4. Объявите функцию с именем get_biggest_city, которой можно передавать произвольное количество названий городов через аргументы. Данная функция должна возвращать название города наибольшей длины. Если таких городов несколько, то первый найденный (из наибольших). Программу реализовать без использования сортировки.
'''


def get_biggest_city(*args):
    array = [len(x) for x in args]
    m_city = max(array)
    return [city for city in args if len(city) == m_city][0]


l = input().rsplit()

print(get_biggest_city(*l))
