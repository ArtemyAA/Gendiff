import json
import yaml
import os


def parse_extension(content, extension):
    if extension == 'json':
        return json.load(content)
    elif extension == 'yaml':
        return yaml.safe_load(content)
    else:
        raise ValueError(f"Unsupported extension: {extension}")


def extract_data(file_path):
    _, extension = os.path.splitext(file_path)
    with open(file_path, 'r') as file:
        return parse_extension(file, extension[1:])
