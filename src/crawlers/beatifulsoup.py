import re
from typing import List, Tuple, Dict

from src.crawlers import Crawler

from bs4 import BeautifulSoup
import urllib.request
import json

class BeatifulSoupCrawler(Crawler):
    def __init__(
            self,
            result_dirpath: str,
            start_url: str = "https://www.heilbronn.de/sitemap.html",
            base_url: str = "https://www.heilbronn.de"
    ):
        super().__init__(result_dirpath)
        self.start_url = start_url
        self.base_url = base_url
        self.websites = []
        self.pdfs = []

    @staticmethod
    def _get_links(url):
        html_doc = urllib.request.urlopen(url)
        soup = BeautifulSoup(html_doc, 'html.parser')
        filter_fn = lambda tag: (tag.name == "a") and (":" not in tag["href"]) and ("/" in tag["href"])
        tags = soup.findAll(filter_fn)
        links = [tag["href"] for tag in tags]

        return links

    def _complete_links(self, links: List[str]) -> List[str]:
        complete_links = [f"{self.base_url}{link}" for link in links]

        return complete_links

    @staticmethod
    def _separate_links(links: List[str]) -> Tuple[List[str], List[str]]:
        websites, pdfs = [], []
        for link in links:
            if ".pdf" in link:
                pdfs.append(link)
            else:
                websites.append(link)

        return websites, pdfs

    def _crawl_website(self, url):
        links = self._get_links(url)
        complete_links = self._complete_links(links)
        websites, pdfs = self._separate_links(complete_links)
        self.websites.extend(websites)
        self.pdfs.extend(pdfs)

        for website in websites:
            self._crawl_website(website)

    def run(self) -> Dict:
        self._crawl_website(self.start_url)
