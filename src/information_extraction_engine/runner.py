import os
import pkgutil
import importlib
from typing import List
from src.information_extraction_engine import InformationExtractor


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

    def _get_extractors(self) -> List:
        """Returns all classes inheriting from `InformationExtractor`"""
        package_classes = self._get_package_classes()
        information_extractors = [cls for cls in package_classes if issubclass(cls, InformationExtractor)]

        return information_extractors

    def _group_extractors(self):
        pass

    def _run_extractors(self):
        pass

    def run_engine(self):
        information_extractors = self._get_extractors()
        pre_processing_extractors, processing_extractors, post_processing_extractors = \
            self._group_extractors(information_extractors)
        self._run_extractors(pre_processing_extractors)
        self._run_extractors(processing_extractors)
        self._run_extractors(post_processing_extractors)
