'''
Сумма цифр
Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.
'''


# объявление функции
def print_digit_sum(num):
    s = str(num)
    arr = [int(i) for i in [*s]]
    print(sum(arr))


# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
