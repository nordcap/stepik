'''
Дополните приведенный код, используя генератор, чтобы получить словарь result, состоящий из всех элементов словаря colors, кроме тех, у которых значением является None.

Примечание. Выводить содержимое словаря result не нужно.
'''

colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange',
          'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber',
          'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None,
          'c22': 'Sand', 'c23': None}

result = {k: colors[k] for k in colors if colors[k] != None}
