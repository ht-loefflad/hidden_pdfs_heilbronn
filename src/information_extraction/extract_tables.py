import os.path
from typing import Dict

import pandas as pd
import tabula
# from src.utils import read_json

from src.information_extraction import InformationExtractor, ProcessingType


class ExtractTables(InformationExtractor):
    TYPE = ProcessingType.PreProcessing

    def __init__(self, result_dirpath, name):
        super().__init__(result_dirpath, name)

    def run(self, json_doc) -> Dict:
        base_directory_tables = os.path.join(self.result_dirpath, 'tables')
        self._create_subfolder(base_directory_tables)
        for element in json_doc['Result']:
            # create sub-folders
            storage_path = element['Metadata']['Storagepath']
            directory_name = self._extract_file_name(storage_path)
            print(directory_name)
            tables_path = os.path.join(base_directory_tables, directory_name)
            self._create_subfolder(tables_path)

            # extract all tables in a list
            df_list = self._extract_tables(storage_path)

            # save extracted tables
            self._export_tables(df_list, tables_path)

        return json_doc

    def _extract_tables(self, doc_path):
        df_list = []
        try:
            df_list = tabula.read_pdf(doc_path, pages='all')
        except:
            f"couldn't read {doc_path}"
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
        extracted_name = os.path.basename(storage_path)
        file_name = extracted_name.split('.')[0]
        return os.path.basename(file_name)
