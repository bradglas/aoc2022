from __future__ import annotations

import argparse
import os.path
from collections import deque
from typing import Any

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> str:
    stack: list[Any] = []

    top_crates: list[str] = []
    stacks_buildt = False
    for i in range(9):
        stack.append(deque())

    lines = s.splitlines()
    for line in lines:
        if not stacks_buildt:
            if line.strip() == '':
                stacks_buildt = True
                continue
            for i in range(0, len(line)):
                if line[i] == '[':
                    stack[i//4].append(line[i + 1])
        else:
            # move instructions start
            move, from_c, to_c = (int(i) for i in line.split() if i.isdigit())
            for i in range(move):
                crate = stack[from_c - 1].popleft()
                stack[to_c - 1].appendleft(crate)

    for i in range(9):
        try:
            top_crates.append(stack[i].popleft())
        except IndexError:
            continue

    return ''.join(top_crates)


INPUT_S = '''\
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''
EXPECTED = 'CMZ'


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
