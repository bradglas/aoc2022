from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:

    elf_list = []
    tot_cal = 0

    numbers = support.parse_numbers_split(s)
    for n in numbers:
        pass

    lines = s.splitlines()
    for line in lines:

        if line.strip() == '':   # blank line start next elf
            elf_list.append(tot_cal)
            tot_cal = 0
        else:
            tot_cal += int(line)

    tot_cal = 0
    sorted_elf = sorted(elf_list, reverse=True)
    for elf in range(3):
        tot_cal += sorted_elf[elf]

    return tot_cal


INPUT_S = '''\

'''
EXPECTED = 1


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
