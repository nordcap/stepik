'''
Подвиг 7. Вводится список городов в одну строку через пробел. Если в этом списке присутствует город Москва, то удалить его. Вывести на экран результирующий список в виде строки с городами через пробел.
'''

arr = input().split()
if 'Москва' in arr:
    arr.remove('Москва')

print(*arr)
