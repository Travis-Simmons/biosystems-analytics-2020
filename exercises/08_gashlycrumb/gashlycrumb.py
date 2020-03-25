#!/usr/bin/env python3
"""
Author : Emmanuel Gonzalez
Date   : 2020-03-03
Purpose: Gashlycrumb
"""

import argparse
import os
import sys
from pprint import pprint


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letters',
                        metavar='letters',
                        nargs='+',
                        type=str,
                        help='Letters to lookup')

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    let_arg = args.letters

    gash_dict = {}

    for line in args.file:
        line = line.strip()
        key = line[0]
        gash_dict[key] = line

    for l in let_arg:
        l = l.upper()
        null = f'I do not know "{l}".'
        print(gash_dict.get(l, null))


# --------------------------------------------------
if __name__ == '__main__':
    main()
