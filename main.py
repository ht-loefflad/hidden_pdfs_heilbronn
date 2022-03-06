import os
from datetime import datetime

from src.crawlers.factory import get_crawler
from src.information_extraction.runner import InformationExtractionEngineRunner
from src.utils import make_sure_dir_exists

RESULT_DIR = "results"
CRAWLER = "scratch"

if __name__ == '__main__':
    current_ts = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
    current_result_dir = os.path.join(RESULT_DIR, current_ts)
    print(f"Current result directory: {current_result_dir}")
    make_sure_dir_exists(current_result_dir)
    crawler = get_crawler("scratch", current_result_dir)
    json_doc = crawler.run()
    iee_runner = InformationExtractionEngineRunner(current_result_dir)
    iee_runner.run_engine(json_doc)
