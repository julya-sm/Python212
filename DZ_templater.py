from jinja2 import Template

pages = [
    {'tab': "/index", 'text': 'Главная'},
    {'tab': "/news", 'text': 'Новости'},
    {'tab': "/about", 'text': 'О компании'},
    {'tab': "/shop", 'text': 'Магазин'},
    {'tab': "/contacts", 'text': 'Контакты'},
]


link = """
<ul>
{% for p in pages -%}
{% if p.text == "Главная"-%}
    <li><a href="{{ p['tab'] }}" class="active">{{ p['text'] }}</a></li>
{% else -%}
    <li><a href="{{ p['tab'] }}">{{ p['text'] }}</a></li>
{% endif -%}
{% endfor -%}
</ul>
"""

tm = Template(link)
msg = tm.render(pages=pages)

print(msg)
