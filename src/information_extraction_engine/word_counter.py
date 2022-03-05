import json
import os
import re

import PyPDF2
from src.information_extraction_engine import InformationExtractor, ProcessingType


class WordCounter(InformationExtractor):

    TYPE = ProcessingType.PreProcessing

    def __init__(self):
        self._regex = re.compile('[a-zA-ZäÄöÖüÜß]{4,}')

    def run(self, json_doc):
        return [self._process(x) for x in json_doc["Result"]]

    def _process(self, pdf_info):
        print(pdf_info['Metadata']['Storagepath'])
        text = ""
        try:
            with open(pdf_info['Metadata']['Storagepath'], 'rb') as file:
                # creating a pdf reader object
                fileReader = PyPDF2.PdfFileReader(file)

                # print the number of pages in pdf file
                if fileReader.numPages == 0:
                    print(pdf_info['Metadata']['Storagepath'] + ' not readable')
                    pdf_info['Metadata']['Readable'] = False
                    return pdf_info


                for page in fileReader.pages:
                    text += page.extractText()
            pdf_info['Metadata']['Readable'] = True
            occurrences = self._extract_words(text)
            storage_dir = os.path.dirname(pdf_info['Metadata']['Storagepath']) ## directory of file
            storage_file_name = os.path.split(pdf_info['Metadata']['Storagepath'])[-1].split('.')[0] + '.wordcount.json'
            storage_path = os.path.abspath( os.path.join(storage_dir, storage_file_name))
            pdf_info['Metadata']['Wordcountfile'] = storage_path
            result = json.dumps(occurrences, indent=4, sort_keys=True, ensure_ascii=False).encode('utf8')
            with open(storage_path, 'wb') as f:
                f.write(result)
        except:
            pdf_info['Metadata']['Readable'] = False
        return pdf_info

    def _extract_words(self, text):
        text = text.replace('-\n', '')
        text = text.replace('\n-', '')
        text = text.replace('\n', ' ')
        all_words = re.findall(self._regex, text)
        all_words = [x.lower() for x in all_words]
        single_word = set(all_words)
        occurrences = {}
        for word in single_word:
            occurrences[word] = all_words.count(word)
        return occurrences
