import os
import pkgutil
import importlib
from typing import List
from src.information_extraction_engine import InformationExtractor


class InformationExtractionEngineRunner:
    def _get_all_classes(self, filepath: str) -> List:
        pass

    def _get_extractors(self, package_dirname: str) -> List:

        for module_loader, name, is_package in pkgutil.iter_modules([package_dirname]):
            importlib.import_module('.' + name, __package__)

        package_classes = InformationExtractor.__subclasses__()


        filenames = os.listdir(package_dirname)
        filepaths = [os.path.join(package_dirname, filename) for filename in filenames]
        all_extractors = []
        for filepath in filepaths:
            extractors_in_file = self._get_extractors_from_file(filepath)
            all_extractors.append(extractors_in_file)

    def _separate_extractors(self):
        pass

    def _run_extractors(self):
        pass

    def run_engine(self):
        information_extractors = self._get_extractors(os.path.dirname(__file__))
        pre_processing_extractors, processing_extractors, post_processing_extractors = \
            self._separate_extractors(information_extractors)
        self._run_extractors(pre_processing_extractors)
        self._run_extractors(processing_extractors)
        self._run_extractors(post_processing_extractors)
