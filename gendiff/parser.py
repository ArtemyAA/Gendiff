import json
import yaml
import argparse


def parse():
    parser = argparse.ArgumentParser(description='Compares two configuration \
files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='see format of output')
    args = parser.parse_args()
    return args.first_file, args.second_file


def extract_data(file_path):
    if file_path.endswith('.json'):
        return json.load(open(file_path))
    if file_path.endswith('.yaml') or file_path.endswith('.yml'):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
