# import geometry.rect
# import geometry.sq
# import geometry.trian
# from geometry import *  # для этого способа нужно имена модулей записать в __init__.py

from geometry import rect, sq, trian


r1 = rect.Rectangle(1, 2)
r2 = rect.Rectangle(3, 4)

s1 = sq.Square(10)
s2 = sq.Square(20)

t1 = trian.Triangle(2, 3, 4)
t2 = trian.Triangle(6, 6, 11)

shape = [r1, r2, s1, s2, t1, t2]

for g in shape:
    print(g.get_perimeter())
