from faker import Faker
from random import choice

from libr.database_libr import create_db, Session
from libr.author import Author


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    book_titles = [
        'Теория графов', 'Квасим капусту вкусно', 'Энциклопедия рыболова',
        'Синхрофазотрон и математика', 'Бабочки Амазонии', 'Крабы и раки', 'Загадки и отгадки']

    faker = Faker('ru_RU')
    session.commit()

    for _ in range(6):
        full_name = faker.name().split()
        author = Author(full_name, book_title=choice(book_titles))
        session.add(author)

    session.commit()
    session.close()
