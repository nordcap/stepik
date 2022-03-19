'''
Стоимость строки
Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, что один любой символ (в том числе пробел) стоит 6060 копеек. Ответ дайте в рублях и копейках в соответствии с примерами.
Формат входных данных
На вход программе подается строка текста.
'''

s = input()
length = len(s)
price = length * 0.6
print(str(int(price // 1)) + ' р. ' + str(round((price % 1)*100)) + ' коп.')
