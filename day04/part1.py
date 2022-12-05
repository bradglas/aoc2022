from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:

    total = 0

    lines = s.splitlines()
    for line in lines:
        elf1_list: list[int] = []
        elf2_list: list[int] = []

        elf1, elf2 = line.split(',')
        a, b = elf1.split('-')
        c, d = int(a), int(b)
        elf1_list.extend(range(c, d + 1))
        a, b = elf2.split('-')
        c, d = int(a), int(b)
        elf2_list.extend(range(c, d + 1))

        contains = all(elem in elf1_list for elem in elf2_list)
        if contains:
            total += 1
        else:
            contains = all(elem in elf2_list for elem in elf1_list)
            if contains:
                total += 1

    return total


INPUT_S = '''\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''
EXPECTED = 2


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
