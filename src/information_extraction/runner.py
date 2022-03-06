import json
import os
import pkgutil
import importlib
from typing import List, Tuple, Union, Dict, Sequence
from src.information_extraction import InformationExtractor, ProcessingType


class InformationExtractionEngineRunner:
    def __init__(self, result_dirpath: str, package_dirnanme: str = None):
        self.result_dirpath = result_dirpath
        if package_dirnanme is not None:
            self.package_dirname = package_dirnanme
        else:
            self.package_dirname = os.path.dirname(__file__)

    def _get_packages(self) -> Dict:
        """Import and return all class objects inside the package `package_name`"""
        for module_loader, name, is_package in pkgutil.iter_modules([self.package_dirname]):
            importlib.import_module('.' + name, __package__)
        packages = {cls.__name__: cls for cls in InformationExtractor.__subclasses__()}

        return packages

    def _get_information_extractors(self) -> Dict:
        """Returns all classes inheriting from `InformationExtractor`"""
        packages = self._get_packages()
        information_extractors = {name: cls for name, cls in packages.items() if issubclass(cls, InformationExtractor)}

        return information_extractors

    @staticmethod
    def _group_by_type(information_extractors: Dict) -> Tuple[Dict, Dict, Dict]:
        """Groups extractors into pre-processing, processing and post-processing extractors"""
        pre_processing_extractors = {}
        processing_extractors = {}
        post_processing_extractors = {}

        for name, cls in information_extractors.items():
            if cls.TYPE == ProcessingType.PreProcessing:
                pre_processing_extractors[name] = cls

            elif cls.TYPE == ProcessingType.Processing:
                processing_extractors[name] = cls

            elif cls.TYPE == ProcessingType.PostProcessing:
                post_processing_extractors[name] = cls

            else:
                raise ValueError(f"Unknown PreprocessingType provided: {cls.TYPE}")

        return pre_processing_extractors, processing_extractors, post_processing_extractors

    def _run_by_type(self, information_extractors: Dict, json_doc: Dict) -> Dict:
        """Executes all extractors of a certain type"""
        for extractor_name, extractor_cls in information_extractors.items():
            extractor = extractor_cls(self.result_dirpath, extractor_name)
            print(f"Currently running {extractor.name}")
            json_doc = extractor.run(json_doc)

        return json_doc

    def run_engine(self, json_doc: Dict):
        """Runs the complete information extraction engine"""
        information_extractors = self._get_information_extractors()
        prep_processing, processing, post_processing = self._group_by_type(information_extractors)
        json_doc = self._run_by_type(prep_processing, json_doc)
        json_doc = self._run_by_type(processing, json_doc)
        json_doc = self._run_by_type(post_processing, json_doc)

        result = json.dumps(json_doc, indent=4, sort_keys=True, ensure_ascii=False).encode('utf8')
        result_filepath = os.path.join(self.result_dirpath, "result.json")
        with open(result_filepath, 'wb') as f:
            f.write(result)
            print(f"Saved information extraction results to {result_filepath}")
