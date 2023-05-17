from flask import Flask, render_template, url_for

app = Flask(__name__)

menu = [
    {'name': 'Главная', 'url': 'index'},
    {'name': 'История', 'url': 'history'},
    {'name': 'Тенденции', 'url': 'fashion'}
]


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html', title='Главная', menu=menu)


@app.route("/history")
def about():
    return render_template('history.html', title='История', menu=menu)


@app.route('/fashion')
def contact():
    return render_template('fashion.html', title='Тенденции', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)