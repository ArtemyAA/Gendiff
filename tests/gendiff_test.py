from gendiff import generate_diff
import pytest
import os


@pytest.fixture
def fixtures_path():
    return os.path.join("tests", "fixtures")


def test1_for_json(fixtures_path):
    first_file = os.path.join(fixtures_path, "file1.json")
    second_file = os.path.join(fixtures_path, "file2.json")
    assert generate_diff(first_file, second_file) == ('{\n- \
follow: false\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ \
timeout: 20\n+ verbose: true\n}')
