'''
Обратная польская нотация
    Обратная польская (или постфиксная) запись — это альтернативная запись арифметического выражение. В такой записи знак, который нужно применить к операндам, записывается после них, а не между ними. Так, выражение a + b превращается в a b +, а выражение a + (b - c) * d — в a b c - d * +. Напишите программу, которая вычисляет значение выражения, записанного в постфиксном виде. Используются только знаки +, -, *, /.
'''


def sum(op1, op2):
    return op1 + op2


def diff(op1, op2):
    return op1 - op2


def mul(op1, op2):
    return op1 * op2


def div(op1, op2):
    return op1 / op2


arr = input().split()
stack = []

for i in range(len(arr)):
    if len(stack) > 0:
        if arr[i] == '+':
            res_sum = sum(stack[-2], stack[-1])
            stack.pop()
            stack.pop()
            stack.append(res_sum)
        elif arr[i] == '-':
            res_diff = diff(stack[-2], stack[-1])
            stack.pop()
            stack.pop()
            stack.append(res_diff)
        elif arr[i] == '*':
            res_mul = mul(stack[-2], stack[-1])
            stack.pop()
            stack.pop()
            stack.append(res_mul)
        elif arr[i] == '/':
            res_div = div(stack[-2], stack[-1])
            stack.pop()
            stack.pop()
            stack.append(res_div)
        else:
            stack.append(int(arr[i]))  # добавляем цифру

    else:
        stack.append(int(arr[i]))  # добавляем первую цифру

print(*stack)
