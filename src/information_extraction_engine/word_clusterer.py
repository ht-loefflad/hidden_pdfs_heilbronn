import json
import os
import re
from copy import copy

import PyPDF2
from src.information_extraction_engine import InformationExtractor, ProcessingType


class WordClusterer(InformationExtractor):

    TYPE = ProcessingType.Processing

    def run(self, json_doc):
        print("Clustering words")
        temp = [x for x in json_doc["Result"] if 'Wordcountfile' in x['Metadata'].keys()]
        all_files = [x['Metadata']['Wordcountfile'] for x in temp]
        all_contents = [self._read_json(x) for x in all_files]
        all_keys = {}
        for x in all_contents:
            for key in x.keys():
                all_keys[key] = all_keys[key] + x[key] if key in all_keys.keys() else x[key]

        sorted_keys = sorted(all_keys.items(), key=lambda x: -x[1])
        stuff = [0]
        for sorted_key in sorted_keys:
            stuff.append(sorted_key[1]+stuff[-1])
        stuff.remove(stuff[0])
        stuff = [x/stuff[-1] for x in stuff]
        relevant = []
        for i in range(len(stuff)):
            if stuff[i] > .5: #TODO: this value might be bad
                relevant.append(sorted_keys[i][0])

        tags = [self._extract_tags(relevant, x) for x in all_contents]
        for i in range(len(all_contents)):
            json_doc['Result'][i]['Metadata']['Tags'] = tags[i]
        return json_doc

    def _extract_tags(self, relevant_keys, all_contents):
        relevant_per_file = [(x, all_contents[x]) for x in relevant_keys if x in all_contents.keys()]
        sorted_keys = sorted(relevant_per_file, key=lambda x: -x[1])
        sorted_keys = [x for x in sorted_keys if x[1] > 2]
        return [x[0] for x in sorted_keys[:20]]

    def _get_only_unique_keys(self, all_keys, word_counts):
        working_dict = copy(word_counts)
        for key in word_counts.keys():
            if key in all_keys:
                del working_dict[key]
        return working_dict

    def _read_json(self, path):
        with open(path, 'rb') as f:
            content = f.read().decode('utf8')
            return json.loads(content)
