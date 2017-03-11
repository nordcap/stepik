"""
Моя пицца, твоя пицца: начните с  программы из упражнения 4-1. Создайте копию
списка с видами пиццы, присвойте ему имя friend_pizzas. Затем сделайте следующее.
•	 Добавьте новую пиццу в исходный список.
•	 Добавьте другую пиццу в список friend_pizzas.
•	 Докажите, что в программе существуют два разных списка. Выведите сообщение «My
favorite pizzas are:», а  затем первый список в  цикле for. Выведите сообщение «My
friend’s favorite pizzas are:», а затем второй список в цикле for. Убедитесь в том, что
каждая новая пицца находится в соответствующем списке.
"""
pizza = ["Margherita", "Marinara", "Veronese"]
friend_pizzas = pizza[:]
friend_pizzas.append("Pepperoni")
print("My favorite pizzas are:")
for i in pizza:
    print(i)
print("My friend’s favorite pizzas are:")
for i in friend_pizzas:
    print(i)
