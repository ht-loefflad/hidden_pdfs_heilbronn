from abc import ABC, abstractmethod


class Crawler(ABC):
    @abstractmethod
    def run(self):
        pass
