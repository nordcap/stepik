"""
10-2. метод replace() может использоваться для замены любого слова в строке
другим словом. В следующем примере слово ‘dog’ заменяется словом ‘cat’:
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'
Прочитайте каждую строку из только что созданного файла learning_python.txt и замените
слово строка на другое слово
"""
with open('learning_python.txt') as f:
    for line in f:
        newline = line.replace('строка', 'замена')
        print(newline.strip())
