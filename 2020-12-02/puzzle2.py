#!/usr/bin/env python
"""
2020-12-02 puzzle 2
===================
"""
from __future__ import print_function
import re


def get_character_count(char, search_string):
    count = 0
    for i in search_string:
        if i == char:
            count += 1
    return count


if __name__ == '__main__':
    # Define the pattern to match for within each line of the file
    line_pattern = re.compile(r'^(?P<first_char>\d+)-(?P<second_char>\d+)\s+(?P<char>[a-zA-Z])\s*:\s+(?P<pwd>.*)$')  # noqa

    # Create a buffer of the lines read
    samples = []

    # Read in the file
    with open('input', 'r') as infile:
        for line in [this_line.strip() for this_line in infile.read().split('\n')]:  # noqa
            if not line:
                # Blank line, skip
                continue
            match = line_pattern.match(line.strip())

            if not match:
                # wtf?
                print(f'Failed match: {line.strip()}')
                continue

            samples.append(match.groupdict())

    print(f'Found {len(samples)} samples')

    # Create a buffer for valid passwords from the samples
    valid = []

    # Iterate through the samples to find valid passwords
    for spec in samples:
        try:
            first_char_met = (
                spec['pwd'][int(spec['first_char']) - 1] == spec['char']
            )
        except IndexError:
            first_char_met = False

        try:
            second_char_met = (
                spec['pwd'][int(spec['second_char']) - 1] == spec['char']
            )
        except IndexError:
            second_char_met = False

        print(' '.join([
            f'spec={spec}',
            f'first_char_met={first_char_met}',
            f'second_char_met={second_char_met}',
        ]))
        if (
            (first_char_met and not second_char_met)
            or (not first_char_met and second_char_met)
        ):
            valid.append(spec)

    print(f'Found {len(valid)} valid passwords')

# vim:expandtab:sts=4:sw=4:ts=4
