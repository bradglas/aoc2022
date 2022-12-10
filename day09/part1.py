from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:

    head: tuple[int, ...] = (0, 0)
    tail = head
    visited = set()
    visited.add(tail)
    lines = s.splitlines()

    for line in lines:
        direction, count = line.split()
        if direction == 'R':
            d = (0, 1)
        elif direction == 'L':
            d = (0, -1)
        elif direction == 'U':
            d = (1, 0)
        elif direction == 'D':
            d = (-1, 0)
        else:
            raise AssertionError(f'unexpected input - direction: {direction}')

        for x in range(int(count)):
            head = tuple(p+q for p, q in zip(head, d))
            # check adjent in same row, col
            # same col or row ?
            if abs(head[0] - tail[0]) > 1 or \
                    abs(head[1] - tail[1]) > 1:  # move tail
                if head[0] == tail[0] or head[1] == tail[1]:  # same row or col
                    tail = tuple(p+q for p, q in zip(tail, d))
                else:  # move diagonally
                    tail = tuple(p-q for p, q in zip(head, d))

            visited.add(tail)

    return len(visited)


INPUT_S = '''\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
'''
EXPECTED = 13


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
