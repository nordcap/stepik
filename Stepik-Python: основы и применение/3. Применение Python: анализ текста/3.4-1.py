"""
Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

Sample Input 1:
https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample2.html
Sample Output 1:
Yes
Sample Input 2:
https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample1.html
Sample Output 2:
No
Sample Input 3:
https://stepic.org/media/attachments/lesson/24472/sample1.html
https://stepic.org/media/attachments/lesson/24472/sample2.html
Sample Output 3:
Yes
"""

"""
links = ["https://stepic.org/media/attachments/lesson/24472/sample0.html",
         "https://stepic.org/media/attachments/lesson/24472/sample2.html"]

links = ["https://stepic.org/media/attachments/lesson/24472/sample0.html",
         "https://stepic.org/media/attachments/lesson/24472/sample1.html"]

links = ["https://stepic.org/media/attachments/lesson/24472/sample1.html",
         "https://stepic.org/media/attachments/lesson/24472/sample2.html"]
"""
import requests, re, sys

links = []

for line in sys.stdin:
    line = line.rstrip()
    links.append(line)

two_link = "No"

request = requests.get(links[0])  # A

all_link_A = re.findall(r"href=\"(?P<link>\S+)\"", request.text)
for i in all_link_A:
    request = requests.get(i)  # C
    all_link_C = re.findall(r"href=\"(?P<link>\S+)\"", request.text)
    for j in all_link_C:
        if j == links[1]:
            two_link = "Yes"

print(two_link)
