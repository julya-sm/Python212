# Создать класс Student со свойством 'имя' и методом для вывода информации на экран.
# Вложенный класс содержит информацию о ноутбуке: модель, процессор, память


class Student:
    def __init__(self, name):
        self.name = name
        self.laptop = self.Laptop()

    def display(self):
        print(self.name, end=' ')
        self.laptop.display()

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i7'
            self.ram = 16

        def display(self):
            print(f'=> {self.brand}, {self.cpu}, {self.ram}')


s1 = Student("Roman")
s2 = Student("Vladimir")

s1.display()
s2.display()
