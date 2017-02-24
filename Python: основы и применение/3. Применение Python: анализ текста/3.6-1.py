"""
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический
факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true

Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true

Пример входного файла:
31
999
1024
502

﻿Пример выходного файла:
Interesting
Boring
Interesting
Boring
"""
import requests, re

api_url = "http://numbersapi.com/31/math?json=true"

params = {
    "json": "true"
}
url = "http://numbersapi.com"

with open("dataset_24476_3.txt", "r") as f:
    for line in f:
        api_url = url + '/' + str(line.strip()) + '/math'
        res = requests.get(api_url, params=params["json"])
        facts = re.findall(r"(\buninteresting\b|\bunremarkable\b|\bboring\b|we're missing a fact)", res.text)
        if len(facts) > 0:
            print("Boring")
        else:
            print("Interesting")
