"""
10-1. Изучение Python: откройте пустой файл в текстовом редакторе и напишите несколько
строк текста о возможностях Python. Каждая строка должна начинаться с фразы: «In Python
you can...» Сохраните файл под именем learning_python.txt в каталоге, использованном для
примеров этой главы. Напишите программу, которая читает файл и выводит текст три раза:
с чтением всего файла, с перебором строк объекта файла и с сохранением строк в списке
с последующим выводом списка вне блока with.
"""
print("чтение всего файла")
with open('learning_python.txt') as f:
    text = f.read().strip()
print(text)

print("перебор строк объекта файла")
with open('learning_python.txt') as f:
    for line in f:
        print(line.strip())

print("сохранение строк в списке")
with open('learning_python.txt') as f:
    lines = f.readlines()
for line in lines:
    print(line.strip())
