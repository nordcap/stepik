'''
Is Valid Triangle?
Напишите функцию is_valid_triangle(side1, side2, side3), которая принимает в качестве аргументов три натуральных числа, и возвращает значение True если существует невырожденный треугольник со сторонами side1, side2, side3 и False в противном случае.
'''


# объявление функции
def is_valid_triangle(side1, side2, side3):
    m = max(side1, side2, side3)
    if (side1 == m and side1 < side2 + side3) or (side2 == m and side2 < side1 + side3) or (
            side3 == m and side3 < side1 + side2):
        return True
    else:
        return False


print(is_valid_triangle(2, 2, 2))
print(is_valid_triangle(2, 3, 10))
print(is_valid_triangle(3, 4, 5))
