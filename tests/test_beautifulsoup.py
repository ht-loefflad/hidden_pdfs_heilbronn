import pytest

from src.crawlers.beatifulsoup import BeatifulSoupCrawler

class TestBeautifulSoupCrawler:

    @pytest.fixture
    def bs_crawler(self):
        crawler = BeatifulSoupCrawler()
        return crawler

    def test_get_links(self, bs_crawler):
        soup = bs_crawler.get_links('https://www.heilbronn.de/sitemap.html')
        print(soup)