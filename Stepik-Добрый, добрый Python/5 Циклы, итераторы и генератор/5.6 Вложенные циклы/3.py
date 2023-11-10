'''
Подвиг 3. Вводится натуральное число n. Необходимо найти все простые числа, которые меньше этого числа n, то есть, в диапазоне [2; n). Результат вывести на экран в строчку через пробел.
'''

n = int(input())

for simple in range(2, n):
    flag = True
    for i in range(2, simple):
        if simple % i == 0:
            flag = False
            break
    if flag:
        print(simple, end=' ')
