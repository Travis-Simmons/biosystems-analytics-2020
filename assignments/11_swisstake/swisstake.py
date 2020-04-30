#!/usr/bin/env python3
"""
Author : Emmanuel Gonzalez
Date   : 2020-04-29
Purpose: Parse SwissProt records
"""

import argparse
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter SwissProt file for keywords, taxa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='SwissProt file')

    parser.add_argument('-k',
                        '--keyword',
                        help='Keyword to take',
                        metavar='keyword',
                        type=str,
                        required=True,
                        default=None)

    parser.add_argument('-s',
                        '--skiptaxa',
                        nargs='+',
                        help='Taxa to skip',
                        metavar='taxa',
                        type=str,
                        default=' ')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.fa')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    keyword_args = set(args.keyword.split('""'))
    skip = set(map(str.lower, (args.skiptaxa)))

    skip_cnt, take_cnt = 0, 0

    for rec in SeqIO.parse(args.file, "swiss"):
        taxa = set(map(str.lower, (rec.annotations.get('taxonomy'))))
        key = set(map(str.lower, (rec.annotations.get('keywords'))))

        if skip.intersection(taxa):
            skip_cnt += 1

        else:
            if keyword_args.intersection(key):
                SeqIO.write(rec, args.outfile, 'fasta')
                take_cnt += 1
            else:
                skip_cnt += 1

    print(
        f'Done, skipped {skip_cnt} and took {take_cnt}. See output in "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
