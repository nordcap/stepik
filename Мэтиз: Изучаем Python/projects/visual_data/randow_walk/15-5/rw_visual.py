"""15-5. Рефакторинг: метод fill_walk() получился слишком длинным. Создайте новый метод
с именем get_step(), который определяет расстояние и направление для каждого шага, по-
сле чего вычисляет этот шаг. В результате метод fill_walk() должен содержать два вызова
get_step():
x_step = get_step()
y_step = get_step()
Рефакторинг сокращает размер fill_walk(), а метод становится более простым и понятным."""
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Новые блуждания строятся до тех пор, пока программа остается активной.
while True:
    # Построение случайного блуждания и нанесение точек на диаграмму.
    rw = RandomWalk()
    rw.fill_walk()
    # Назначение размера области просмотра.
    plt.figure(figsize=(10, 6))


    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=10)
    # Выделение первой и последней точек.
    plt.scatter(0, 0, c='green', edgecolors='none', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)
    # Удаление осей.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
