"""
15-1. Кубы: число, возведенное в третью степень, называется «кубом». Нанесите на диа-
грамму первые пять кубов.
"""

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
cube = [i**3 for i in input_values]
plt.plot(input_values, cube, linewidth=3)
# Назначение заголовка диаграммы и меток осей.
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)
# Назначение размера шрифта делений на осях.
plt.tick_params(axis='both', which='major', labelsize=14)
plt.scatter(input_values, cube, s=100, c='red')
plt.show()