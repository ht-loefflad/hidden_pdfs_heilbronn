import json
import os

import pytest

from src.information_extraction.runner import InformationExtractionEngineRunner


class TestInformationExtractionEngineRunner:
    result_dirpath = "results"
    json_doc_long_filepath = os.path.join("results", "result.json")

    @pytest.fixture
    def json_doc_short(self):
        return {
            "Result": [
                {
                    "Metadata": {
                        "Storagepath": "pdfs\\Wegweiser_bei_seelischen_Problemen.pdf"
                    },
                    "Pdflink": "https://www.heilbronn.de//fileadmin/daten/stadtheilbronn/formulare/leben/beratungsstellen/Wegweiser_bei_seelischen_Problemen.pdf",
                    "Websitelink": "https://www.heilbronn.de//leben/gesundheit/beratungsstellen/ibb"
                },
                {
                    "Metadata": {
                        "Storagepath": "pdfs\\Beratungsstellen.pdf"
                    },
                    "Pdflink": "https://www.heilbronn.de//fileadmin/daten/stadtheilbronn/formulare/leben/beratungsstellen/Beratungsstellen.pdf",
                    "Websitelink": "https://www.heilbronn.de//leben/gesundheit/beratungsstellen/ibb"
                },
                {
                    "Metadata": {
                        "Storagepath": "pdfs\\HN_Innenstadt_Broschuere_7hEStG.pdf"
                    },
                    "Pdflink": "https://www.heilbronn.de//fileadmin/daten/stadtheilbronn/formulare/bauen_wohnen/Stadterneuerung/HN_Innenstadt_Broschuere_7hEStG.pdf",
                    "Websitelink": "https://www.heilbronn.de//stadterneuerung.html"
                },
                {
                    "Metadata": {
                        "Storagepath": "pdfs\\HN_Innenstadt_Broschuere_7hEStG.pdf"
                    },
                    "Pdflink": "https://www.heilbronn.de//fileadmin/daten/stadtheilbronn/formulare/bauen_wohnen/Stadterneuerung/HN_Innenstadt_Broschuere_7hEStG.pdf",
                    "Websitelink": "https://www.heilbronn.de//stadterneuerung.html"
                }
            ]
        }

    @pytest.fixture
    def json_doc_long(self):
        with open(self.json_doc_long_filepath, "r") as file:
            json_doc = json.load(file)

        return json_doc

    @pytest.fixture
    def iee_runner(self):
        return InformationExtractionEngineRunner(self.result_dirpath)

    def test_run_engine(self, iee_runner, json_doc_long):
        iee_runner.run_engine(json_doc_long)
