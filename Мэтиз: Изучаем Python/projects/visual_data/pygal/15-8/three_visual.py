"""15-8. Три кубика: при броске 3 кубиков D6 наименьший возможный результат равен 3,
а наибольший — 18. Создайте визуализацию, которая показывает, что происходит при бро-
ске трех кубиков D6."""
import pygal
from die import Die

# Создание двух кубиков D8.
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Моделирование серии бросков с сохранением результатов в списке.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Анализ результатов.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов.
hist = pygal.Bar()
hist.title = "Results of rolling three D6 dice 1000 times."
hist.x_labels = [str(i) for i in range(3, 19)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('three_visual.svg')
