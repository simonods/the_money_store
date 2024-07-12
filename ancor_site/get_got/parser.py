from dataclasses import dataclass
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.binance.com/"
NEWS_URL = urljoin(BASE_URL, "en/square/news/market")


@dataclass
class Article:
    pub_time: str
    title: str
    content: str
    currency: list[float]


def parse_currency(currencies: BeautifulSoup):
    pass


def parse_single_article(article: BeautifulSoup):
    return Article(
        pub_time=article.select_one(".css-vyak18").text,
        title=article.select_one(".css-yxpvu").text,
        content=article.select_one(".css-10lrpzu").text,
        currency=parse_currency(article.select_one(".trading-pairs"))
    )


def parse_articles(soup: BeautifulSoup):
    articles = soup.select(".style_NewsItemRoot__3nhHX")

    return [parse_single_article(article) for article in articles]


def get_home_articles():
    page = requests.get(NEWS_URL).content
    soup = BeautifulSoup(page, "html.parser")

    all_articles = parse_articles(soup)
    for article in all_articles:
        print(article)
    print(len(all_articles))


def main():
    get_home_articles()


if __name__ == '__main__':
    main()
