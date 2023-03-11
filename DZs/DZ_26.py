# Создать класс Pair со свойствами - числа A и B, и методами: изменение чисел, и вычисления их произведения и суммы
# Определить производный класс "Rigth Triangle" со свойствами: катеты А и B, и методами: вычисление гипотенузы
# и площади треугольника, вывод информации о фигуре на экран

from math import sqrt


class Pair:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

    def summa(self):
        return self.__a + self.__b

    def mult(self):
        return self.__a * self.__b


class RightTriangle(Pair):
    def __init__(self, a, b):
        super().__init__(a, b)

    def hypotenuse(self):
        c = round(sqrt(self.a ** 2 + self.b ** 2), 2)
        return c

    def area(self):
        return round(super().mult() / 2, 1)

    def info(self):
        print(f"Прямоугольный треугольник ABC ({self.a}, {self.b}, {self.hypotenuse()})")


triangle = RightTriangle(5, 8)
print(f'Гипотенуза треугольника ABC: {triangle.hypotenuse()}')
triangle.info()
print(f'Площадь треугольника ABC: {triangle.area()}')
print()
print(f"Сумма: {triangle.summa()}")
print(f"Произведение: {triangle.mult()}")
print()
triangle.a = 10
triangle.b = 20
print(f'Гипотенуза треугольника ABC: {triangle.hypotenuse()}')
triangle.info()
print(f'Площадь треугольника ABC: {triangle.area()}')
print()
print(f"Сумма: {triangle.summa()}")
print(f"Произведение: {triangle.mult()}")