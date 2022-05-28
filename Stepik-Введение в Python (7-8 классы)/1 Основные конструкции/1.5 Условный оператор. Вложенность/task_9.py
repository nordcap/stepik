'''
Калькулятор
  Улучшим нашу программу из задачи "Две операции арифметики", чтобы программа могла принять на вход также знак умножения ("*") и деления ("/").
'''
n = float(input())
m = float(input())
op = input()
result = None
if op == "+":
    result = n + m
if op == "-":
    result = n - m
if op == "*":
    result = n * m
if op == "/":
    result = n / m

print(result)
