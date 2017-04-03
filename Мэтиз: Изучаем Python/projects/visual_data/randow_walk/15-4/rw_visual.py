"""15-4. Измененные случайные блуждания: в  классе RandomWalk значения x_step и  y_step
генерируются по единому набору условий. Направление выбирается случайно из списка
[1, -1], а расстояние — из списка [0, 1, 2, 3, 4]. Измените значения в этих списках и посмо-
трите, что произойдет с общей формой диаграммы. Попробуйте применить расширенный
список вариантов расстояния (например, от 0 до 8) или удалите –1 из списка направлений
по оси x или y ."""
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Новые блуждания строятся до тех пор, пока программа остается активной.
while True:
    # Построение случайного блуждания и нанесение точек на диаграмму.
    rw = RandomWalk(50000)
    rw.fill_walk()
    # Назначение размера области просмотра.
    plt.figure(figsize=(10, 6))


    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
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
