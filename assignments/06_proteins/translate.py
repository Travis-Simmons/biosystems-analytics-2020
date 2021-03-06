#!/usr/bin/env python3
"""
Author : Emmanuel Gonzalez
Date   : 2020-03-12
Purpose: Translate DNA/RNA into proteins
"""

import argparse

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
                        type=argparse.FileType('wt'),
                        default="out.txt")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Translate DNA/RNA > protein here"""

    args = get_args()
    k = 3
    
    codon_amino = {}
    for row in args.codons:
        column = row.split()
        seq = column[0]
        amino_acid = column[1]
        codon_amino[seq] = amino_acid

    codon_list = []
    for codon in [args.seq[i:i + k] for i in range(0, len(args.seq) - k + 1, k)]:
        codon_list.append(codon.upper())

    for codon in codon_list:
        amino = codon_amino.get(codon, '-')
        args.outfile.write(amino)

    print(f'Output written to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
