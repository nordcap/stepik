"""
A durak deck contains 36 cards. Each card has a suit of either clubs, diamonds, hearts, or spades (denoted C, D, H, S). Each card also has a value of either 6 through 10, jack, queen, king, or ace (denoted 6, 7, 8, 9, 10, J, Q, K, A). For scoring purposes card values are ordered as above, with 6 having the lowest and ace the highest value.

Напишите программу, которая определяет, бьёт ли одна карта другую.
Если встречаются две карты одной масти, то побеждает та, у которой выше значение;
Если карты разных мастей, то карта, имеющая козырную масть, побеждает;
Если карты разных мастей и нет козырных, то никто не побеждает.

Формат ввода:
На первой строке через пробел указываются две карты в формате <значение><масть>, а на следующей строке указывается козырная масть.

Формат вывода:
Программа должна вывести слово
First, если первая карта бьёт вторую,
Second, если вторая карта бьёт первую,
Error, если ни одна из карт не может побить другую.

Sample Input 1:
AH JH
D
Sample Output 1:
First
Sample Input 2:
AH JS
S
Sample Output 2:
Second
Sample Input 3:
7C 10H
S
Sample Output 3:
Error
"""
val_cards = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
card1, card2 = input().split()
mast = input()

card1_v = card1[0:-1]  # значение первой карты
card1_m = card1[-1]  # масть первой карты
card2_v = card2[0:-1]  # значение второй карты
card2_m = card2[-1]  # масть второй карты

if card1_m == card2_m:
    ind1 = val_cards.index(card1_v)
    ind2 = val_cards.index(card2_v)
    if ind1 > ind2:
        print("First")
    elif ind1 < ind2:
        print("Second")
    else:
        print("Error")
elif card1_m != card2_m:
    if card1_m == mast:
        print("First")
    elif card2_m == mast:
        print("Second")
    else:
        print("Error")
