import os
import pkgutil
import importlib
from typing import List, Tuple
from src.information_extraction_engine import InformationExtractor, ProcessingType


class InformationExtractionEngineRunner:
    def __init__(self, package_dirnanme: str = None):
        if package_dirnanme is not None:
            self.package_dirname = package_dirnanme
        else:
            self.package_dirname = os.path.dirname(__file__)

    def _get_package_classes(self) -> List:
        """Import and return all class objects inside the package `package_name`"""
        for module_loader, name, is_package in pkgutil.iter_modules([self.package_dirname]):
            importlib.import_module('.' + name, __package__)
        package_classes = InformationExtractor.__subclasses__()

        return package_classes

    def _get_information_extractors(self) -> List:
        """Returns all classes inheriting from `InformationExtractor`"""
        package_classes = self._get_package_classes()
        information_extractors = [cls for cls in package_classes if issubclass(cls, InformationExtractor)]

        return information_extractors

    def _group_information_extractors(self, information_extractors: List) -> Tuple[List, List, List]:
        """Groups extractors into pre-processing, processing and post-processing extractors"""
        pre_processing_extractors = []
        processing_extractors = []
        post_processing_extractors = []

        for information_extractor in information_extractors:
            if information_extractor.TYPE == ProcessingType.PreProcessing:
                pre_processing_extractors.append(information_extractor)

            elif information_extractor.TYPE == ProcessingType.Processing:
                processing_extractors.append(information_extractor)

            elif information_extractor.TYPE == ProcessingType.PostProcessing:
                post_processing_extractors.append(information_extractor)

            else:
                raise ValueError(f"Unknown PreprocessingType provided: {information_extractor.TYPE}")

        return pre_processing_extractors, processing_extractors, post_processing_extractors

    def _run_extractors(self):
        pass

    def run_engine(self):
        information_extractors = self._get_information_extractors()
        pre_processing_extractors, processing_extractors, post_processing_extractors = \
            self._group_information_extractors(information_extractors)
        self._run_extractors(pre_processing_extractors)
        self._run_extractors(processing_extractors)
        self._run_extractors(post_processing_extractors)
