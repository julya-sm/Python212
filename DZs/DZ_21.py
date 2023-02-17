
# 1. Найти в списке из 10 случайных чисел число, введенное пользователем. Применить алгоритм линейного поиска

from random import randint


def find_number(lst, n):
    pos = 0
    found = False
    while pos < len(lst) and not found:
        if lst[pos] == n:
            found = True
        else:
            pos += 1

    return found


random_list = [randint(10, 100) for i in range(10)]
print(random_list)
user_number = int(input('Введите двузначное положительное число: '))

if find_number(random_list, user_number):
    print(f'Число {user_number} в списке присутствует')
else:
    print('Число', user_number, 'в списке отсутствует')

# 2. Удалить строку из файла по ее индексу

f = open('dz.txt', 'w')
f.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;')
f.close()

f = open('dz.txt', 'r')
read_f = f.readlines()
print(read_f)
x = int(input('Введите номер строки: '))
for i in range(len(read_f)):
    if i == x:
        read_f[i] = ''
f.close()

f = open('dz.txt', 'w')
f.writelines(read_f)
f.close()

# Объединить четыре списка

lst1 = [5, 9, 6, 7]
lst2 = [3, 11, 8]
lst3 = [2, 4]
lst4 = [10, 1, 12]
total_lst = lst1 + lst2 + lst3 + lst4

print(total_lst)

# результат отсортировать по возрастанию или убыванию по выбору пользователя.


def quick_sort(a, pos):
    if len(a) > 1:
        x = a[(len(a) - 1) // 2]
        low = [i for i in a if i < x]
        eq = [i for i in a if i == x]
        hi = [i for i in a if i > x]
        if pos == 2:
            a = quick_sort(low, pos) + eq + quick_sort(hi, pos)
        elif pos == 1:
            a = quick_sort(hi, pos) + eq + quick_sort(low, pos)

    return a


up_or_down = int(input('Введите 1 для сортировки по убыванию, 2 - для сортировки по возрастанию: '))
print(quick_sort(total_lst, up_or_down))

# Найти значение, указанное пользователем, методом линейного поиска

your_num = int(input('Введите число: '))
if find_number(total_lst, your_num):
    print(f'Число {your_num} в списке присутствует')
else:
    print(f'Число {your_num} в списке отсутствует')
