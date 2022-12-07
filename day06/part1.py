from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def hasDups(a: str) -> bool:
    k = {}
    for j in a:
        if j in k:
            return True
            k[j] += 1
        else:
            k[j] = 1
    return False


def compute(s: str) -> int:

    lines = s.splitlines()
    for line in lines:
        startOfPacket = 0
        for i in range(0, len(line)):
            packet = line[i:i+4]
            if hasDups(packet):
                pass
            else:
                startOfPacket = i + 4
                break

    return startOfPacket


INPUT_S = '''\
mjqjpqmgbljsphdztnvjfqwrcgsmlb
'''
EXPECTED = 7


@ pytest.mark.parametrize(
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
