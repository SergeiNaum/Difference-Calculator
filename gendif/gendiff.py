"""Generate Diff - main module"""

import json


def generate_diff(file_path1: str,
                  file_path2: str):
    result = []
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    dictionary1 = dict(file1)
    dictionary2 = dict(file2)
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

    for line in sorted(result, key=lambda x: x[2]):
        print(line)
    # return sorted(result, key=lambda x: x[2])
