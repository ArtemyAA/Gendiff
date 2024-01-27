def make_diff(data1, data2):
    diff = {}
    keys = data1.keys() | data2.keys()
    for key in sorted(keys):
        if key not in data1:
            diff[key] = {'status': 'added', 'content': data2[key]}
        elif key not in data2:
            diff[key] = {'status': 'removed', 'content': data1[key]}
        elif key in data1 and key in data2 and data1[key] != data2[key]:
            diff[key] = {'status': 'changed', 'from': data1[key], 'to': data2[key]}
        elif key in data1 and key in data2 and data1[key] == data2[key]:
            diff[key] = {'status': 'unchanged', 'content': data2[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = {'status': 'directory',
                         'content': make_diff(data1[key], data2[key])}
    return diff
