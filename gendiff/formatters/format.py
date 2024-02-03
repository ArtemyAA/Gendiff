from gendiff import stylize, jsonize, plainize


def format_data(difference, format):
    if format == 'stylish':
        return stylize(difference)
    elif format == 'json':
        return jsonize(difference)
    elif format == 'plain':
        return plainize(difference)
