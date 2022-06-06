'''
Перестановки разрешены!
    Вводится натуральное число n, затем – n целых чисел. Для каждого из этих чисел переставьте его цифры так, чтобы получилось наибольшее по модулю число. Программа должна вывести число, которое дает максимальный результат после проделанных операций.
   '''


def max_digit(n):
    k = str(abs(int(n)))
    s = ''.join(sorted(list(k), reverse=True))
    return int(s)


n = int(input())
arr = [input() for i in range(n)]
arr_rev = list(map(max_digit, arr))
ind = arr_rev.index(max(arr_rev))
print(arr[ind])
