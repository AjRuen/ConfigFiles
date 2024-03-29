#!/usr/bin/env python3
"""Default template for my python files. Copy of Template by Tyler Westland"""

__author__ = "Aaron Ruen"

import argparse
import os
import sys


def parse_arguments(args=None) -> argparse.Namespace:
    """Returns the parsed arguments.
    Parameters
    ----------
    args: List of strings to be parsed by argparse.
        The default None results in argparse using the values passed into
        sys.args.
    """
    parser = argparse.ArgumentParser(
            description="A default template for python",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("input_file", help="Path to the input file.")
    parser.add_argument("-o", "--output_file", help="Path to the output file.",
            default="output")
    parser.add_argument("-q", "--quiet", help="Don't print out non-errors",
                        default=False, action="store_true")
    args = parser.parse_args(args=args)
    return args


def main(input_file:str, quiet:bool=False, output_file:str="output") -> None:
    """Main function.
    Parameters
    ----------
    input_file: str
        Path the input file.
    output_file: str
        Path to the output file. Default is 'output'
    quiet: bool
        Rather non-errors should be printed. Default is False
    Returns
    -------
    ???
        Something useful.
    Raises
    ------
    FileNotFoundError
        Means that the input file was not found.
    """
    # Error check if the file even exists
    if not os.path.isfile(input_file):
        raise FileNotFoundError("File not found: {}".format(input_file))

    return None


def cli_interface() -> None:
    """Get program arguments from command line and run main"""
    args = parse_arguments()
    try:
        main(**vars(args))
        sys.exit(0)
    except FileNotFoundError as exp:
        print(exp, file=sys.stderr)
        sys.exit(1)


# Execute only if this file is being run as the entry file.
if __name__ == "__main__":
    cli_interface()