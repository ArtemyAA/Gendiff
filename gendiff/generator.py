import json


def generate_diff(file1_path, file2_path):
    data1 = json.load(open(file1_path))
    data2 = json.load(open(file2_path))
    diff = []

    def to_str(smth):
        return str(smth).lower()

    for key in sorted(data1.keys() | data2.keys()):
        if key not in data2:
            diff.append(f'- {key}: {to_str(data1[key])}')
        elif key not in data1:
            diff.append(f'+ {key}: {to_str(data2[key])}')
        elif key in data1 and data2 and data1[key] != data2[key]:
            diff.append(f'- {key}: {to_str(data1[key])}')
            diff.append(f'+ {key}: {to_str(data2[key])}')
        else:
            diff.append(f'  {key}: {to_str(data1[key])}')
    diff_to_str = '\n'.join(diff)
    return f'{{\n{diff_to_str}\n}}'
