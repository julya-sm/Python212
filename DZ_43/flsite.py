from flask import Flask, render_template, url_for, request, flash, session, redirect, g, abort
import os
import sqlite3
from FDataBase import FDataBase

DATABASE ='/tmp/flsk.db'
DEBUG = True
SECRET_KEY = 'afaa7a3db46af43000675767a7e63daf366cc255'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db')))

def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con

def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    if not hasattr(g, 'link.db'):
        g.link_db = connect_db()
    return g.link_db

@app.route("/")
def index():
    db = get_db() # Открытие базы данных
    dbase = FDataBase(db)
    return render_template('index.html', title='Главная', menu=dbase.get_menu(), articles=dbase.get_article_description())

@app.route("/article", methods=['POST', 'GET'])
def article():
    db = get_db() # Открытие базы данных
    dbase = FDataBase(db)
    if request.method == "POST":
        # if len(request.form['name']) > 4 and len(request.form['art']) > 10:
        res = dbase.article(request.form['name'], request.form['price'], request.form['url'], request.form['art'])
        print(res)
        if not res:
            flash('Ошибка добавления товара ', category='error')
        else:
            flash('Товар добавлен успешно', category='success')
    return render_template('article.html', title='Добавление товара', menu=dbase.get_menu())

@app.route('/article/<alias>')
def show_article(alias):
    db = get_db()  # Открытие базы данных
    dbase = FDataBase(db)
    # id_post = get_id_post()
    name, art = dbase.get_article(alias)
    if not name:
        print('Ничего не получилось')
        abort(404)
    return render_template('show_article.html', title=name, art=art, menu=dbase.get_menu())


if __name__ == '__main__':
    app.run(debug=True)