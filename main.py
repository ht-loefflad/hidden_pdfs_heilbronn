from src.crawlers.factory import get_crawler
from src.readers.factory import get_reader

if __name__ == '__main__':
    crawler = get_crawler("beatiful_soup")
    crawler.run()

