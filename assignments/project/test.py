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

prg = './edit_gps.py'
input1 = './inputs/corrected_coordinates.csv'

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
    rv, out = getstatusoutput('{} -k foo {}'.format(prg, bad))
    assert rv > 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_missing_csv():
    """fails on missing keyword"""

    rv, out = getstatusoutput('{} {}'.format(prg, input1))
    assert rv > 0
    assert re.search('are required: -c/--csv', out)


# --------------------------------------------------
if __name__ == '__main__':
    main()
