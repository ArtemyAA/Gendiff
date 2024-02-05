import gendiff.formatters.json as json
import gendiff.formatters.stylish as stylish
import gendiff.formatters.plain as plain


def format_data(difference, format):
    if format == 'stylish':
        return stylish.stylize(difference)
    elif format == 'json':
        return json.jsonize(difference)
    elif format == 'plain':
        return plain.plainize(difference)
    else:
        raise ValueError("Unsupported format")
