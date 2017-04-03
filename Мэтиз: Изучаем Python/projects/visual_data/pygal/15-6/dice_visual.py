"""15-6. Автоматические метки: измените программы die.py и dice_visual.py. Замените список,
используемый для задания значений hist.x_labels, циклом, автоматически генерирующим
этот список. Если вы хорошо освоили генераторы списков, также попробуйте заменить
другие циклы for в die_visual.py и dice_visual.py генераторами списков."""
import pygal
from die import Die

# Создание двух кубиков D6.
die_1 = Die()
die_2 = Die()

# Моделирование серии бросков с сохранением результатов в списке.
results = []
for roll_num in range(1000):
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
hist.x_labels = [str(i) for i in range(2, 13)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
