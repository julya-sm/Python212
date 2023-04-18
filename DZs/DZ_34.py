# Провести парсинг данных из интернет-ресурса, результат сохранить в файле .csv

import requests
from bs4 import BeautifulSoup
import re
import csv


def refined(s):
    return re.sub(r'\D+', '', s)


def write_csv(data):
    with open('books.csv', 'a') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\r')

        writer.writerow((data['name'], data['url'], data['price']))


def get_html(url):
    res = requests.get(url)
    return res.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    p1 = soup.find_all('div', id='items_block')
    p1 = soup.find_all('div', class_='items')
    for pp in p1:
        books = pp.find_all('div', class_='item_block new')
        for book in books:
            name = book.find('u').text
            url = book.find('a', class_='block_name diblock')['href']
            price = book.find('span', class_='fs30').text
            pr = refined(price)
            data = {'name': name, 'url': url, 'price': pr}
            write_csv(data)


def main():
    url = 'https://rukodelie-online.ru/catalog/literatura/knigi'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
