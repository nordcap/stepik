"""
8-16. Импортирование: возьмите за основу одну из написанных вами программ с  одной
функцией. Сохраните эту функцию в  отдельном файле. Импортируйте функцию в  файл
основной программы и вызовите функцию каждым из следующих способов:
import имя_модуля
from имя_модуля import имя_функции
from имя_модуля import имя_функции as псевдоним
import имя_модуля as псевдоним
from имя_модуля import *
"""
#import buildcar
#from buildcar import build_car
#from buildcar import build_car as bc
#from buildcar import *
import buildcar as bc

car_profile = bc.build_car('УАЗ', 'УАЗ', color='зеленый', top_package=False)
print(car_profile)
