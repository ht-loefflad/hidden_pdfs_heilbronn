from src.readers.readerjson import read_json


def get_reader(type: str):
    readers = {
        "json": read_json()
    }
    return readers[type]
