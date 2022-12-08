from __future__ import annotations

import argparse
import os.path
from collections import deque

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    stack: deque[str] = deque()
    size = {}
    size['/'] = 0
    total = 0
    curDir = ''
    lines = s.splitlines()
    for line in lines:
        a = line.split()
        if line[0] == '$':  # command
            if a[1] == 'cd':
                if a[2] == '..':
                    prevDir = stack.popleft()
                    curDir = stack[0]
                    size[curDir] += size[prevDir]
                else:
                    curDir += a[2]
                    stack.appendleft(curDir)

        elif a[0] == 'dir':
            size[curDir + a[1]] = 0
        else:
            size[curDir] += int(a[0])

    while stack:
        prevDir = stack.popleft()
        if prevDir != '/':
            curDir = stack[0]
            size[curDir] += size[prevDir]

    for k in size:
        if size[k] <= 100000:
            total += size[k]

    return total


INPUT_S = '''\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
'''
EXPECTED = 95437


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
