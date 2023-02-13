
# 1. Найти в списке из 10 случайных чисел число, введенное пользователем. Применить алгоритм бинарного поиска

from random import randint


def find_number(lst, n):
    first = 0
    last = len(lst) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if lst[midpoint] == n:
            found = True
        else:
            if n < lst[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    if found:
        print('Число', n, 'в списке присутствует')
    else:
        print('Число', n, 'в списке отсутствует')


ten_digits = sorted([randint(10, 100) for i in range(10)])
user_number = int(input('Введите двузначное положительное число: '))
find_number(ten_digits, user_number)
