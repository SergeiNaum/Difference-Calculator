"""Parser module"""
import json
import yaml


def parse(file_name, file_ex):
    if file_ex == '.json':
        with open(file_name) as file1:
            return json.load(file1)
    if file_ex in ('.yaml', '.yml'):
        with open(file_name) as file2:
            return yaml.safe_load(file2)

    raise ValueError('Unknown file format')
