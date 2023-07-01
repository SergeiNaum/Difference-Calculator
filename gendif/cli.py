"""Parser module - parsing args from user command line"""

import argparse


def parsing_args():
    """Parsing args from user command line"""
    # Create an arguments parser object
    parser = argparse.ArgumentParser(description='Compares two\
                configuration files and shows a difference.')

    parser.add_argument('first_file')
    parser.add_argument('second_file')

    args = parser.parse_args(['-h'])

    return args


