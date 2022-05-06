with open('text.txt', encoding='utf-8') as file:
    s = file.readline().strip()
    print(s[::-1])
