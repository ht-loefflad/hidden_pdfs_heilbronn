from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict


class ProcessingType(Enum):
    PreProcessing = 0,
    Processing = 1,
    PostProcessing = 2


class InformationExtractor(ABC):
    TYPE: ProcessingType = ...

    @abstractmethod
    def run(self, json_doc: Dict):
        pass
