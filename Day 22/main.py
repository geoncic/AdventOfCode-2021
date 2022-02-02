from __future__ import annotations

from typing import NamedTuple

import argparse
import os.path
import numpy as np

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
ACTIVE_AREA = (-50, 50)

def day_twentytwo(data):
    # p1_sol = part_one(data)
    part_two(data)

def part_one(data):
    on_set = set()
    for line in data:
        inst = line[0]
        if check_instruction(line[1]):
            cubes = cube_list(line[1])
        for cube in cubes:
            flip_cube(inst, cube, on_set)
    return len(on_set)

def part_two(data):
    cubes: list[Cube] = []
    reboots: list[Reboot] = []
    status = 0

    for line in data:
        if line[0] == 'off':
            status = -1
        else:
            status = 1
        reboots.append(Reboot.parse(status, line[1]))


    # reboots = [Reboot.parse(line[0], line[1]) for line in data]

    # test1 = ((0, 5), (0, 5), (0, 5))
    # test2 = ((2, 7), (2, 7), (2, 7))
    # ints = get_overlap(test1, test2)
    # print(ints)

    for curr_cube in reboots:
        overlap: list[Cube] = []


        for cube in cubes:
            sign = curr_cube[0] * cube[0]

            if curr_cube[0] == cube[0]:
                sign = -1*curr_cube[0]

            elif curr_cube[0] == 1 and cube[0] == -1:
                sign = 1

            c1 = ((curr_cube[1].x0, curr_cube[1].x1), (curr_cube[1].y0, curr_cube[1].y1), (curr_cube[1].z0, curr_cube[1].z1))
            c2 = ((cube[1].x0, cube[1].x1), (cube[1].y0, cube[1].y1), (cube[1].z0, cube[1].z1))


            if Cube.intersects(curr_cube[1], cube[1]):
                inter = get_overlap(c1, c2)
                overlap.append(Reboot.parse(sign, inter))

        for intersection in overlap:
            cubes.append(intersection)
            # print(intersection)

        if curr_cube[0] == 1:
            cubes.append(curr_cube)

    res = 0

    for cube in cubes:
        # print(cube)


        res += abs(cube[1].size) * cube.status


    print(cubes[-2])
    print(cubes[-2][1].size)
    print(res)
    return res



def get_overlap(c1: tuple[tuple], c2: tuple[tuple]) -> tuple[tuple]:
    if any(r1[0] > r2[1] or r2[0] > r1[1] for r1, r2 in zip(c1, c2)):
        return None

    return tuple([(max(r1[0], r2[0]), min(r1[1], r2[1])) for r1, r2 in zip(c1, c2)])


class Cube(NamedTuple):
    x0: int
    x1: int
    y0: int
    y1: int
    z0: int
    z1: int

    @property
    def size(self) -> int:
        return (
            abs(self.x1 - self.x0+1) *
            abs(self.y1 - self.y0+1) *
            abs(self.z1 - self.z0+1)
        )

    def intersects(self, other: Cube) -> bool:
        return (
            self.x0 < other.x1 and
            self.x1 > other.x0 and
            self.y0 < other.y1 and
            self.y1 > other.y0 and
            self.z0 < other.z1 and
            self.z1 > other.z0
        )


    @classmethod
    def parse(cls, x0: int, x1: int, y0: int, y1: int, z0: int, z1: int) -> Cube:
        return cls(
            x0, x1,
            y0, y1,
            z0, z1,
        )


class Reboot(NamedTuple):
    status: int
    cube: Cube

    @classmethod
    def parse(cls, s: int, inst: tuple[tuple]) -> Reboot:
        # status = -1 if s == 'off' else 1
        x0, x1 = inst[0][0], inst[0][1]
        y0, y1 = inst[1][0], inst[1][1]
        z0, z1 = inst[2][0], inst[2][1]

        return cls(s, Cube.parse(x0, x1, y0, y1, z0, z1))

