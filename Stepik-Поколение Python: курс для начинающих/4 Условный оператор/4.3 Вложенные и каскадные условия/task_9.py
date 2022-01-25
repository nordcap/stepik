'''
Пересечение отрезков 🌶️🌶️
'''

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# [a1,b1] [a2, b2]

# пустое множество
if b1 < a2 or b2 < a1:
    print("пустое множество")
    exit(0)

# точка
if b1 == a2:
    print(b1)
elif b2 == a1:
    print(b2)
# отрезок
else:
    print(max(a1, a2), min(b1, b2))
