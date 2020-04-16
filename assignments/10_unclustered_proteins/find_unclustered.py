#!/usr/bin/env python3
"""
Author : Emmanuel Gonzalez
Date   : 2020-04-15
Purpose: Find Unclustered Proteins
"""

import argparse
import re
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-c',
                        '--cdhit',
                        help='Output file from CD-HIT (clustered proteins)',
                        metavar='cdhit',
                        type=argparse.FileType('r'),
                        default=None,
                        required=True)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='outfile',
                        #type='str',
                        type=argparse.FileType('wt'),
                        default='unclustered.fa')

    parser.add_argument('-p',
                        '--proteins',
                        help='Proteins FASTA',
                        metavar='proteins',
                        type=argparse.FileType('r'),
                        default=None,
                        required=True)
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Find unclustered proteins and write to FASTA file"""

    args = get_args()
    protein_ids = set()

    for line in args.cdhit:

        if line[0] != '>':
            match = re.search(r'>(\d+)', line)

            if match is not None:
                iden = match.group(1)
                protein_ids.add(iden)

    num_seq, num_write = 0, 0
    for rec in SeqIO.parse(args.proteins, 'fasta'):
        prot_id = re.sub(r'\|.*', '', rec.id)
        num_seq += 1

        if prot_id not in protein_ids:
            num_write += 1
            SeqIO.write(rec, args.outfile, 'fasta')

    print(f'Wrote {num_write:,} of {num_seq:,} unclustered proteins to "{args.outfile.name}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
