import os

from libr.database_libr import DATABASE_NAME
import create_db_lib as db_creator


if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()
