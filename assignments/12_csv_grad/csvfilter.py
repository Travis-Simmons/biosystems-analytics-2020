#!/usr/bin/env python3
"""
Author : Emmanuel Gonzalez
Date   : 2020-05-07
Purpose: Filter a delimited text file for some value
"""

import argparse
import sys
import csv
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='CSV filter',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        required=True,
                        default=None)

    parser.add_argument('-v',
                        '--val',
                        help='Value for filter',
                        metavar='val',
                        type=str,
                        required=True,
                        default=None)

    parser.add_argument('-c',
                        '--col',
                        help='Column for filter',
                        metavar='col',
                        type=str,
                        required=False,
                        default='')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='OUTFILE',
                        type=argparse.FileType('wt'),
                        default='out.csv')

    parser.add_argument('-d',
                        '--delimiter',
                        help='Input delimiter',
                        metavar='delim',
                        type=str,
                        default=',')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Filter and write CSV/TSV file here"""

    args = get_args()

    cnt_col, cnt_val = 0, 0

    if args.delimiter == ',':
        reader = csv.DictReader(args.file, delimiter=',')
    else:
        reader = csv.DictReader(args.file, delimiter='\t')

    if args.col:

        if args.col not in reader.fieldnames:
            options = ', '.join(reader.fieldnames)
            sys.stderr.write(
                f'--col "{args.col}" not a valid column!\nChoose from {options}\n')

    writer = csv.DictWriter(args.outfile, fieldnames=reader.fieldnames)
    writer.writeheader()

    for rec in reader:

        if args.col:

            column = rec[args.col]

            if re.search(args.val, column, re.IGNORECASE):
                cnt_col += 1
                writer.writerow(rec)

        else:

            if re.search(args.val, str(rec.values()), re.IGNORECASE):
                cnt_val += 1
                writer.writerow(rec)

    print(
        f'Done, wrote {cnt_col if args.col else cnt_val} to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
