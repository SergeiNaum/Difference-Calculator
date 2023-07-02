"""Generate Diff - main module"""

import pathlib
from gendif.parcer import parce


def get_file_ex(file_path: str) -> str:
    """Get file extension from file path."""
    file_path = pathlib.Path(file_path)
    extension = file_path.suffix

    return extension


def get_f_data(file_path: str) -> str:
    """Get data from file."""
    extension = get_file_ex(file_path)
    data = parce(file_path, extension)

    return data


def generate_diff(file_path1: str,
                  file_path2: str):
    result = []

    dictionary1 = dict(get_f_data(file_path1))
    dictionary2 = dict(get_f_data(file_path2))
    keys1 = set(dictionary1.keys())
    keys2 = set(dictionary2.keys())
    all_keys = keys1 | keys2

    for key in all_keys:
        if key in keys1 and key not in keys2:
            result.append(f"- {key}: {dictionary1[key]}")
        elif key in keys2 and key not in keys1:
            result.append(f"+ {key}: {dictionary2[key]}")
        elif dictionary1[key] != dictionary2[key]:
            result.append(f"- {key}: {dictionary1[key]}")
            result.append(f"+ {key}: {dictionary2[key]}")
        else:
            result.append(f"  {key}: {dictionary1[key]}")

    # return sorted(result, key=lambda x: x[2])
    # for line in sorted(result, key=lambda x: x[2]):
    #     print(line)
    return sorted(result, key=lambda x: x[2])
