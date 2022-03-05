from abc import ABC, abstractmethod
from typing import Dict


class Crawler(ABC):
    @abstractmethod
    def run(self) -> Dict:
        pass
