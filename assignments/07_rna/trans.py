#!/usr/bin/env python3
"""
Author : Emmanuel Gonzalez
Date   : 2020-03-26
Purpose: Transcribe DNA into RNA.
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
                        help='A readable file',
                        type=argparse.FileType('r'),
                        nargs='+',
                        default=None)

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='out')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_dir = args.outdir

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    num_files, num_seqs = 0
    for fh in args.file:
        num_files += 1
        out_file = os.path.join(out_dir, os.path.basename(fh.name))
        out_fh = open(out_file, 'wt')

        for dna in fh:
            out_fh.write(dna.rstrip().replace('T', 'U') + '\n')

        out_fh.close()

    print(f'Done, wrote {num_seqs} in {num_files}')

    print('Done')


# --------------------------------------------------
if __name__ == '__main__':
    main()
