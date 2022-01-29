from __future__ import annotations
import json

import argparse
from collections import Counter
import os.path
from typing import NamedTuple
from itertools import permutations


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
AXIS_ROTATIONS = [
    p for t in [
        (1, 2, 3),
        (1, 2, -3),
        (1, -2, 3),
        (1, -2, -3),
        (-1, 2, 3),
        (-1, 2, -3),
        (-1, -2, 3),
        (-1, -2, -3),
    ]
    for p in permutations(t)
]


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


def scanner_trasform(cls: Scanner) -> dict:

    tran_coords = {}
    for idx, axis in enumerate(AXIS_ROTATIONS):
        tran_coords[axis] = []
        for coord in cls.points:
            tran_coords[axis].append(point_transform(coord, axis))

    return tran_coords


def point_transform(pt: tuple, axis: tuple) -> tuple:
    res = [0, 0, 0]
    for i in range(3):
        res[abs(axis[i]) - 1] = pt[i]
        if axis[i] < 0:
            res[abs(axis[i]) - 1] *= -1

    return tuple(res)


class AxisInfo(NamedTuple):
    axis: int
    sign: int
    diff: int


def compute(s: str) -> ...:
    scanners = [Scanner.from_str(part) for part in s.split('\n\n')]
    scanner_positions = {0: (0, 0, 0)}
    all_points = set(scanners.pop(0).points)


    while scanners:
        offset, scanner, new_points = find_orientation(all_points, scanners)

        scanner_positions[scanner.sid] = tuple(offset)

        for p in new_points:
            all_points.add(p)
        scanners.remove(scanner)

    max_distace = 0
    for scanner, offset in scanner_positions.items():
        for scanner2, offset2 in scanner_positions.items():
            distance = sum([abs(a - b) for a, b in zip(offset, offset2)])
            print([abs(a-b) for a, b in zip(offset, offset2)])

            if distance > max_distace:
                max_distace = distance
                # print(f'Scanner {scanner} and Scanner {scanner2} with offsets {offset} and {offset2} and distance {distance}')


    print(f'Part One is: {len(all_points)}')
    print(f'Part Two is: {max_distace}')


def find_orientation(known: set, scanners) -> [list, Scanner, list[tuple]]:
    for scanner in scanners:
        for axis, points in scanner_trasform(scanner).items():
            distances = Counter()
            for p1 in known:
                for p2 in points:
                    distances[str([a - b for a, b in zip(p1, p2)])] += 1

            offset = distances.most_common(1)[0]
            if offset[1] >= 12:
                offset = json.loads(offset[0])
                match = [(x + offset[0], y + offset[1], z + offset[2]) for x, y, z in points]

                return offset, scanner, match


def most_common(lst):
    return max(set(lst), key=lst.count)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        compute(f.read())

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
