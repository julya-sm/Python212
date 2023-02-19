
# 1. Объединить два текстовых файла

import os.path
import time

filenames = [r'd:\PythonProj\212_2\one.txt', r'd:\PythonProj\212_2\res_1.txt']

with open(r'd:\PythonProj\212_2\output_file.txt', 'w') as outfile:
    for filename in filenames:
        with open(filename) as infile:
            for line in infile:
                outfile.write(line)

with open('output_file.txt') as f:
    print(f.read())

# 2. Определить, существует ли файл. Если существует, вывести на экран его имя и время последнего доступа.
# Если не существует, вывести сообщение об этом.


def file_info(p, fn):

    file_dir = os.path.dirname(p)
    t = os.path.getmtime(p)
    friendly_t = time.strftime('%d.%m.%Y, %H:%M:%S', time.localtime(t))
    print(fn, f'({file_dir}) - время последнего доступа {friendly_t}')


path = input(r'Введите полное имя файла: ')
is_file_exist = os.path.exists(path)
file_name = os.path.basename(path)

if not is_file_exist:
    print('Файла', file_name, 'не существует')
    exit()
else:
    file_info(path, file_name)
