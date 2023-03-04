# 2 варианта: 1 - с декоратором @property, 2 - с get_...() / set_...()
# Вариант I

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, surname, num, percent, value=0):
#         self.__surname = surname
#         self.__num = num
#         self.__percent = percent
#         self.__value = value
#         print(f'Счет №{self.__num}, принадлежащий {self.__surname}, был открыт.')
#         print("*" * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет №{self.__num}, принадлежащий {self.__surname}, был закрыт.')
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, sn):
#         self.__surname = sn
#
#     @property
#     def num(self):
#         return self.__num
#
#     @num.setter
#     def num(self, n):
#         self.__num = n
#
#     @property
#     def percent(self):
#         return self.__percent
#
#     @percent.setter
#     def percent(self, pct):
#         self.__percent = pct
#
#     @property
#     def value(self):
#         return self.__value
#
#     @value.setter
#     def value(self, v):
#         self.__value = v
#
#     @classmethod
#     def set_usd_rate(cls, new_rate):
#         cls.rate_usd = new_rate
#
#     @classmethod
#     def set_eur_rate(cls, new_rate):
#         cls.rate_eur = new_rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def print_balance(self):
#         print(f'Текущий баланс: {self.__value} {Account.suffix}')
#
#     def print_info(self):
#         print('Информация о счете:')
#         print('-' * 20)
#         print(f'№{self.__num}')
#         print(f'Владелец: {self.__surname}')
#         self.print_balance()  # методы экземпляра вызываются с помощью self
#         print(f'Проценты: {self.__percent:.0%}')
#         print('-' * 20)
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}')
#
#     def edit_owner(self, surname):
#         self.__surname = surname
#
#     def add_percents(self):
#         self.__value += self.__value * self.__percent
#         print('Проценты были успешно начислены!')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f'К сожалению, у вас нет {val} {Account.suffix}')
#         else:
#             self.__value -= val
#             print(f'{val} {Account.suffix} было успешно снято')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#
# acc = Account(num='12345', surname='Долгих', percent=0.03, value=1000)
# acc.print_info()
# acc.surname = "Дюма"
# acc.num = "44444"
# acc.percent = 0.05
# acc.value = 5000
# acc.print_info()

# Вариант II

class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'

    def __init__(self, surname, num, percent, value=0):
        self.__surname = surname
        self.__num = num
        self.__percent = percent
        self.__value = value
        print(f'Счет №{self.__num}, принадлежащий {self.__surname}, был открыт.')
        print("*" * 50)

    def __del__(self):
        print('*' * 50)
        print(f'Счет №{self.__num}, принадлежащий {self.__surname}, был закрыт.')

    def get_surname(self):
        return self.__surname

    def set_surname(self, sn):
        self.__surname = sn

    def get_num(self):
        return self.__num

    def set_num(self, n):
        self.__num = n

    def get_percent(self):
        return self.__percent

    def set_percent(self, pct):
        self.__percent = pct

    def get_value(self):
        return self.__value

    def set_value(self, v):
        self.__value = v

    @classmethod
    def set_usd_rate(cls, new_rate):
        cls.rate_usd = new_rate

    @classmethod
    def set_eur_rate(cls, new_rate):
        cls.rate_eur = new_rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def print_balance(self):
        print(f'Текущий баланс: {self.__value} {Account.suffix}')

    def print_info(self):
        print('Информация о счете:')
        print('-' * 20)
        print(f'№{self.__num}')
        print(f'Владелец: {self.__surname}')
        self.print_balance()  # методы экземпляра вызываются с помощью self
        print(f'Проценты: {self.__percent:.0%}')
        print('-' * 20)

    def convert_to_usd(self):
        usd_val = Account.convert(self.__value, Account.rate_usd)
        print(f'Состояние счета: {usd_val} {Account.suffix_usd}')

    def convert_to_eur(self):
        eur_val = Account.convert(self.__value, Account.rate_eur)
        print(f'Состояние счета: {eur_val} {Account.suffix_eur}')

    def edit_owner(self, surname):
        self.__surname = surname

    def add_percents(self):
        self.__value += self.__value * self.__percent
        print('Проценты были успешно начислены!')
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.__value:
            print(f'К сожалению, у вас нет {val} {Account.suffix}')
        else:
            self.__value -= val
            print(f'{val} {Account.suffix} было успешно снято')
        self.print_balance()

    def add_money(self, val):
        self.__value += val
        print(f'{val} {Account.suffix} было успешно добавлено!')
        self.print_balance()


acc = Account(num='12345', surname='Долгих', percent=0.03, value=1000)
acc.print_info()
acc.set_surname("Дюма")
acc.set_num("44444")
acc.set_percent(0.05)
acc.set_value(5000)
acc.print_info()
