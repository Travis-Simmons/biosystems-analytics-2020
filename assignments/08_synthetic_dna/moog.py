#!/usr/bin/env python3
"""
Author : emmanuelgonzalez
Date   : 2020-04-01
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import random
import Bio


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o',
                        '--outfile',
                        help='The output file',
                        metavar='str',
                        type=argparse.FileType('wt'),
                        default='out.fa')

    parser.add_argument('-t',
                        '--seqtype',
                        help='The sequence type',
                        metavar='str',
                        type=str,
                        choices=['dna', 'rna'],
                        default='dna')

    parser.add_argument('-n',
                        '--numseqs',
                        help='The number of sequences to generate',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument('-m',
                        '--minlen',
                        help='The minimum length for any sequence',
                        metavar='int',
                        type=int,
                        default=50)

    parser.add_argument('-x',
                        '--maxlen',
                        help='The maximum length for any sequence',
                        metavar='int',
                        type=int,
                        default=75)

    parser.add_argument('-p',
                        '--pctgc',
                        help='The average percentage of GC content for a \
                            sequence',
                        metavar='float',
                        type=float,
                        default=0.5)

    parser.add_argument('-s',
                        '--seed',
                        help='An integer value to use for the random seed',
                        metavar='int',
                        type=int,
                        default=None)


    args = parser.parse_args()

    if not 0 < args.pctgc < 1:
        parser.error(f'--pctgc "{args.pctgc}" must be between 0 and 1')

    return args

def create_pool(pctgc, max_len, seq_type):
    t_or_u = 'T' if seq_type == 'dna' else 'U'
    num_gc = int((pctgc / 2) * max_len)
    num_at = int(((1 - pctgc) / 2) * max_len)

    pool = 'A' * num_at + 'C' * num_gc + 'G' * num_gc + t_or_u * num_at
    for _ in range(max_len - len(pool)):
        pool += random.choice(pool)
    return ''.join(sorted(pool))

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)
    
    seqs = 0
    for _ in range(args.numseqs):
        seqs += 1
        seq_len = random.randint(args.minlen, args.maxlen)
        seq = random.sample(pool, seq_len)
        args.outfile.write(f'>{seqs}' + "\n" + ''.join(seq) + "\n")

    print(f'Done, wrote {args.numseqs} {args.seqtype.upper()} {"sequence" if args.numseqs == 1 else "sequences"} to "{args.outfile.name}".')



# --------------------------------------------------
if __name__ == '__main__':
    main()
