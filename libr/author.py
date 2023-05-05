from sqlalchemy import Column, Integer, String

from libr.database_libr import Base


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    surname = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    patronymic = Column(String(100), nullable=False)
    book_title = Column(String(250), nullable=False)

    def __init__(self, full_name, book_title):
        self.surname = full_name[0]
        self.name = full_name[1]
        self.patronymic = full_name[2]
        self.book_title = book_title

    def __repr__(self):
        return f'Автор (ФИО): {self.surname} {self.name} {self.patronymic} Название книги: {self.book_title}'
