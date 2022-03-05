import json
import os

from src.information_extraction_engine import InformationExtractor, ProcessingType


class Hasher(InformationExtractor):
    TYPE = ProcessingType.PreProcessing

    def run(self, json_doc):
        self._create_hash_codes(json_doc)
        self._check_for_duplicates(json_doc)

    def _create_hash_codes(self, json_doc):
        for result in json_doc["Result"]:
            # creating a hash value
            path = result['Metadata']['Storagepath']
            with open(os.path.abspath(path), 'rb') as file:
                result['Hash'] = hash(file.read())

    @staticmethod
    def _find_duplicate_hash_codes(json_doc):
        all_hash_codes = [result["Hash"] for result in json_doc["Result"]]
        unique_hash_codes = []
        duplicate_hash_codes = []
        for hash_code in all_hash_codes:
            if hash_code not in unique_hash_codes:
                unique_hash_codes.append(hash_code)
            else:
                duplicate_hash_codes.append(hash_code)

        return duplicate_hash_codes

    def _check_for_duplicates(self, json_doc):
        duplicate_hash_codes = self._find_duplicate_hash_codes(json_doc)
        duplicate_results = []
        for result in json_doc["Result"]:
            hash_code = result["Hash"]
            if hash_code in duplicate_hash_codes:
                result["IsDuplicate"] = True
                duplicate_results.append(result)
            else:
                result["IsDuplicate"] = False

    def _write_duplicates(self):
        findduplicaes