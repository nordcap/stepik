'''
Подвиг 2. Вводятся три строчки стихотворения (каждая с новой строки). Сохранить его в виде вложенного списка с разбивкой по строкам и словам (слова разделяются пробелом). Результирующий список lst вывести на экран командой:

print(lst)
'''

a = input().split()
b = input().split()
c = input().split()
lst = []
lst.append(a)
lst.append(b)
lst.append(c)
print(lst)
