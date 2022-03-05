import os
import pkgutil
import importlib
from typing import List, Tuple, Union, Dict
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

    def _get_information_extractor_classes(self) -> List:
        """Returns all classes inheriting from `InformationExtractor`"""
        package_classes = self._get_package_classes()
        information_extractor_classes = [cls for cls in package_classes if issubclass(cls, InformationExtractor)]

        return information_extractor_classes

    @staticmethod
    def _group_information_extractors(information_extractor_classes: List) -> Tuple[List, List, List]:
        """Groups extractors into pre-processing, processing and post-processing extractors"""
        pre_processing_extractors = []
        processing_extractors = []
        post_processing_extractors = []

        for information_extractor_cls in information_extractor_classes:
            if information_extractor_cls.TYPE == ProcessingType.PreProcessing:
                pre_processing_extractors.append(information_extractor_cls())

            elif information_extractor_cls.TYPE == ProcessingType.Processing:
                processing_extractors.append(information_extractor_cls())

            elif information_extractor_cls.TYPE == ProcessingType.PostProcessing:
                post_processing_extractors.append(information_extractor_cls())

            else:
                raise ValueError(f"Unknown PreprocessingType provided: {information_extractor_cls.TYPE}")

        return pre_processing_extractors, processing_extractors, post_processing_extractors

    @staticmethod
    def _run_extractors(extractors: List, json_doc: Dict):
        """Executes all extractors in `extractors`"""
        for extractor in extractors:
            extractor.run(json_doc)

    def run_engine(self, json_doc: Dict):
        """Runs the complete information extraction engine"""
        information_extractor_classes = self._get_information_extractor_classes()
        pre_processing_extractors, processing_extractors, post_processing_extractors = \
            self._group_information_extractors(information_extractor_classes)
        self._run_extractors(pre_processing_extractors, json_doc)
        self._run_extractors(processing_extractors, json_doc)
        self._run_extractors(post_processing_extractors, json_doc)
