import sqlite3
import time
import math
import re
from flask import url_for

class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM mainmenu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения из базы данных")
        return []

    def article(self, name, price, url, art):
        try:
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO article VALUES(NULL, ?, ?, ?, ?, ?)", (name, art, price, url, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления товара в БД " + str(e))
            return False
        return True

    def get_article(self, alias):
        try:
            self.__cur.execute(f"SELECT name, art FROM article WHERE url LIKE '{alias}' LIMIT 1")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД " + str(e))

        return False, False

    def get_article_description(self):
        try:
            self.__cur.execute(f"SELECT id, name, art, price, url FROM article ORDER BY time DESC")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения товаров из БД " + str(e))

        return []
