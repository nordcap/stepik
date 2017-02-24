"""
Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.
Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа
имеет ценность 1. Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные
 прямо под нижележащими кубиками, имеют ценность 3. И т. д.

Ценность цвета равна сумме ценностей всех кубиков этого цвета.

Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
Sample Input:
<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>
Sample Output:
4 3 1
"""
from xml.etree.ElementTree import XMLParser


class SearchColor:  # The target object of the parser
    depth = 0  # эквивалентно ценности
    red = 0  # ценность красных кубиков
    green = 0  # ценность зеленых кубиков
    blue = 0  # ценность синих кубиков

    def start(self, tag, attrib):  # Called for each opening tag.
        self.depth += 1
        if attrib['color'] == "red":
            self.red += self.depth
        if attrib['color'] == "green":
            self.green += self.depth
        if attrib['color'] == "blue":
            self.blue += self.depth

    def end(self, tag):  # Called for each closing tag.
        self.depth -= 1

    def data(self, data):
        pass  # We do not need to do anything with data.

    def close(self):  # Called when all data has been parsed.
        return "{} {} {}".format(self.red, self.green, self.blue)


target = SearchColor()
parser = XMLParser(target=target)

exampleXML = input()

parser.feed(exampleXML)

print(parser.close())

