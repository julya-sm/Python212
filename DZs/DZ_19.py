
# 1. Валидация номера телефона: +7 499 456-45-78, 74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78

import re


def valid_number(num):
    r1 = r'^\+?7\s?\(?\d{3}\)?\s?\d{3}[-\s]?\d{2}[-\s]?\d{2}$'
    valid_num = re.findall(r1, num)
    if valid_num:
        print("Номер правильный")
    else:
        print("Номер неправильный")


n = "7 (499) 456-45-78"

valid_number(n)

# 2. Подсчитать количество отрицательных чисел в списке с применением рекурсии


def count_negatives(lst):
    if len(lst) == 0:  # или lst == []
        return 0
    else:
        count = count_negatives(lst[1:])
        if lst[0] < 0:
            count += 1
    return count


print(count_negatives([-2, 3, 8, -11, -4, 6]))
