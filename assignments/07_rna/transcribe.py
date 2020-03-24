#!/usr/bin/env python3
"""
Author : emmanuelgonzalez
Date   : 2020-03-19
Purpose: Rock the Casbah
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
    """Make a jazz noise here"""

    args = get_args()
     
    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)
    f_cnt = 0
    for f in args.file: 
        f_cnt += 1
        name = f.name
        out_file = os.path.join(args.outdir, os.path.basename(name))
        #print(out_file)
        out_fh = open(out_file, 'wt')
        replace = 'T'
        s_cnt = 0
        for row in f:
            s_cnt += 1
            seq = str(row.split()[0])
            #print("Seq:", seq)
            trans = []
            for ch in seq:
                #print(ch)
                #trans = []
                if ch in replace:
                    trans.append('U')
                else:
                    trans.append(ch)
            trans_seq = ''.join(trans)
            #print(trans_seq)
            #print("trans:", trans) 
        out_fh.write(trans_seq)
    #print(f_cnt, s_cnt)
    plural = {'plural': 'sequences files', 'single': 'sequence file'}
    print(plural)

    #if s_cnt and f_cnt == 1:
    #    print(f'Done, wrote {s_cnt} sequence in {f_cnt} file to directory "{args.outdir}".') 
    #if s_cnt and f_cnt > 1 :
    #    print(f'Done, wrote {s_cnt} sequences in {f_cnt} files to directory "{args.outdir}".')

        #if f_cnt > 1:
        #    print(f'Done, wrote {s_cnt} sequences in {f_cnt} files to directory "{args.outdir}".')
# --------------------------------------------------
if __name__ == '__main__':
    main()
