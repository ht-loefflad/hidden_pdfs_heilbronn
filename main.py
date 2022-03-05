import os

from src.crawlers.factory import get_crawler
from src.information_extraction.runner import InformationExtractionEngineRunner
from src.utils import make_sure_dir_exists

RESULT_DIR = "results"
CRAWLER = "scratch"

if __name__ == '__main__':
    make_sure_dir_exists(RESULT_DIR)
    crawler = get_crawler("scratch", RESULT_DIR)
    json_doc = crawler.run()
    iee_runner = InformationExtractionEngineRunner()
    iee_runner.run_engine(json_doc)
