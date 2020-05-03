#!/usr/bin/env python3
"""
Author : Emmanuel Gonzalez
Date   : 2020-04-09
Purpose: Update GPS coordiantes on TIF images in a given directory.
"""

import argparse
import os
import subprocess
import glob
import time
import pandas as pd

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dir',
                        metavar='dir',
                        type=str,
                        help='The directory containing TIF images')

    parser.add_argument('-c',
                        '--csv',
                        help='CSV file with updated coordinates',
                        metavar='FILE',
                        type=str,
                        required=True)

    parser.add_argument('-o',
                        '--outdir',
                        metavar='outdir',
                        type=str,
                        default='gpscorrect_out')

    args = parser.parse_args()

    if not os.path.isdir(args.dir):
        parser.error(f"No such file or directory: '{args.dir}'")

    return args


# --------------------------------------------------
def main():
    """Open CSV and update coordinates"""

    args = get_args()
    img_cnt = 0

    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)

    images = glob.glob(args.dir + "*.tif", recursive=True)

    df = pd.read_csv(args.csv, index_col='Filename', usecols=['Filename', 'Upper left', 'Lower right'])

    for i in images:
        filename = ''.join(os.path.splitext(os.path.basename(i)))

        if filename in df.index:
            img_cnt += 1
            start = time.time()

            u_l = df.loc[[str(filename)][0], ['Upper left'][0]]
            u_l_long, u_l_lat = u_l.split(',')
            l_r = df.loc[[str(filename)][0], ['Lower right'][0]]
            l_r_long, l_r_lat = l_r.split(',')
            print(f'>{img_cnt} {filename:5}')

            basename = os.path.splitext(os.path.basename(i))[0]
            outfile = args.outdir + '/' + basename + '_corrected.tif'
            cmd = (
                f'gdal_translate -of "GTiff" -co "COMPRESS=LZW" -a_ullr {u_l_long} {u_l_lat} {l_r_long} {l_r_lat} -a_srs EPSG:4326 {i} {outfile}')
            subprocess.call(cmd, shell=True)

            end = time.time()
            ind_time = end - start
            print(f'Done - Processing time: {ind_time}' + "\n")
        else:
            continue

    print(
        f'Process complete, edited {img_cnt} images. Outputs in "{args.outdir}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
