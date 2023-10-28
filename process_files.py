#!/usr/bin/env python3

import argparse
from collections import deque
from io import TextIOWrapper
from collections.abc import Generator
from typing import (
    Optional,
    Deque,
    NamedTuple,
)


class Line(NamedTuple):
    text: str
    cnt: int


def get_line(filename: str) -> Generator[Line, None, None]:
    fp: TextIOWrapper
    curr_text: str
    next_text: str
    count: int

    with open(filename, 'r') as fp:
        try:
            curr_text = next(fp).rstrip('\n')
            count = 1
        except StopIteration:
            return

        for next_text in fp:
            next_text = next_text.rstrip('\n')
            if next_text != curr_text:
                yield Line(curr_text, count)
                curr_text = next_text
                count = 0
            count += 1
        if count > 0:
            yield Line(curr_text, count)


def write_line(fp: TextIOWrapper, line: Line) -> None:
    for _ in range(line.cnt):
        fp.write(f'{line.text}\n')


def append_line(pipe: Deque[Line], lines: Generator[Line, None, None]) -> None:
    try:
        pipe.append(next(lines))
    except StopIteration:
        pass


def process_files(file1: str, file2: str, file1_out: Optional[str] = None,
                  file2_out: Optional[str] = None) -> None:

    lines1: Generator[Line, None, None]
    lines2: Generator[Line, None, None]
    pipe1: Deque[Line]
    pipe2: Deque[Line]
    line1: Line
    line2: Line

    if file1_out is None:
        file1_out = file1 + '.out'
    if file2_out is None:
        file2_out = file2 + '.out'

    lines1 = get_line(file1)
    lines2 = get_line(file2)
    pipe1 = deque()
    pipe2 = deque()

    with open(file1_out, 'w') as fp1, open(file2_out, 'w') as fp2:
        for _ in range(2):
            append_line(pipe1, lines1)
            append_line(pipe2, lines2)

        if len(pipe1) == 2:
            if pipe1[0].text < pipe1[1].text:
                cmp = lambda a, b: a < b
            else:
                cmp = lambda a, b: a > b
        elif len(pipe2) == 2:
            if pipe2[0].text < pipe2[1].text:
                cmp = lambda a, b: a < b
            else:
                cmp = lambda a, b: a > b
        elif len(pipe1) == len(pipe2) == 1:
            line1 = pipe1.popleft()
            line2 = pipe2.popleft()
            if line1.text != line2.text:
                write_line(fp1, line1)
                write_line(fp2, line2)

        while pipe1 and pipe2:
            if cmp(pipe1[0].text, pipe2[0].text):
                write_line(fp1, pipe1.popleft())
                append_line(pipe1, lines1)
            elif pipe1[0].text == pipe2[0].text:
                pipe1.popleft()
                append_line(pipe1, lines1)
                pipe2.popleft()
                append_line(pipe2, lines2)
            else:
                write_line(fp2, pipe2.popleft())
                append_line(pipe2, lines2)

        while pipe1:
            write_line(fp1, pipe1.popleft())
        while pipe2:
            write_line(fp2, pipe2.popleft())

        for line1 in lines1:
            write_line(fp1, line1)
        for line2 in lines2:
            write_line(fp2, line2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file1', metavar='FILE1', help='first file')
    parser.add_argument('file2', metavar='FILE2', help='second file')
    parser.add_argument(
        '--file1_out', metavar='FILE1_OUT', default=None,
        help='output for the first file (default: FILE1 + ".out")')
    parser.add_argument(
        '--file2_out', metavar='FILE2_OUT', default=None,
        help='output for the second file (default: FILE2 + ".out")')
    args = parser.parse_args()

    process_files(**args.__dict__)
