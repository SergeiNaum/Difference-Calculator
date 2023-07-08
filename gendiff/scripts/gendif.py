#!/usr/bin/env python
"""Difference Generator."""

from gendiff.gendif import generate_diff
from gendiff.cli import parse_args


def main():
    first_file, second_file, output_format = parse_args()
    print(generate_diff(first_file, second_file, output_format))


if __name__ == '__main__':
    main()
