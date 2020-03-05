#!/usr/bin/env python3
"""
Author : Emmanuel Gonzalez
Date   : 2020-02-28
Purpose: Calcualte the Hamming distance between two string of equal or different lengths.
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Hamming Distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file')

    parser.add_argument('-m',
                        '--min',
                        help='Minimum integer value of the Hamming distance',
                        metavar='int',
                        type=int,
                        default=0)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Find differences between two words or two DNA strands"""

    args = get_args()

    with open(args.file) as f:
        for line in f:
            line = line.strip()
            word1, word2 = line.split()

            if len(word1) == len(word2):
                diffs = 0
                for ch1, ch2 in zip(word1, word2):
                    if ch1 != ch2:
                        diffs += 1
                diffs
            else:
                len_diff = abs(len(word1) - len(word2))
                diffs = 0
                for ch1, ch2 in zip(word1, word2):
                    if ch1 != ch2:
                        diffs += 1
                diffs += len_diff

            if args.min != 0:
                if diffs >= args.min:
                    print(f'{diffs:8}:{word1:20}{word2:20}')
                else:
                    None
            else:
                print(f'{diffs:8}:{word1:20}{word2:20}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
