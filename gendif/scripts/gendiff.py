#!/usr/bin/env python
"""Difference Generator."""

from gendif import generate_diff
from gendif.cli import parsing_args


def main():
    first_file, second_file, output_format = parsing_args()
    for el in generate_diff(first_file, second_file):
        print(el)
    # print(generate_diff(first_file, second_file))


if __name__ == '__main__':
    main()
