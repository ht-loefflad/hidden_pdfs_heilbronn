from abc import ABC, abstractmethod
from typing import Dict


class Crawler(ABC):
    def __init__(self, result_dirpath: str):
        self.result_dirpath = result_dirpath

    @abstractmethod
    def run(self) -> Dict:
        pass
