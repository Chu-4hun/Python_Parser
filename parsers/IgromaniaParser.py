from bs4 import BeautifulSoup
import requests
from data.Article import Article


class IgromaniaParser:

    lastTitle = ''

    def parce(self):
        url = "https://www.igromania.ru/news/game/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.findAll('div', class_='aubl_item')
        articles = []

        for item in items:
            title = item.find('a', class_='aubli_name').get_text(strip=True)
            if title == self.lastTitle:
                break
            image = item.find('a', class_='aubli_img').find('img').get('src')
            aricle_src = ("https://www.igromania.ru/news/game" + f"{item.find('a', class_='aubli_img').get('href')}")

            articles.append(Article(title, image, aricle_src))

        self.lastTitle = articles[0]

        return articles
