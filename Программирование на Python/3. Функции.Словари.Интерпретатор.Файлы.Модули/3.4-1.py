'''Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.
Sample Input:
a3b4c2e10b1
Sample Output:
aaabbbbcceeeeeeeeeeb
'''

import re

with open("sample_input", "r") as file_input:
    str_input = file_input.readline().strip()
    arr = re.split('(\d+)', str_input)
    list_output = [''.join(i[0] * int(i[1])) for i in zip(arr[::2], arr[1::2])]
    str_output = ''.join((str(i) for i in list_output))
    with open("sample_output.txt", "w") as file_output:
        file_output.write(str_output)
