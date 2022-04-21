'''
Дополните приведенный код, используя генератор, чтобы получить словарь result, состоящий из всех элементов словаря favorite_numbers , значения которых являются двузначными числами.

Примечание. Выводить содержимое словаря result не нужно.
'''

favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62,
                    'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654,
                    'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271,
                    'anna': 55, 'madlen': 876}

result = {k: favorite_numbers[k] for k in favorite_numbers if len(str(favorite_numbers[k])) == 2}

for key, value in result.items():
    print(key, ":", value)
