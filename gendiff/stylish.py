def convert(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return value


def dict_to_string(data, depth=0, space_count=4, fullfill=' '):
    if not isinstance(data, dict):
        return data
    result = ['{']
    space = fullfill * depth * space_count
    depth += 1
    for key, value in data.items():
        result.append(f"{space}    {key}: {dict_to_string(value, depth)}")
    result.append(f'{space}{"}"}')
    return '\n'.join(result)

def stylize(diff_tree, depth=0, space_count=4, fullfill=' '): # noqa C901
    result = ['{']
    indent = space_count * depth
    space = indent * fullfill
    depth += 1
    for key, element in diff_tree.items():
        element_status = element.get('status')
        value = convert(element.get('content'))
        value_from = convert(element.get('from'))
        value_to = convert(element.get('to'))
        if element_status == 'directory':
            result.append(
                f"{space}    {key}: {stylize(value, depth)}")
        elif element_status == 'added':
            result.append(f'{space}  + {key}: {dict_to_string(value, depth)}')
        elif element_status == 'removed':
            result.append(f'{space}  - {key}: {dict_to_string(value, depth)}')
        elif element_status == 'changed':
            result.append(f'{space}  - {key}: {dict_to_string(value_from, depth)}') # noqa E501
            result.append(f'{space}  + {key}: {dict_to_string(value_to, depth)}') # noqa E501
        elif element_status == 'unchanged':
            result.append(f'{space}    {key}: {dict_to_string(value, depth)}')
        else:
            raise ValueError
    result.append(space + '}')
    return '\n'.join(result)
