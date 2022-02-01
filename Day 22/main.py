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

    reboots = [Reboot.parse(line[0], line[1]) for line in data]

    for step in reboots:
       print(step)
    # xmin, xmax, ymin, ymax, zmin, zmax = create_array(data)
    # x_os = abs(xmin)
    # y_os = abs(ymin)
    # z_os = abs(zmin)
    #
    # print(xmin, xmax, ymin, ymax, zmin, zmax)
    # reactor = np.zeros((xmax + x_os, ymax + y_os, zmax + z_os))
    # print(reactor)
    #
    # # Todo: Create a numpy array based on largest and smallest values


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
            self.x1 - self.x0 *
            self.y1 - self.y0 *
            self.z1 - self.z0
        )

    def intersects(self, other: Cube) -> bool:
        return (
            self.x0 <= other.x1 - 1 and
            self.x1 - 1 >= other.x0 and
            self.y0 <= other.y1 - 1 and
            self.y1 - 1 >= other.y0 and
            self.z0 <= other.z1 - 1 and
            self.z1 - 1 >= other.z0
        )


    @classmethod
    def parse(cls, x0: int, x1: int, y0: int, y1: int, z0: int, z1: int) -> Cube:
        return cls(
            x0, x1 + 1,
            y0, y1 + 1,
            z0, z1 + 1,
        )


class Reboot(NamedTuple):
    on: bool
    cube: Cube

    @classmethod
    def parse(cls, s: str, inst: tuple[tuple]) -> Reboot:
        status = s
        x0, x1 = inst[0][0], inst[0][1]
        y0, y1 = inst[1][0], inst[1][1]
        z0, z1 = inst[2][0], inst[2][1]

        return cls(status == 'on', Cube.parse(x0, x1, y0, y1, z0, z1))

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
