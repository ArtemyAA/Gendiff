import gendiff.diff
from gendiff.parser import extract_data
import gendiff.formatters.format as formatter


def generate_diff(file1_path, file2_path, format='stylish'):
    data1 = extract_data(file1_path)
    data2 = extract_data(file2_path)
    diff = gendiff.diff.make_diff(data1, data2)
    return formatter.format_data(diff, format)
