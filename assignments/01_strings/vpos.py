#!/usr/bin/env python3
"""
Author : emmanuelgonzalez
Date   : 2020-01-29
Purpose: Accepts exactly two positions and determines if vowel is present in the word. 
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find position of vowel in string',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('vowel',
                        metavar='vowel',
                        help='A vowel to look for',
                        choices=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

    parser.add_argument('text',
                        metavar='text',
                        help='The text to search')
    """
    parser.add_argument('-a',
                        '--arg',
                        help='A named string argument',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-i',
                        '--int',
                        help='A named integer argument',
                        metavar='int',
                        type=int,
                        default=0)

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None)

    parser.add_argument('-o',
                        '--on',
                        help='A boolean flag',
                        action='store_true')
    """
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    vowel = args.vowel
    text = args.text 
    vowels = "aeiou"
    """
    for char in text:
        if char in vowels:
            position = text.find(vowel)
            print(f'Found "{vowel}" in "{text}" at index {position}.')
        else:
            print(f'"{vowel}" is not found in "{text}".')
    
    """
    if vowel.casefold() in text.casefold() and vowels: 
        index = text.find(vowel)
        print(f'Found "{vowel}" in "{text}" at index {index}.')
    else:
        print(f'"{vowel}" is not found in "{text}".')

# --------------------------------------------------
if __name__ == '__main__':
    main()
