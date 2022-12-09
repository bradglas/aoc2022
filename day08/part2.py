from __future__ import annotations

import argparse
import os.path
from typing import Any

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    matrix: list[Any] = []
    max_scenic_score = 0

    for _, line in enumerate(s.splitlines()):
        row = []
        for col, n in enumerate(line):
            row.append(int(n))
        matrix.append(row)

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for R in range(num_rows):
        for C in range(num_cols):
            tree = matrix[R][C]
            # left
            lscore = 0
            for x in range(C - 1, -1, -1):
                lscore += 1
                if matrix[R][x] >= tree:
                    break

            # right
            rscore = 0
            for x in range(C + 1, num_rows):
                rscore += 1
                if matrix[R][x] >= tree:
                    break

            # up
            uscore = 0
            for x in range(R - 1, -1, -1):
                uscore += 1
                if matrix[x][C] >= tree:
                    break

            # down
            dscore = 0
            for x in range(R + 1, num_cols):
                dscore += 1
                if matrix[x][C] >= tree:
                    break

            scenic_score = lscore * rscore * uscore * dscore
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

    return max_scenic_score


INPUT_S = '''\
30373
25512
65332
33549
35390
'''
EXPECTED = 8


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
