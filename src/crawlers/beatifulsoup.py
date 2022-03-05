from src.crawlers import Crawler

from bs4 import BeautifulSoup
import urllib.request
import json

class BeatifulSoupCrawler(Crawler):
    def run(self):
        pass

    def get_links(self, url):
        html_doc = urllib.request.urlopen(url)
        soup = BeautifulSoup(html_doc, 'html.parser')
        return soup
