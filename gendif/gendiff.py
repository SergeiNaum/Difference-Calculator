"""Generate Diff - main module"""

import pathlib
from gendif.parcer import parce
from gendif.tree import build_tree
from gendif.formatter import formatting


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
                  format='stylish') -> str:

    dictionary1 = dict(get_f_data(file_path1))
    dictionary2 = dict(get_f_data(file_path2))
    tree = build_tree(dictionary1, dictionary2)
    diff = formatting(tree, format)

    return diff
