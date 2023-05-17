from flask import Flask, render_template, url_for

app = Flask(__name__)

menu = [
    {'name': 'Главная', 'url': 'index'},
    {'name': 'О нас', 'url': 'about'},
    {'name': 'Обратная связь', 'url': 'contact'}
]


@app.route("/index")  # можно несколько декораторов указывать
@app.route("/")
def index():
    return render_template('index.html', title='Главная', menu=menu)


@app.route("/about")
def about():
    return render_template('about.html', title='О нас', menu=menu)


@app.route('/profile/<path:username>')
def profile(username):
    return f'Пользователь: {username}'


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Обратная связь', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
