'''
Подвиг 2. Вводятся: габариты изделия (целые числа): ширина, глубина, высота - в одну строчку через пробел. С помощью метода format, используя ключи в качестве имен переменных, сформировать строку: "Габариты: <ширина> x <глубина> x <высота>". Результат вывести на экран.
'''

a, b, c = input().split()
print("Габариты: {a} x {b} x {c}".format(a=a, b=b, c=c))
