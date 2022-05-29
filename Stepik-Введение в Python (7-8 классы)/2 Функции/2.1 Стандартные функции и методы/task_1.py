'''
Редактирование пробелов
    Вводится строка. Уберите все пробельные последовательности с концов строки и выведите их количество. Пользоваться методом split() нельзя.
'''

s = input()
old_length = len(s)
s1 = s.strip()
new_length = len(s1)
print(s1)
print(old_length - new_length)
