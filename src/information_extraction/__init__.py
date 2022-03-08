from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict


class ProcessingType(Enum):
    PreProcessing = 0,
    Processing = 1,
    PostProcessing = 2


class InformationExtractor(ABC):
    TYPE: ProcessingType = ...

    def __init__(self, result_dirpath: str, name: str):
        if result_dirpath is not None:
            self.result_dirpath = result_dirpath
        else:
            self.result_dirpath = "results"
        self.name = name

    @abstractmethod
    def run(self, json_doc: Dict) -> Dict:
        pass
