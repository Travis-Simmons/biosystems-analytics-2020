#!/usr/bin/env python3
"""
Author : emmanuelgonzalez
Date   : 2020-03-12
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
from pprint import pprint

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA into proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq',
                        metavar='str',
                        help='DNA/RNA sequence')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        required=True,
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('w'),
                        default="out.txt")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    outfile = args.outfile.name
    aa = args.codons
    k = 3
    
    codon_amino = {}
    for line in args.codons:
        lines = line.split()
        for l in lines:
            seq = lines[0]
            aa = lines[1]
            codon_amino[seq] = aa 

    codon_list = []
    for codon in [args.seq[i:i + k] for i in range(0, len(args.seq) - k + 1)]:
        codon_list.append(codon.upper())
    codon_list = codon_list[::3]

    amino_list = []
    for c in codon_list:
        amino = codon_amino.get(c, '-')
        amino_list.append(amino)
        args.outfile.write(amino)
    
    print(f'Output written to "{outfile}".') 


# --------------------------------------------------
if __name__ == '__main__':
    main()
