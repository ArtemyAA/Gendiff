def to_string(data, depth=0, space_count=4, fullfill=' '):
    if isinstance(data, bool):
        return str(data).lower()
    elif data is None:
        return 'null'
    elif isinstance(data, dict):
        result = ['{']
        space = fullfill * depth * space_count
        depth += 1
        for key, value in data.items():
            result.append(f"{space}    {key}: {to_string(value, depth)}")
        result.append(f'{space}{"}"}')
        return '\n'.join(result)
    return data


def stylize(diff_tree, depth=0, space_count=4, fullfill=' '):
    result = ['{']
    indent = space_count * depth
    space = indent * fullfill
    depth += 1
    for key, element in diff_tree.items():
        element_status = element.get('status')
        value = element.get('content')
        value_from = element.get('from')
        value_to = element.get('to')
        if element_status == 'nested':
            result.append(
                f"{space}    {key}: {stylize(value, depth)}")
        elif element_status == 'added':
            result.append(f'{space}  + {key}: {to_string(value, depth)}')
        elif element_status == 'removed':
            result.append(f'{space}  - {key}: {to_string(value, depth)}')
        elif element_status == 'changed':
            result.append(
                f'{space}  - {key}: '
                f'{to_string(value_from, depth)}')
            result.append(
                f'{space}  + {key}: '
                f'{to_string(value_to, depth)}')
        else:
            result.append(f'{space}    {key}: {to_string(value, depth)}')
    result.append(space + '}')
    return '\n'.join(result)
