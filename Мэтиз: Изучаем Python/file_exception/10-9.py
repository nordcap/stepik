"""
10-9. Ошибки без уведомления: измените блок except из упражнения 10-8 так, чтобы при
отсутствии файла программа продолжала работу, не уведомляя пользователя о проблеме.
"""
try:
    with open('cats.txt') as cat_f:
        for line in cat_f:
            print(line.strip())
except FileNotFoundError:
    pass
try:
    with open('dogs.txt') as dog_f:
        for line in dog_f:
            print(line.strip())
except FileNotFoundError:
    pass
