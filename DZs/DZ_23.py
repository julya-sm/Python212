
# Создать класс Rectangle, описывающий прямоугольник. В классе должны быть все необходимые методы,
# а также методы вычисления площади, периметра и диагонали, и метод, рисующий прямоугольник.

import math


class Rectangle:

    def __init__(self, height, width):
        self.width = width
        self.height = height
        print('Высота прямоугольника:', self.height)
        print('Ширина прямоугольника:', self.width)

    def find_area(self):
        return self.width * self.height

    def find_perimeter(self):
        return self.width * 2 + self.height * 2

    def find_diagonal(self):
        d = math.sqrt(self.width ** 2 + self.height ** 2)
        return round(d, 1)

    def draw_rect(self):
        for i in range(self.height):
            print('*' * self.width)


rect1 = Rectangle(3, 9)
print('Площадь прямоугольника:', rect1.find_area())
print('Периметр прямоугольника:', rect1.find_perimeter())
print('Диагональ прямоугольника:', rect1.find_diagonal())
print()
rect1.draw_rect()
