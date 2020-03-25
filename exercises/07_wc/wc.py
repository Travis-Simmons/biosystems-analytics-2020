#!/usr/bin/env python3
"""
Author : emmanuelgonzalez
Date   : 2020-03-02
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*', 
                        default=[sys.stdin],
                        type=argparse.FileType('r'),
                        help='Input file(s)')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file_arg = args.file
    
    total_lines, total_chars, total_words = 0, 0, 0
    for fh in args.file:
        lines, chars, words = 0, 0, 0
        for line in fh:
            lines += 1
            chars += len(line)
            words += len(line.split())
        total_lines += lines
        total_chars += chars
        total_words += words

        print(f'{lines:8}{words:8}{chars:8} {fh.name}')

    if len(args.file) > 1:
        print(f'{total_lines:8}{total_words:8}{total_chars:8} total')

# --------------------------------------------------
if __name__ == '__main__':
    main()
