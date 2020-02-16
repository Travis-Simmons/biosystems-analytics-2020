#!/usr/bin/env python3
"""
Author : emmanuelgonzalez
Date   : 2020-02-16
Purpose: Seven Days of the Week
"""

import argparse

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='What to do on each day',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('days',
                        metavar='str',
                        nargs='+',
                        help='Days of the week')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Check list for days and return string"""

    args = get_args()
    days = args.days

    day_do = {'Monday': 'On Mondays I never go to work', 'Tuesday': 'On Tuesdays I stay at home', 'Wednesday': 'On Wednesdays I never feel inclined',
              'Thursday': 'On Thursdays, it\'s a holiday', 'Friday': 'And Fridays I detest', 'Saturday': 'Oh, it\'s much too late on a Saturday', 'Sunday': 'And Sunday is the day of rest'}

    for day in days:
        null = f'Can\'t find "{day}"'
        print(day_do.get(day, null))


# --------------------------------------------------
if __name__ == '__main__':
    main()
