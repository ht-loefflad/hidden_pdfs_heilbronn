import os.path

import pandas as pd
import tabula
# from src.utils import read_json

from src.information_extraction_engine import InformationExtractor, ProcessingType


class ExtractTables(InformationExtractor):
    def __init__(self):
        TYPE = ProcessingType.PreProcessing

    def run(self, json_doc):
        self._create_subfolder('../../tables')
        for element in json_doc['Result']:
            # create sub-folders
            storage_path = element['Metadata']['Storagepath']
            directory_name = self._extract_file_name(storage_path)
            self._create_subfolder(directory_name)

            # extract all tables in a list
            df_list = self._extract_tables(storage_path)

            self._export_tables(df_list, directory_name)
            # save extracted tables

    def _extract_tables(self, doc_path):
        df_list = tabula.read_pdf(doc_path, pages='all')
        return df_list

    def _export_tables(self, df_list, directory_name):
        j = 0
        for df in df_list:
            table_name = f'{directory_name}/table_{j}.csv'
            df.to_csv(table_name)
            j += 1


    def _create_subfolder(self, file_name):
        if not os.path.exists(file_name):
            os.mkdir(file_name)

    def _extract_file_name(self, storage_path):
        return os.path.basename(storage_path)
