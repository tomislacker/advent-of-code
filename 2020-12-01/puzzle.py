"""
ModuleName
==========
"""
#!/usr/bin/env python
from __future__ import print_function


if __name__ == '__main__':
    input_path = 'input'
    with open(input_path, 'r') as infile:
        data = [
            int(line.strip())
            for line in infile.read().split()
            if line.strip()
        ]
    print(f'Reading {len(data)} entries')

    found_pairs = []
    for first_idx, value1 in enumerate(data):
        for second_idx, value2 in enumerate(data[(first_idx + 1):]):
            if (value1 + value2) == 2020:
                found_pairs.append((
                    value1,
                    value2,
                    first_idx,
                    second_idx,
                    (value1 * value2)
                ))

    print(f'Found pairs: {len(found_pairs)}')
    print(found_pairs)
# vim:expandtab:sts=4:sw=4:ts=4
