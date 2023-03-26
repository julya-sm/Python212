# Создать родительский класс Shape и дочерние классы Square, Rectangle и Triangle
# В родительском классе должны быть абстрактные методы:
# нахождения площади, периметра, рисования фигуры и вывода информации
# Вывод информации - с использованием полиморфизма

from abc import ABC, abstractmethod

from math import sqrt


class Shape(ABC):
    def __init__(self, color, a, b=None, c=None):
        self.color = color
        if c is None:
            if b is None:
                self.a = self.b = a
            else:
                self.a = a
                self.b = b
        else:
            self.a = a
            self.b = b
            self.c = c

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def info(self):
        print(f"Цвет: {self.color}\nПериметр: {self.perimeter()}\nПлощадь: {self.area()}")

    @abstractmethod
    def draw(self):
        pass


class Square(Shape):
    def perimeter(self):
        return 4 * self.a

    def area(self):
        return self.a ** 2

    def info(self):
        print("===Квадрат===")
        print(f"Сторона: {self.a}")
        super().info()

    def draw(self):
        for i in range(self.a):
            for j in range(self.a):
                print('*', end="")
            print()


class Rectangle(Shape):
    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

    def draw(self):
        for i in range(self.a):
            for j in range(self.b):
                print('*', end="")
            print()

    def info(self):
        print("===Прямоугольник===")
        print(f"Длина: {self.a}\nШирина: {self.b}")
        super().info()


class Triangle(Shape):

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return round(sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)), 2)

    def draw(self):
        rows = []
        for n in range(self.b):
            rows.append(" " * n + "*" * (self.a - 2 * n))
        print("\n".join(reversed(rows)))

    def info(self):
        print("===Треугольник===")
        print(f"Сторона 1: {self.a}\nСторона 2: {self.b}\nСторона 3: {self.c}")
        super().info()


shapes = [
    Square('red', 3),
    Rectangle('green', 3, 7),
    Triangle('yellow', 11, 6, 6)
]

for shape in shapes:
    shape.info()
    shape.draw()
    print()
