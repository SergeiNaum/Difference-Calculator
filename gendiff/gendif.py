"""Generate Diff - main module"""

import pathlib
from gendiff.parcer import parce
from gendiff.tree import build_tree
from gendiff.formatter import format


def get_file_ex(file_path: str) -> str:
    """Get file extension from file path."""
    file = pathlib.Path(file_path)
    extension = file.suffix

    return extension


def get_f_data(file_path: str) -> str:
    """Get data from file."""
    extension = get_file_ex(file_path)
    data = parce(file_path, extension)

    return data


def generate_diff(file_path1: str,
                  file_path2: str,
                  format_name='stylish') -> str:

    dictionary1 = dict(get_f_data(file_path1))
    dictionary2 = dict(get_f_data(file_path2))
    tree = build_tree(dictionary1, dictionary2)
    diff = format(tree, format_name)

    return diff
