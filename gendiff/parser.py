import json
import yaml
import os


def parse_content(content, extension):
    if extension == 'json':
        return json.load(content)
    elif extension == 'yaml' or extension == 'yml':
        return yaml.safe_load(content)
    raise ValueError(f"Unsupported extension: {extension}")


def fetch_data(file_path):
    _, extension = os.path.splitext(file_path)
    with open(file_path, 'r') as file:
        return parse_content(file, extension[1:])
