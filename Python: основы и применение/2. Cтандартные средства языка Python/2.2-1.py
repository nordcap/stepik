"""В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.

Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней, равное days.

Примечание:
Для решения этой задачи используйте стандартный модуль datetime.
Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta﻿ для прибавления дней к дате."""
from datetime import date, timedelta

input_str = input().split()
days = int(input())
diff_date = timedelta(days=days)
current_date = date(int(input_str[0]), int(input_str[1]), int(input_str[2]))
output_str = current_date + diff_date
print(output_str.year, output_str.month, output_str.day)
