#!/usr/bin/env python3
"""
Author : Emmanuel Gonzalez
Date   : 2020-03-19
Purpose: Transcribe DNA to RNA
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('r'),
                        help='Input file(s)')

    parser.add_argument('-o',
                        '--outdir',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='out')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Transcribe here"""

    args = get_args()
    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)
    f_cnt = 0
    s_cnt = 0
    for f in args.file:
        f_cnt += 1
        name = f.name
        out_file = os.path.join(args.outdir, os.path.basename(name))
        out_fh = open(out_file, 'wt')
        replace = 'T'
        for row in f:
            seqs = row.split()[:]
            trans = []
            for seq in seqs:
                s_cnt += 1
                for ch in seq:
                    if ch in replace:
                        trans.append('U')
                    else:
                        trans.append(ch)
                trans_seq = ''.join(trans)
            out_fh.write(trans_seq + '\n')

    if s_cnt == 1 and f_cnt > 1:
        print(
            f'Done, wrote {s_cnt} sequence in {f_cnt} files to directory "{args.outdir}".')
    elif s_cnt > 1 and f_cnt == 1:
        print(
            f'Done, wrote {s_cnt} sequences in {f_cnt} file to directory "{args.outdir}".')
    elif s_cnt > 1 and f_cnt > 1:
        print(
            f'Done, wrote {s_cnt} sequences in {f_cnt} files to directory "{args.outdir}".')
    else:
        print(
            f'Done, wrote {s_cnt} sequence in {f_cnt} file to directory "{args.outdir}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
