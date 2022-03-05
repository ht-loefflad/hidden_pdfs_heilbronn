import json


def read_json(json_file_obj: str) -> list:
    json_list = []
    json_file = open(json_file_obj)
    data = json.load(json_file)
    for i in data['Result']:
        json_list.append(i)
    json_file.close()
    return json_list
