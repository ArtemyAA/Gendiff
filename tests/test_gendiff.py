from gendiff import generate_diff
import pytest
import os


def build_fixture_path(file_name):
    return os.path.join("tests", "fixtures", file_name)


def read_content(file_name):
    with open(file_name) as file:
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
def test_for_gendiff(input1, input2, format, expected):
    assert generate_diff(
        build_fixture_path(input1),
        build_fixture_path(input2),
        format
    ) == read_content(build_fixture_path(expected))
