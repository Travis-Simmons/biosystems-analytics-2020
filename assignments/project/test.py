#!/usr/bin/env python3
"""
Author : emmanuelgonzalez
Date   : 2020-05-02
Purpose: Rock the Casbah
"""

import csv
import hashlib
import os
import random
import re
import string
from subprocess import getstatusoutput, getoutput
from random import shuffle
from Bio import SeqIO
import shutil

prg = './edit_gps.py'
input1 = './inputs/corrected_coordinates.csv'

# --------------------------------------------------
def random_filename():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput('{} {}'.format(prg, flag))
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_file():
    """fails on bad file"""

    bad = random_filename()
    rv, out = getstatusoutput('{} -c inputs/corrected_coordinates.csv {}'.format(prg, bad))
    assert rv > 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_missing_csv():
    """fails on missing keyword"""

    rv, out = getstatusoutput('{} {}'.format(prg, input1))
    assert rv > 0
    assert re.search('are required: -c/--csv', out)


# --------------------------------------------------
def test_01():
    run({
        'csv': '-c inputs/corrected_coordinates.csv',
        'dir': 'tif_imgs/',
        'edits': '5'
    })


# --------------------------------------------------
def run(args):
    """Run and test"""

    out_tmpl = 'Process complete, edited {edits} images. Outputs in "{out}".'
    run_tmpl = '{prg} -c {csv} -o {out_dir} {dir}'
    out_dir = random_filename()

    if os.path.isdir(out_dir):
        os.remove(out_dir)

    try:
        cmd = run_tmpl.format(prg=prg,
                              csv=input1,
                              out_dir=out_dir,
                              dir=args['dir'])

        rv, out = getstatusoutput(cmd)
        assert rv == 0
        assert out.split('\n')[-1] == out_tmpl.format(edits=args['edits'],
                                                      out=out_dir)


        file_cnt = len(os.listdir(out_dir))
        assert file_cnt  == int(args['edits'])

    finally:
        if os.path.isdir(out_dir):
            shutil. rmtree(out_dir)

# # --------------------------------------------------
# if __name__ == '__main__':
#     main()
