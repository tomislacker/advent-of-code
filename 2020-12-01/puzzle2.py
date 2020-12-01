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

    found_sets = []
    for first_idx, value1 in enumerate(data):
        for second_idx, value2 in enumerate(data[(first_idx + 1):]):
            for third_idx, value3 in enumerate(data[(second_idx + 1):]):
                if (value1 + value2 + value3) == 2020:
                    found_sets.append((
                        value1,
                        value2,
                        value3,
                        first_idx,
                        second_idx,
                        third_idx,
                        (value1 * value2 * value3)
                    ))

    print(f'Found pairs: {len(found_sets)}')
    print(found_sets)
# vim:expandtab:sts=4:sw=4:ts=4
