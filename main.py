from src.crawlers.factory import get_crawler
from src.utils import make_sure_dir_exists

RESULT_DIR = "pdfs"
CRAWLER = "scratch"

if __name__ == '__main__':
    make_sure_dir_exists(RESULT_DIR)
    crawler = get_crawler("scratch")
    crawler.run()
