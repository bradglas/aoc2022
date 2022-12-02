from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
LOSE = 0
DRAW = 3
WIN = 6
ROCK = 1
PAPER = 2
SISSORS = 3


def compute(s: str) -> int:

    score = 0
    lines = s.splitlines()
    for line in lines:
        points = 0
        opponent, mine = line.split(' ')

        match opponent:
            case 'A':  # rock
                match mine:
                    case 'X':
                        points = LOSE + SISSORS
                    case 'Y':
                        points = DRAW + ROCK
                    case 'Z':
                        points = WIN + PAPER

        match opponent:
            case 'B':  # paper
                match mine:
                    case 'X':
                        points = LOSE + ROCK
                    case 'Y':
                        points = DRAW + PAPER
                    case 'Z':
                        points = WIN + SISSORS

        match opponent:
            case 'C':  # sissors
                match mine:
                    case 'X':
                        points = LOSE + PAPER
                    case 'Y':
                        points = DRAW + SISSORS
                    case 'Z':
                        points = WIN + ROCK

        score += points

    return score


INPUT_S = '''\
A Y
B X
C Z
'''
EXPECTED = 12


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
