'''
Заменить цифры
    Замените каждую цифру n в строке на цифру (n + 1), причем цифра 9 должна меняться на 0. Выведите измененную строку и сумму полученных чисел.
'''

arr = list(input())
sum_digit = 0
for i, val in enumerate(arr):
    if val.isdigit():
        k = int(val) + 1
        k = 0 if k == 10 else k
        arr[i] = str(k)
        sum_digit += k

print("".join(arr))
print(sum_digit)
