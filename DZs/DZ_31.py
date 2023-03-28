# Создать класс Triangle, свойства - длина трех сторон, метод - проверка существования треугольника
# В дескрипторе проверяется, чтобы длина сторон задавалась целым положительным числом


class PositiveInt:
    @staticmethod
    def is_int_and_positive(side):
        if not isinstance(side, int):
            raise TypeError(f'Сторона {side} должна быть целым числом')
        if side <= 0:
            raise ValueError(f'Сторона {side} должна быть положительным числом')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.is_int_and_positive(value)
        setattr(instance, self.name, value)


class Triangle:
    a = PositiveInt()
    b = PositiveInt()
    c = PositiveInt()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_exist(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            print(f'Треугольник со сторонами ({self.a}, {self.b}, {self.c}) существует')
        else:
            print(f'Треугольник со сторонами ({self.a}, {self.b}, {self.c}) не существует')


t1 = Triangle(2, 5, 6)
t2 = Triangle(5, 2, 8)
t3 = Triangle(7, 3, 6)
t1.is_exist()
t2.is_exist()
t3.is_exist()
