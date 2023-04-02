# Создать файл со списком словаря словарей

import json
from random import choice


def gen_person():
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(nums)

    person = {
        'name': name,
        'tel': tel
    }

    return person


def write_json(person_dict):
    pers_key = ''
    keys = ['a', 'b', 'c', '1', '2', '3', '4', '5', '6', '7']

    while len(pers_key) != 10:
        pers_key += choice(keys)

    try:
        data = json.load(open('person2.json'))
    except FileNotFoundError:
        data = {}

    data[pers_key] = person_dict
    with open('person2.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())
