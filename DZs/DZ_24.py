# Создать класс Sphere
# - метод get_volume возвращает объем шара, ограниченного данной сферой
# - get_area - возвращает площадь верхней поверхности сферы
# - sp1.r возвращает радиус сферы - действительное число (в этом случае применила @property)

import math


class Sphere:
    def __init__(self, r, cx = 0, cy = 0, cz = 0):
        self.__cx = cx
        self.__cy = cy
        self.__cz = cz
        self.__r = r

    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self, new_r):
        if isinstance(new_r, (int, float)) and new_r > 0:
            self.__r = new_r
        else:
            print('Радиус должен быть положительным числом')

    def set_center(self, cx, cy, cz):
        if isinstance(cx, (int, float)) and isinstance(cy, (int, float)) and isinstance(cx, (int, float)):
            self.__cx = cx
            self.__cy = cy
            self.__cz = cz
        else:
            print('Координаты должны быть числами')

    def get_center(self):
        return self.__cx, self.__cy, self.__cz

    def get_volume(self):
        return (4 / 3) * math.pi * self.__r ** 3

    def get_area(self):
        return 4 * math.pi * self.__r ** 2

    def is_point_inside(self, x, y, z):
        ab = math.sqrt((self.__cx - x) ** 2 + (self.__cy - y) ** 2 + (self.__cz - z) ** 2)
        return ab <= self.__r


sp1 = Sphere(0.6, 0, 0, 0)  # можно только радиус указать
print('radius:', sp1.r)
print('get_volume:', sp1.get_volume())
print('get_area:', sp1.get_area())
print('get_center:', sp1.get_center())
print('is_point_inside(0, -1.5, 0):', sp1.is_point_inside(0, -1.5, 0))
sp1.set_center(0, 0, 1)
print('get_center2:', sp1.get_center())
print()
sp1.r = 1.6
print('radius:', sp1.r)
print(sp1.__dict__)
print('is_point_inside(0, -1.5, 0):', sp1.is_point_inside(0, -1.5, 0))
