'''
Аве, Цезарь 🌶️
На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова. Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова). Строчные буквы при этом остаются строчными, а прописные – прописными.

Формат входных данных
На вход программе подается строка текста на английском языке.
'''
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
symbol = [" ", ",", ".", "!", "?"]

lan = 'e'
chif = 'ch'


def chru(chifr, n, l, fraza):
    arr_res = []
    if l == 'r':
        moch = 32
    if l == 'e':
        moch = 26
    if chifr == 'def':
        n = -n
    for i in range(len(fraza)):
        if fraza[i].isalpha():
            if fraza[i] == fraza[i].upper():
                for j in range(moch):
                    if moch == 32:
                        if fraza[i] == rus_upper_alphabet[j]:
                            arr_res.append(rus_upper_alphabet[(j + n) % moch])
                            break
                    if moch == 26:
                        if fraza[i] == eng_upper_alphabet[j]:
                            arr_res.append(eng_upper_alphabet[(j + n) % moch])
                            break
            elif fraza[i] == fraza[i].lower():
                for j in range(moch):
                    if moch == 32:
                        if fraza[i] == rus_lower_alphabet[j]:
                            arr_res.append(rus_lower_alphabet[(j + n) % moch])
                            break
                    if moch == 26:
                        if fraza[i] == eng_lower_alphabet[j]:
                            arr_res.append(eng_lower_alphabet[(j + n) % moch])
                            break
        else:
            arr_res.append(fraza[i])
    return arr_res


arr_s = [w for w in input().split()]

arr_out = []
for word in arr_s:
    arr_out.append(
        chru(chif, len(word.replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace('"', '')), lan,
             word))

for word in arr_out:
    for i in word:
        print(i, end='')
    print(' ', end='')
