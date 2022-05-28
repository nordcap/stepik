"""
В этой задаче вам необходимо воспользоваться API сайта artsy.net
API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.
В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).
Вам даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получите информацию о имени художника и годе рождения.
Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения,
выведите их имена в лексикографическом порядке.
"""
import requests, json

client_id = "your_client_id"
client_secret = "your_client_secret"

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token": token}
image_man = {}
with open("dataset_24476_4.txt", "r") as f:
    for line in f:
        # инициируем запрос с заголовком
        r = requests.get("https://api.artsy.net/api/artists/" + str(line.strip()), headers=headers)
        r.encoding = 'utf-8'
        # разбираем ответ сервера
        res = json.loads(r.text)
        image_man[res['sortable_name']] = res['birthday']

image_man_sort = sorted(image_man.items(), key=lambda v: v[1], reverse=False)
for m in image_man_sort:
    print(m[0])


