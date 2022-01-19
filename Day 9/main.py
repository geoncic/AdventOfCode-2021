import collections
from typing import Generator


def dayNine():
    data = readFile()

    coords = collections.defaultdict(lambda: 9)

    for y, line in enumerate(data):
        for x, c in enumerate(line):
            coords[(x, y)] = int(c)

    print(f'Part One: Risk Level is {partOne_alt(coords)[0]}')
    print(f'Part Two: Basin Size is {partOne_alt(coords)[1]}')


def partOne_alt(data):
    risk_level = 0
    minimas = []
    basins = []
    for (x, y), n in data.items():
        if all(data.get(pt, 9) > n for pt in adjacent(x, y)):
            minimas.append((x, y))
            risk_level += n + 1

    for x, y in minimas:
        seen = set()
        todo = [(x, y)]

        while todo:
            x, y = todo.pop()
            seen.add((x, y))
            for pt in adjacent(x, y):
                if pt not in seen and data.get(pt, 9) < 9:
                    todo.append(pt)

        basins.append(len(seen))
    basin_sort_3 = sorted(basins)
    basin_sort_3 = basin_sort_3[-3:]
    basin_size = basin_sort_3[0]*basin_sort_3[1]*basin_sort_3[2]

    return risk_level, basin_size


def adjacent(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1


def readFile():
    with open('input.txt') as f:
        data = f.read().split('\n')
        data = [list(i) for i in data]
    return data


if __name__ == "__main__":
    dayNine()
