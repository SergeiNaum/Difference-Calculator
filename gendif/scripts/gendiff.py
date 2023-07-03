#!/usr/bin/env python
"""Difference Generator."""

from gendif import generate_diff
from gendif.cli import parsing_args


def main():
    first_file, second_file, output_format = parsing_args()
    print(generate_diff(first_file, second_file, output_format))


if __name__ == '__main__':
    main()
