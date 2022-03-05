import pytest

from src.readers.hasher import Hasher


class TestHasher:
    @pytest.fixture
    def hasher(self):
        return Hasher()

    @pytest.fixture
    def json_doc(self):
        json_doc = {
            "Result": [
                {
                    "Metadata": {
                        "Storagepath": "pdfs\\Wegweiser_bei_seelischen_Problemen.pdf"
                    },
                    "Pdflink": "https://www.heilbronn.de//fileadmin/daten/stadtheilbronn/formulare/leben/beratungsstellen/Wegweiser_bei_seelischen_Problemen.pdf",
                    "Websitelink": "https://www.heilbronn.de//leben/gesundheit/beratungsstellen/ibb",
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
                        "Storagepath": "pdfs\\Beratungsstellen.pdf"
                    },
                    "Pdflink": "https://www.heilbronn.de//fileadmin/daten/stadtheilbronn/formulare/leben/beratungsstellen/Beratungsstellen.pdf",
                    "Websitelink": "https://www.heilbronn.de//leben/gesundheit/beratungsstellen/ibb"
                }
            ]
        }
        return json_doc

    def test_run(self, hasher, json_doc):
        hasher.run(json_doc)
