#!/usr/bin/env python3
"""
Author : Emmanuel Gonzalez
Date   : 2020-02-13
Purpose: Jump numbers to encode.
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

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text

    jumper = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0',
              '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}

    for char in text:
        #print(char, char in jumper)
        # if char in jumper:
        #   print(jumper[char])
        # else:
        #    print(char)

        #print(jumper[char] if char in jumper else char, end='')
        print(jumper.get(char, char), end = '')
    print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
