'''
Подвиг 4. Вводится строка со словами, разделенными пробелом. Необходимо первый пробел заменить на одинарную кавычку, а все остальные - на двойные. Результирующую строку отобразить на экране.
'''

s = input()
print(s.replace(' ', '\"').replace('\"', '\'', 1))
