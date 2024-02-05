def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, int):
        return str(value)
    return f"'{str(value)}'"


def plainize(diff_tree, path=''):
    result = []
    for key, element in diff_tree.items():
        element_status = element.get('status')
        value = element.get('content')
        value_from = element.get('from')
        value_to = element.get('to')
        new_path = path + ('.' if path else '') + key
        if element_status == 'nested':
            result.append(plainize(value, new_path))
        elif element_status == 'added':
            result.append(f'Property {to_str(new_path)} \
was added with value: {to_str(value)}')
        elif element_status == 'removed':
            result.append(f'Property {to_str(new_path)} was removed')
        elif element_status == 'changed':
            result.append(f'Property {to_str(new_path)} was updated. \
From {to_str(value_from)} to {to_str(value_to)}')
    return '\n'.join(result)
