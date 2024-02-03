def make_diff(data1, data2):
    diff = {}
    all_keys = set(data1.keys()) | set(data2.keys())
    for key in sorted(all_keys):
        if isinstance(data1.get(key), dict)\
                and isinstance(data2.get(key), dict):
            diff[key] = {
                'status': 'nested',
                'content': make_diff(data1[key], data2[key])
            }
        elif key not in data1:
            diff[key] = {
                'status': 'added',
                'content': data2[key]
            }
        elif key not in data2:
            diff[key] = {
                'status': 'removed',
                'content': data1[key]
            }
        else:
            if data1[key] == data2[key]:
                diff[key] = {
                    'status': 'unchanged',
                    'content': data2[key]
                }
            else:
                diff[key] = {
                    'status': 'changed',
                    'from': data1[key],
                    'to': data2[key]
                }
    return diff
