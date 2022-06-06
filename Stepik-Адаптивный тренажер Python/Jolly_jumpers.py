"""
Последовательность n>0n>0 целых чисел называется jolly jumper в случае, если значения абсолютных
 разностей последовательных элементов принимают все возможные значения между 11 и n−1n−1.
Например, последовательность 1 -3 -4 -1 1 является jolly jumper последовательностью, так как
 абсолютные разности равны 4 1 3 2, соответственно, а n−1=4n−1=4.
Будем считать, что последовательность из одного числа является jolly jumper.
Напишите программу, которая проверяет, является ли введённая последовательность jolly jumper.
Формат ввода:
Строка, содержащая 1≤n≤100001≤n≤10000 целых чисел, разделённых пробелом.
Формат вывода:
Одна строка, содержащая "Jolly" (без кавычек), если последовательность является jolly jumper и "Not jolly" в противном случае.
Sample Input 1:
1 -3 -4 -1 1
Sample Output 1:
Jolly
Sample Input 2:
1 3 5
Sample Output 2:
Not jolly
Sample Input 3:
4
Sample Output 3:
Jolly
"""
lst_n = [int(i) for i in input().split()]
n = len(lst_n)
lst_divN = []
for k in range(1, n):
    lst_divN.append(k)
flag = True
for i, v in enumerate(lst_n):
    if i < n - 1:
        d = abs(lst_n[i] - lst_n[i + 1])
        if lst_divN.count(d) == 0:
            flag = False
            break
        else:
            lst_divN.remove(d)

if flag:
    print('Jolly')
else:
    print('Not jolly')
