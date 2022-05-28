'''В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики: они говорили каким-то
странным набором звуков.
В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении подстановочный шифр, т.е.
заменяли каждый символ исходного сообщения на соответствующий ему другой символ. Биологи раздобыли ключ к шифру и теперь нуждаются в помощи:
Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки одинаковой длины,
на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита, после чего идёт строка,
которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки, которые
и передаём на вывод программы:
*d*%*d*#*d*
dacabac

Sample Input 1:
abcd
*d%#
abacabadaba
#*%*d*%
Sample Output 1:
*d*%*d*#*d*
dacabac

Sample Input 2:
dcba
badc
dcba
badc
Sample Output 2:
badc
dcba
'''


def getCipher(s, cipher, direct):
    if direct == 'direct':
        for elem in cipher:
            if s == elem[0]:
                return elem[1]
    elif direct == 'back':
        for elem in cipher:
            if s == elem[1]:
                return elem[0]


sym_input = input()  # символы исходного алфавита,
sym_output = input()  # символы конечного алфавита
str_encode = input()  # строка, которую нужно зашифровать переданным ключом,
str_decode = input()  # строка, которую нужно расшифровать.

code = list(zip(sym_input, sym_output))  # шифр

str_output_direct = ''
for s in str_encode:
    str_output_direct = str_output_direct + getCipher(s, code, 'direct')

str_output_back = ''
for s in str_decode:
    str_output_back = str_output_back + getCipher(s, code, 'back')

print(str_output_direct)
print(str_output_back)
