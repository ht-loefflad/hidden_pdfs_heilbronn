from src.crawlers.factory import get_crawler

if __name__ == '__main__':
    crawler = get_crawler("beatiful_soup")
    crawler.run()
