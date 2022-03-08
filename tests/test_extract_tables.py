import pytest

from src.information_extraction.extract_tables import ExtractTables
from tests.test_config import TestConfig


class TestExtractTables(TestConfig):

    @pytest.fixture
    def extract_tables(self):
        extract_tables = ExtractTables(self.result_dirpath, "ExtractTables")
        return extract_tables

    def test_extract_tables(self, extract_tables):
        df_list = extract_tables._extract_tables('../pdfs/Sozialdatenatlas.pdf')
        print(df_list)

    def test_export_tables(self, extract_tables):
        df_list = extract_tables._extract_tables('../pdfs/Sozialdatenatlas.pdf')
        # print(df)
        extract_tables._export_tables(df_list, '../results')

    def test_run(self, extract_tables, json_doc_long):
        json_doc_long["Result"] = json_doc_long["Result"][:20]
        extract_tables.run(json_doc_long)
