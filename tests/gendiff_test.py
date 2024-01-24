from gendiff import generate_diff
import pytest
import os


@pytest.fixture
def fixtures_path():
    return os.path.join("tests", "fixtures")


def test1_for_json(fixtures_path):
    first_file = os.path.join(fixtures_path, "file1.json")
    second_file = os.path.join(fixtures_path, "file2.json")
    answer = os.path.join(fixtures_path, 'answer.py')
    expected = open(answer, 'r')
    assert generate_diff(first_file, second_file) == expected.read()
