"""
15-2. Цветные кубы: примените цветовую карту к диаграмме с кубами.
"""

import matplotlib.pyplot as plt

input_values = list(range(1, 5001))
cube = [i ** 3 for i in input_values]
# Назначение заголовка диаграммы и меток осей.
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)
# Назначение размера шрифта делений на осях.
plt.tick_params(axis='both', which='major', labelsize=14)
plt.scatter(input_values, cube, c=cube, cmap=plt.cm.Blues, edgecolor='none', s=40)
plt.show()
