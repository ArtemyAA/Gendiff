from gendiff import generate_diff
import pytest
import os


def create_path(file_name):
    return os.path.join("tests", "fixtures", file_name)


def read_txt_file(file_name):
    with open(create_path(file_name)) as file:
        result = file.read()
    return result


@pytest.mark.parametrize('input1,input2,format,expected', [
    ('file1.json', 'file2.json', 'stylish', 'answer.txt'),
    ('file1.yaml', 'file2.yaml', 'stylish', 'answer.txt'),
    ('tree1.json', 'tree2.json', 'stylish', 'answer_trees.txt'),
    ('tree1.yaml', 'tree2.yaml', 'stylish', 'answer_trees.txt'),
    ('tree1.json', 'tree2.json', 'plain', 'answer_plain.txt'),
    ('tree1.yaml', 'tree2.yaml', 'plain', 'answer_plain.txt'),
    ('tree1.json', 'tree2.json', 'json', 'answer_json.txt'),
    ('tree1.yaml', 'tree2.yaml', 'json', 'answer_json.txt')])
def test_for_json(input1, input2, format, expected):
    assert generate_diff(create_path(input1), create_path(input2), format)\
        == read_txt_file(expected)
