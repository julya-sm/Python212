# Провести парсинг данных нескольких веб-страниц любого ресурса с применением ООП
# Страниц со статьями 466, я взяла 2 первые, для примера

import requests
from bs4 import BeautifulSoup


class Parser:
    html = ''
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        articles = self.html.find_all('div', class_='load-list')[0]
        for article in articles:
            title = article.find('h2').text
            href = article.find('h2').find('a')['href']
            author_or_info = article.find('span').find('a').text.strip()

            self.res.append({
                'title': title,
                'href': href,
                'author_or_info': author_or_info
            })

    def save(self):
        with open(self.path, 'w', encoding='utf-8-sig') as f:
            i = 1
            for article in self.res:
                f.write(f"Статья № {i}\n\nНазвание: {article['title']}\nСсылка: {article['href']}"
                        f"\nАвтор/Компания/Рубрика: {article['author_or_info']}\n\n{'*' * 20}\n")
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()
