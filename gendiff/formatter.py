"""Formatter module - formatting the tree with the selected formatter"""

from gendiff.formatters import format_stylish, format_plain, format_json


def format(tree: dict, format_name='stylish') -> str:
    formats = {
        'stylish': format_stylish,
        'json': format_json,
        'plain': format_plain,
    }
    if format_name in formats:
        return formats[format_name](tree)

    raise ValueError(f'Unknown format: {format_name}')
