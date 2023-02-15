from typing import List
import requests
from bs4 import BeautifulSoup
from models.news import News


class ParachainsInfoScrapper():

    news: List[News] = []

    def __init__(self):
        response = requests.get("https://parachains.info/news")
        self.soup = BeautifulSoup(response.content, 'html5lib')

    def build_news_list(self):
        news_cards = self.soup.find_all('div', class_='news_card')

        for card in news_cards:
            media_body = card.find(class_='media-body')

            self.news.append(News(
                self.get_parachain_name(card),
                self.get_parachain_logo(card),
                self.get_date(media_body),
                self.get_title(media_body),
                self.get_type(media_body),
                self.get_url(media_body)
            ))

    def get_parachain_name(self, card) -> str:
        parachain_name_container = card.find(class_='news_parachain_name')

        if (parachain_name_container.find('a')):
            parachain_name = parachain_name_container.find(
                'a').text.strip()
        else:
            parachain_name = parachain_name_container.find(
                class_='parachain_small_font').text.strip()

        return parachain_name

    def get_parachain_logo(self, card) -> str:
        parachain_name_container = card.find(class_='news_parachain_name')

        parachain_logo_element = parachain_name_container.find(
            class_='project_image_logo')

        parachain_logo = parachain_logo_element.get('src').strip()

        if "data" in parachain_logo:
            parachain_logo = parachain_logo_element.get('data-srcset').strip()

        return parachain_logo

    def get_title(self, media_body) -> str:
        return media_body.find('a').text.strip()

    def get_type(self, media_body) -> str:
        return media_body.find(class_='badge').text.strip()

    def get_date(self, media_body) -> str:
        return media_body.find(class_='datetime').text.strip()

    def get_url(self, media_body) -> str:
        return media_body.find('a').get('href').strip()


if __name__ == "__main__":
    parachainsNews = ParachainsInfoScrapper()
    parachainsNews.build_news_list()
    for news in parachainsNews.news:
        news.to_string()
