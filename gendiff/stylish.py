def convert(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value


def get_children(directory):
    if directory.get('status') == 'directory':
        return directory.get('content')
    return None


def stylize(diff_tree, depth=0, fullfull='.'):
    result = []
    for key, element in diff_tree.items():
        current_depth = depth
        indent = current_depth * 4 - 2
        space = indent * fullfull
        if element['status'] == 'added':
            result.append(f'{space}+ {key}: {convert(element["content"])}')
        elif element['status'] == 'removed':
            result.append(f'{space}- {key}: {convert(element["content"])}')
        elif element['status'] == 'changed':
            result.append(f'{space}- {key}: {convert(element["from"])}')
            result.append(f'{space}+ {key}: {convert(element["to"])}')
        elif element['status'] == 'unchanged':
            result.append(f'{space}  {key}: {convert(element["content"])}')
        elif element['status'] == 'directory':
            one_step = get_children(element)
            if one_step:
                current_depth += 1
                result.append(f'{space}{key}: ')
                result.append(stylize(one_step, current_depth, fullfull))
    result_to_convert = '\n'.join(result)
    return f'{{\n{result_to_convert}\n}}'
