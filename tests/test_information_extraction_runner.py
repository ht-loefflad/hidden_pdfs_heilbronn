import pytest

from src.information_extraction.runner import InformationExtractionEngineRunner
from tests.test_config import TestConfig


class TestInformationExtractionEngineRunner(TestConfig):
    @pytest.fixture
    def iee_runner(self):
        return InformationExtractionEngineRunner(self.result_dirpath)

    def test_run_engine(self, iee_runner, json_doc_long):
        iee_runner.run_engine(json_doc_long)
