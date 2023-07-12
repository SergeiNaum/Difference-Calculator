#!/usr/bin/env python
"""Difference Generator."""

from gendiff.gendif import generate_diff
from gendiff.cli import parse_args


def main():
    args = parse_args()
    first_file = args.first_file
    second_file = args.second_file
    output_format = args.format
    print(generate_diff(first_file, second_file, output_format))


if __name__ == '__main__':
    main()
