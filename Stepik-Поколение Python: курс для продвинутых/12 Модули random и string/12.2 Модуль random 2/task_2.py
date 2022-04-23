'''
Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter, где Letter – заглавная буква английского алфавита, Number – число от 00 до 9999 (включительно).

Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает случайный корректный почтовый индекс Латверии.
'''
# AB23_56VG
import random
import string


def generate_index():
    letter_1 = random.choice(string.ascii_uppercase)
    letter_2 = random.choice(string.ascii_uppercase)
    letter_3 = random.choice(string.ascii_uppercase)
    letter_4 = random.choice(string.ascii_uppercase)
    digit_1 = random.randint(0, 99)
    digit_2 = random.randint(0, 99)
    return f"{letter_1}{letter_2}{digit_1}_{digit_2}{letter_3}{letter_4}"


print(generate_index())
