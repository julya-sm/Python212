# Словарь хранит название стран (ключи) и их столиц (значения).
# Нужно реализовать: добавление, удаление, поиск, редактирование и просмотр данных (используя их упаковку и распаковку).

import json


class CountryCapital:
    @staticmethod
    def load(file_name):
        try:
            data = json.load(open(file_name))
        except FileNotFoundError:
            data = {}
        finally:
            return data

    @staticmethod
    def add_data(file_name):
        new_country = input('Введите название страны: ')
        new_capital = input('Введите название столицы: ')

        data1 = CountryCapital.load(file_name)

        data1[new_country] = new_capital

        with open(file_name, 'w') as f:
            json.dump(data1, f)

    @staticmethod
    def delete_data(file_name):
        del_country = input('Введите название удаляемой страны: ')

        data1 = CountryCapital.load(file_name)

        if del_country in data1:
            del data1[del_country]
            with open(file_name, 'w') as f:
                json.dump(data1, f)
        else:
            print('Такой страны в словаре нет')

    @staticmethod
    def search_data(file_name):
        data1 = CountryCapital.load(file_name)
        desired_country = input('Введите название искомой страны: ')

        if desired_country in data1:
            print(f'Страна {desired_country} со столицей {data1[desired_country]} есть в словаре')
        else:
            print(f'Страна {desired_country} в словаре отсутствует')

    @staticmethod
    def edit_data(file_name):
        edit_country = input('Введите название страны для корректировки: ')
        data1 = CountryCapital.load(file_name)

        if edit_country in data1:
            new_capital = input('Введите новое название столицы: ')
            data1[edit_country] = new_capital

            with open(file_name, 'w') as f:
                json.dump(data1, f)
        else:
            print(f'Страна {edit_country} в словаре отсутствует')

    @staticmethod
    def view_data(file_name):
        with open(file_name) as f:
            print(json.load(f))


file = 'capital_lst.json'
while True:
    index = input('Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных'
                  '\n4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы\nВвод: ')

    if index == '1':
        CountryCapital.add_data(file)
    elif index == '2':
        CountryCapital.delete_data(file)
    elif index == '3':
        CountryCapital.search_data(file)
    elif index == '4':
        CountryCapital.edit_data(file)
    elif index == '5':
        CountryCapital.view_data(file)
    elif index == '6':
        break
    else:
        print('Вы ввели некорректный номер')
