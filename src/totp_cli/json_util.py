import json


def read_json(file_path: str) -> dict:
    with open(file_path, mode="r") as file:
        return json.load(file)

def write_json(file_path: str, content: dict) -> None:
    with open(file_path, mode="w+") as file:
        json.dump(content, file)