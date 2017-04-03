"""Два кубика D8s: создайте модель, которая показывает, что происходит при 1000-крат-
ном бросании двух восьмигранных кубиков. Постепенно наращивайте количество бросков,
пока не начнете замечать ограничения, связанные с ресурсами вашей системы."""
import pygal
from die import Die

# Создание двух кубиков D8.
die_1 = Die(8)
die_2 = Die(8)

# Моделирование серии бросков с сохранением результатов в списке.
results = []
for roll_num in range(1000000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Анализ результатов.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов.
hist = pygal.Bar()
hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = [str(i) for i in range(2, 17)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
