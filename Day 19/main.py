from __future__ import annotations

import argparse
# import collections
import os.path
from typing import NamedTuple


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test.txt')


class Scanner(NamedTuple):
    sid: int
    points: list[tuple[int, int, int]]

    @classmethod
    def from_str(cls, s: str) -> Scanner:
        lines = s.splitlines()
        _, _, sid_s, _ = lines[0].split()
        points = []
        for line in lines[1:]:
            x, y, z = line.split(',')
            points.append((int(x), int(y), int(z)))
        return cls(int(sid_s), points)


class AxisInfo(NamedTuple):
    axis: int
    sign: int
    diff: int


def compute(s: str) -> ...:
    scanners = [Scanner.from_str(part) for part in s.split('\n\n')]
    scanners_by_id = {scanner.sid: scanner for scanner in scanners}
    print(scanners_by_id)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        compute(f.read())

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
