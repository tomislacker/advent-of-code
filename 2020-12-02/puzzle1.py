#!/usr/bin/env python
"""
2020-12-02 puzzle 1
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
    line_pattern = re.compile(r'^(?P<min_count>\d+)-(?P<max_count>\d+)\s+(?P<char>[a-zA-Z])\s*:\s+(?P<pwd>.*)$')  # noqa

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
        char_count = get_character_count(
            spec['char'],
            spec['pwd'])
        if char_count >= int(spec['min_count']) and char_count <= int(spec['max_count']):  # noqa
            valid.append(spec)

    print(f'Found {len(valid)} valid passwords')

# vim:expandtab:sts=4:sw=4:ts=4
