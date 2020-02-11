#!/usr/bin/env python3
"""
Author : Emmanuel Gonzalez
Date   : 2020-02-11
Purpose: Print out favorite things. 
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='My Favorite Things',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('favorites',
                        metavar='str',
                        nargs='+',
                        help='Some things')
    
    parser.add_argument('-s',
                        '--sep',
                        #action='store_false',
                        help='A separator',
                        default=', ')
    
    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    favs = args.favorites
    sep = args.sep
    
    if len(favs) == 1:
        favs = str(favs[0])
        print('{}'.format(favs))
        print("This is one of my favorite things.")
    
    else:
        str1 = sep.join(favs)
        print(str1)
        print("These are a few of my favorite things.")

# --------------------------------------------------
if __name__ == '__main__':
    main()
