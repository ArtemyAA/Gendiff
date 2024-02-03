import gendiff


def generate_diff(file1_path, file2_path, format='stylish'):
    data1 = gendiff.extract_data(file1_path)
    data2 = gendiff.extract_data(file2_path)
    diff = gendiff.make_diff(data1, data2)
    style = gendiff.format_data(diff, format)
    return style
