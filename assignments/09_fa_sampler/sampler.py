#!/usr/bin/env python3
"""
Author : Emmanuel Gonzalez
Date   : 2020-04-08
Purpose: Probabilistically sample one or more input FASTA files
        into an output directory.
"""

import argparse
import os
import random
from Bio import SeqIO

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Probabalistically subset FASTA files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('r'),
                        help='Input FASTA file(s)')

    parser.add_argument('-p',
                        '--pct',
                        help='Percent of reads',
                        metavar='reads',
                        type=float,
                        default=.1)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed value',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='OUTDIR',
                        type=str,
                        default='out')

    args = parser.parse_args()

    if not 0 <= args.pct < 1:
        parser.error(f'--pct "{args.pct}" must be between 0 and 1')

    return args


# --------------------------------------------------
def main():
    """ Sample here """
    args = get_args()
    random.seed(args.seed)

    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)

    cnt = 0
    seq_cnt = 0
    for fh in args.file:
        cnt += 1
        basename = os.path.basename(fh.name)
        out_file = os.path.join(args.outdir, basename)
        print(f'{cnt:3}: {basename}')

        out_fh = open(out_file, 'w')
        for rec in SeqIO.parse(fh, 'fasta'):
            if random.random() <= args.pct:
                seq_cnt += 1
                SeqIO.write(rec, out_fh, 'fasta')
        out_fh.close()

    print(f'Wrote {seq_cnt:,} sequences from {cnt} {"file" if cnt == 1 else "files"} to directory "{args.outdir}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
