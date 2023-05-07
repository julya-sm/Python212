import os

from sqlalchemy import and_, or_, not_, desc, func, distinct, text
from libr.database_libr import DATABASE_NAME, Session
import create_db_lib as db_creator

from libr.author import Author


if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()

# # 1:
#
#     for it in session.query(Author):
#         print(it)
#     print('*' * 50)
#
# # 2:
#
#     print(session.query(Author).count())
#     print('*' * 50)
#
# # 3:
#
#     print(session.query(Author).first())
#     print('*' * 50)

# 4:

    # session.query(Author).filter(
    #     Author.id.like(3)
    # ).update({'book_title': 'Энциклопедия рыболова'})
    # session.commit()

    # session.query(Author).filter(
    #     Author.id.like(5)
    # ).update({'book_title': 'Квасим капусту вкусно'})
    # session.commit()

# # 5:
#
#     print(session.query(Author).filter(Author.book_title.in_(
#         ['Энциклопедия рыболова', 'Бабочки Амазонии'])).all())
#     print('*' * 50)
#
# # 6:
#     for it in session.query(Author).order_by(Author.surname):
#         print(it)
#     print('*' * 50)

# 7:

    # for it in session.query(Author).order_by(Author.book_title):
    #     print(it)
    # print('*' * 50)

# 8:

    # session.add(Author(full_name='Пупкин Василий Селиверстович'.split(), book_title='Загадки и отгадки'))
    # session.commit()

# 9:

    # for it in session.query(Author).limit(4):
    #     print(it)
    # print('*' * 50)

# 10:

    # i = session.query(Author).filter(Author.id == 7).one()
    # session.delete(i)
    # session.commit()

