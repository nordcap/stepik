'''
Сумма цифр
Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.
'''


# объявление функции
def print_digit_sum(num):
    arr = [int(i) for i in [*num]]
    print(sum(arr))


# считываем данные
n = input()

# вызываем функцию
print_digit_sum(n)
