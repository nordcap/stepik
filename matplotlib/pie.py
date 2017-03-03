import matplotlib.pyplot as plt

slices = [7, 2, 2, 13]

activities = ['sleeping', 'eating', 'working', 'playing']
colors = ['m', 'c', 'r', 'y']
# Создать новое окно (фигуру) с одинаковыми размерами сторон (6 x 6 дюйма)
#plt.figure(figsize=(7, 7))

# Установим размеры осей по горизонтали и вертикали тоже одинаковыми
#plt.axes([0.0, 0.0, 1.0, 1.0])

plt.pie(slices, labels=activities, colors=colors, startangle=90, shadow=True, explode=(0, 0.1, 0, 0), autopct='%1.1f%%')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('scatter')
# plt.legend()

plt.show()
