'''
Подвиг 6. Дата некоторого дня характеризуется двумя натуральными числами: m (порядковый номер месяца) и n (число). По введенным m и n (в одну строку через пробел) определить:

а) дату предыдущего дня (принять, что m и n не характеризуют 1 января);
б) дату следующего дня (принять, что m и n не характеризуют 31 декабря).

В задаче принять, что год не является високосным. Вывести предыдущую дату и следующую дату (в формате: mm.dd, где m - число месяца; d - номер дня) в одну строчку через пробел.

P.S. Число дней в месяцах не високосного года, начиная с января: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
'''

arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m, n = map(int, input().split())
# а) дату предыдущего дня (принять, что m и n не характеризуют 1 января);
if 2 <= n <= arr[m - 1]:
    previous_month = m
    previous_day = n - 1
else:
    previous_month = m - 1
    previous_day = arr[m - 2]

# б) дату следующего дня (принять, что m и n не характеризуют 31 декабря).
if 1 <= n < arr[m - 1]:
    next_month = m
    next_day = n + 1
else:
    next_month = m + 1
    next_day = 1

print(
    f"{str(previous_month).rjust(2, '0')}.{str(previous_day).rjust(2, '0')} {str(next_month).rjust(2, '0')}.{str(next_day).rjust(2, '0')}")
