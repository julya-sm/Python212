class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_perimeter(self):
        return 2 * (self.w + self.h)


# print(__name__)  # __main__ - возвращается при запуске самого rect.py

# geometry.rect - при запуске rect.py как модуля из start.py

__author__ = 'Julia'
if __name__ == '__main__':
    print(f'Modul {__name__} ({__author__})')
