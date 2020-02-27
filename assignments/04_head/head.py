#!/usr/bin/env python3
"""
Author : Emmanuel Gonzalez
Date   : 2020-02-26
Purpose:
"""

import argparse
import os
import sys
import linecache


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="""
            This filter displays the first count lines or bytes of each of the specified files,
            or of the standard input if no files are specified. If count is omitted it defaults to 10.
            If more than a single file is specified, each file is preceded by a header consisting of the
            string ''==> XXX <=='' where ''XXX'' is the name of the file.
            """,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        # default=[sys.stdin],
                        # type=argparse.FileType('r'),
                        help='Input file')

    parser.add_argument('-n',
                        '--num',
                        help='Number of lines (default: 10)',
                        metavar='int',
                        #default=parser.error(f'--num "{args.num}" must be greater than 0'),
                        type=int,
                        #choices=range(0, 10),
                        default=10)

    args = parser.parse_args()
    if args.num and args.num >= 1:
        return args
    else:
        raise parser.error(f'--num "{args.num}" must be greater than 0')


# --------------------------------------------------
def main():
    """Extract lines"""

    args = get_args()
    with open(args.file) as f:
        count = 0
        lines_wanted = range(0, args.num)

        for line in f:
            line = line.strip()
            if count in lines_wanted:
                print(line)
            count += 1


# --------------------------------------------------
if __name__ == '__main__':
    main()
