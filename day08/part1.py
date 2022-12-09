from __future__ import annotations

import argparse
import os.path
from typing import Any

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

matrix: list[Any] = []
visable: list[Any] = []


def check_vis_LR(row: int, col: int, start: int, end: int) -> str:
    r = row
    c = col
    if visable[r][c] != 'y':
        for x in range(start, end):
            if matrix[r][c] <= matrix[r][x]:
                return 'n'

    return 'y'


def check_vis_TB(row: int, col: int, start: int, end: int) -> str:
    r = row
    c = col
    if visable[r][c] != 'y':
        for x in range(start, end):
            if matrix[r][c] <= matrix[x][c]:
                return 'n'

    return 'y'


def compute(s: str) -> int:
    visable_cnt = 0
    for _, line in enumerate(s.splitlines()):
        row = []
        vrow = []
        for col, n in enumerate(line):
            row.append(int(n))
            vrow.append('?')
        matrix.append(row)
        visable.append(vrow)

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # all the trees on edges are visable
    for col in range(num_cols):
        visable[0][col] = 'y'
        visable[num_rows - 1][col] = 'y'
    for i in range(num_rows):
        visable[i][0] = 'y'
        visable[i][num_cols - 1] = 'y'

    for R in range(1, num_rows - 1):
        for C in range(1, num_cols - 1):
            # from left
            visable[R][C] = check_vis_LR(R, C, 0, C)

            # from right
            visable[R][C] = check_vis_LR(R, C, C + 1, num_cols)

            # from top
            visable[R][C] = check_vis_TB(R, C, 0, R)
            # from bottom
            visable[R][C] = check_vis_TB(R, C, R + 1, num_rows)

    for i, _ in enumerate(visable):
        for col, vis in enumerate(visable[i]):
            if vis == 'y':
                visable_cnt += 1

    return visable_cnt


INPUT_S = '''\
30373
25512
65332
33549
35390
'''
EXPECTED = 21


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
