from bs4 import BeautifulSoup
import requests
from data.Article import Article
from utils import MongodbService


class StopGameParser:

    lastTitle = ''

    def __init__(self):
        storage = MongodbService
        lastTitle = storage.getLastArticleParser


    def parce(self):
        url = 'https://stopgame.ru/news'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.findAll('div', class_='item article-summary')
        articles = []

        for item in items:
            title = item.find('div', class_='caption caption-bold').get_text(strip=True)
            if title == self.lastTitle:
                break
            image = item.find('img').get('src')
            aricle_src = ("https://stopgame.ru" + f"{item.find('a').get('href')}")

            articles.append(Article(title, image, aricle_src))

        return articles
