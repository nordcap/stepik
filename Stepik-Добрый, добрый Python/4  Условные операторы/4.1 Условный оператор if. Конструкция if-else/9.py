'''
Подвиг 9. Вводится шестизначное число. Определить, является ли оно счастливым. (Счастливым называют такое шестизначное число, в котором сумма его первых трех цифр равна сумме его последних трех цифр.). Вывести ДА, если счастливое и НЕТ - в противном случае.
'''

digits = list(map(int, input()))
begins = digits[:3]
ends = digits[3:]
if sum(begins) == sum(ends):
    print("ДА")
else:
    print("НЕТ")
