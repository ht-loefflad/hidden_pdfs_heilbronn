import json

import pytest

from src.information_extraction_engine.extract_tables import ExtractTables


class TestExtractTables:

    @pytest.fixture
    def extract_tables(self):
        extract_tables = ExtractTables()
        return extract_tables

    def test_extract_tables(self, extract_tables):
        df_list = extract_tables._extract_tables('../pdfs/Sozialdatenatlas.pdf')
        print(df_list)

    def test_export_tables(self, extract_tables):
        df_list = extract_tables._extract_tables('../pdfs/Sozialdatenatlas.pdf')
        # print(df)
        extract_tables._export_tables(df_list, '../results')

    def test_run(self, extract_tables):
        fp = open('../pdfs/result.json')
        json_doc = json.load(fp)
        extract_tables.run(json_doc)
