import json
import yaml


def define_type(file_name):
    if file_name.endswith('.json'):
        type = '.json'
    elif file_name.endswith('.yaml') or file_name.endswith('.yml'):
        type = '.yaml'
    return type


def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


def extract_data(file_path):
    if define_type(file_path) == '.json':
        return load_json(file_path)
    elif define_type(file_path) == '.yaml':
        return load_yaml(file_path)
