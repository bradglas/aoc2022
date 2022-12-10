from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:

    knot: list[tuple[int, ...]] = []
    visited = set()
    NUM_KNOTS = 10
    lines = s.splitlines()

    # init knots
    for i in range(NUM_KNOTS):
        knot.append((0, 0))

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
            knot[0] = tuple(p+q for p, q in zip(knot[0], d))
            prev = knot[0]
            for i in range(1, NUM_KNOTS):
                # check adjent in same row, col
                # same col or row ?
                hr, hc = prev
                tr, tc = knot[i]

                if abs(hr - tr) == 2 and abs(hc - tc) == 2:
                    knot[i] = ((hr + tr) // 2, (hc + tc) // 2)
                elif abs(hr - tr) == 2:
                    knot[i] = ((hr + tr) // 2, hc)
                elif abs(hc - tc) == 2:
                    knot[i] = (hr, (hc + tc) // 2)

                prev = knot[i]

            visited.add(knot[9])

    return len(visited)


INPUT_S = '''\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
'''
EXPECTED = 36


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
