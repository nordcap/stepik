'''
Таблица-3
Дано натуральное число n \, (n \le 9)n (n≤ 9). Напишите программу, которая печатает таблицу сложения для всех чисел от 11 до nn в соответствии с примером.
Формат входных данных
На вход программе подается одно натуральное число.
Формат выходных данных
Программа должна вывести таблицу сложения для всех чисел от 11 до nn.
Примечание. В конце строки может быть пробел.
'''
n = int(input())

for i in range(1, n + 1):
    for j in range(1, 10):
        print(f"{i} + {j} = {i + j}")
    print()