class Overlap(NamedTuple):
    modifier: int
    cube: Cube

    @classmethod
    def parse(cls, m: int, inst: tuple[tuple]) -> Reboot:
        modifier = m
        x0, x1 = inst[0][0], inst[0][1]
        y0, y1 = inst[1][0], inst[1][1]
        z0, z1 = inst[2][0], inst[2][1]

        return cls(modifier, Cube.parse(x0, x1, y0, y1, z0, z1))



def create_array(data):
    xmin, xmax, ymin, ymax, zmin, zmax = 0, 0, 0, 0, 0, 0

    for line in data:
        if int(line[1][0][0]) < xmin:
            xmin = int(line[1][0][0])
        if int(line[1][0][1]) > xmax:
            xmax = int(line[1][0][1])
        if int(line[1][1][0]) < ymin:
            ymin = int(line[1][1][0])
        if int(line[1][1][1]) > ymax:
            ymax = int(line[1][1][1])
        if int(line[1][2][0]) < zmin:
            zmin = int(line[1][2][0])
        if int(line[1][2][1]) > zmax:
            zmax = int(line[1][2][1])

    return xmin, xmax, ymin, ymax, zmin, zmax

def flip_cube(inst: str, coord: tuple, states: set) -> set:

    if (ACTIVE_AREA[0] <= coord[0] <= ACTIVE_AREA[1] and\
            ACTIVE_AREA[0] <= coord[1] <= ACTIVE_AREA[1] and\
            ACTIVE_AREA[0] <= coord[2] <= ACTIVE_AREA[1]):

        if inst == 'on':
            states.add(tuple(coord))
        else:
            try:
                states.remove(tuple(coord))
            except KeyError:
                # print(f'Coord already off')
                pass
    return states


def check_instruction(inst: tuple[tuple]) -> bool:
    print(f'Checking set: {inst}')

    x1, x2 = inst[0][0], inst[0][1]
    y1, y2 = inst[1][0], inst[1][1]
    z1, z2 = inst[2][0], inst[2][1]

    if x1 < ACTIVE_AREA[0] and x2 < ACTIVE_AREA[0]:
        # print(f'Set is lower than X')
        # print(inst)
        return False
    elif x1 > ACTIVE_AREA[1] and x2 > ACTIVE_AREA[1]:
        # print(f'Set is higher than X')
        # print(inst)
        return False
    elif y1 < ACTIVE_AREA[0] and y2 < ACTIVE_AREA[0]:
        # print(f'Set is lower than Y')
        # print(inst)
        return False
    elif y1 > ACTIVE_AREA[1] and y2 > ACTIVE_AREA[1]:
        # print(f'Set is higher than Y')
        # print(inst)
        return False
    elif z1 < ACTIVE_AREA[0] and z2 < ACTIVE_AREA[0]:
        # print(f'Set is lower than Z')
        # print(inst)
        return False
    elif z1 > ACTIVE_AREA[1] and z2 > ACTIVE_AREA[1]:
        # print(f'Set is higher than Z')
        # print(inst)
        return False
    else:
        # print(f'Set is someone in active area')
        # print(f'{inst}')
        return True


def cube_list(inst: tuple[tuple]) -> list:
    x1, x2 = inst[0][0], inst[0][1]
    y1, y2 = inst[1][0], inst[1][1]
    z1, z2 = inst[2][0], inst[2][1]

    cubes = []

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            for z in range(z1, z2 + 1):
                cubes.append([x, y, z])

    return cubes

def read_file():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        data = f.read().splitlines()
        instruction = []
        for line in data:
            inst, coord = line.split(' ')

            start = coord.index('=')
            end = coord.index(',', start + 1)
            x1, x2 = coord[start + 1:end].split('..')

            start = coord.index('=', end + 1)
            end = coord.index(',', start + 1)
            y1, y2 = coord[start + 1:end].split('..')

            start = coord.index('=', end + 1)
            z1, z2 = coord[start + 1:].split('..')

            cuboid = ((int(x1), int(x2)), (int(y1), int(y2)), (int(z1), int(z2)))
            instruction.append((inst, cuboid))

    return instruction


def main():
    data = read_file()
    day_twentytwo(data)

if __name__ == "__main__":
    raise SystemExit(main())
