import json

with open('love_number.json') as f:
    n = json.load(f)
    print("Я знаю ваше любимое число! Это", n)
