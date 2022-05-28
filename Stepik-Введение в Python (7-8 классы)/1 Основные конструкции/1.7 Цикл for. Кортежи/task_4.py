'''
Цикл с условием
   С клавиатуры вводятся числа a и b. Необходимо вывести те числа на полуинтервале [a; b) или [b; a), которые являются четными и дают остаток 1 при делении на 7.

        Примечание: запись [a; b) означает промежуток из чисел от a включительно до b невключительно. В языке Python это соответствует записи range(a, b). Аналогично, промежуток [b; a) соответствует записи range(b, a).
'''

a = int(input())
b = int(input())
minimum = None
maximum = None
if a > b:
    minimum = b
    maximum = a
elif a < b:
    minimum = a
    maximum = b

for i in range(minimum, maximum):
    if i % 2 == 0 and i % 7 == 1:
        print(i)
