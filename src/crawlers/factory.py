from src.crawlers.scratch_crawler import ScratchCrawler
from src.crawlers.beatifulsoup import BeatifulSoupCrawler


def get_crawler(type: str, result_dirpath: str):
    crawlers = {
        "beatiful_soup": BeatifulSoupCrawler,
        "scratch": ScratchCrawler
    }
    return crawlers[type](result_dirpath)
