"""
Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию,
после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.

Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

Обратите внимание, что на вход программе приходят вещественные числа.
Sample Input 1:
5.0
0.0
mod
Sample Output 1:
Деление на 0!
Sample Input 2:
-12.0
-8.0
*
Sample Output 2:
96.0
Sample Input 3:
5.0
10.0
/
Sample Output 3:
0.5
"""
num1 = float(input())
num2 = float(input())
op = input()

if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '/':
    if num2 == 0.0:
        result = 'Деление на 0!'
    else:
        result = num1 / num2
elif op == '*':
    result = num1 * num2
elif op == 'mod':
    if num2 == 0.0:
        result = 'Деление на 0!'
    else:
        result = num1 % num2
elif op == 'pow':
    result = num1 ** num2
elif op == 'div':
    if num2 == 0.0:
        result = 'Деление на 0!'
    else:
        result = num1 // num2

print(result)
