import json
import os

import pytest


class TestConfig:
    result_dirpath = os.path.join("tests", "results")
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
