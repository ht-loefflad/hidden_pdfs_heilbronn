from src.crawlers.beatifulsoup import BeatifulSoupCrawler


def get_crawler(type: str):
    crawlers = {
        "beatiful_soup": BeatifulSoupCrawler()
    }
    return crawlers[type]
