# -----------------------Домашнее задание 14.05.23-------------------------------------------

from jinja2 import FileSystemLoader, Environment

file_loader = FileSystemLoader('DZ_41')
env = Environment(loader=file_loader)
tm = env.get_template('main.html')
msg = tm.render(title='Домашнее задание', h1='Страница с домашним заданием', p1='Домашнее задание выполнено!!!')
print(msg)
