import pytest

from src.information_extraction_engine.runner import InformationExtractionEngineRunner


class TestInformationExtractionEngineRunner:
    @pytest.fixture
    def iee_runner(self):
        return InformationExtractionEngineRunner()

    def test_run_engine(self, iee_runner):
        iee_runner.run_engine()
