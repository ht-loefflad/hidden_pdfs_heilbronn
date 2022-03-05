from abc import ABC, abstractmethod
from enum import Enum


class ProcessingType(Enum):
    PreProcessing = 0,
    Processing = 1,
    PostProcessing = 2


class InformationExtractor(ABC):
    TYPE: ProcessingType = ...

    @abstractmethod
    def run(self):
        pass
