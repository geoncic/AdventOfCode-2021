import collections
from typing import Generator


def dayEleven():
    data = readFile()
    coords = collections.defaultdict(lambda: x)

    for y, line in enumerate(data):
        for x, c in enumerate(line):
            coords[(x, y)] = int(c)
    print(data)
    print(coords)
    partOne(coords, 100)
    partOne(coords, 1000)


def partOne(coords, cycles):
    flashes = 0
    c = 0

    while c != cycles:
        c += 1
        cycle_flash = 0
        seen = set()
        triggered = []
        todo = []
        for (x, y), n in coords.items():
            if coords.get((x, y)) == 9:
                coords[(x, y)] = 0
                flashes += 1
                cycle_flash += 1
            else:
                coords[(x, y)] += 1

        for x in coords:
            triggered = eval_triggered(coords, x, triggered)

        for x, y in triggered:
            todo.append((x, y))

        while todo:
            x, y = todo.pop()
            seen.add((x, y))
            for pt in adjacent(x, y):
                if coords.get(pt) != 0:
                    if coords.get(pt) == 9:
                        todo.append(pt)
                        coords[pt] = 0
                        flashes += 1
                        cycle_flash += 1
                    else:
                        coords[pt] += 1
                else:
                    pass
        if cycle_flash == 100:
            print(f'Cycle {c} saw {cycle_flash} flashes!')
            break
        else:
            pass
    print(f'Total of {flashes} flashes in {c} Cycles')


def eval_triggered(coords, pt, triggered):
    if coords.get(pt) == 0:
        triggered.append(pt)
    return triggered


def adjacent(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    yield x - 1, y - 1
    yield x, y - 1
    yield x + 1, y - 1
    yield x - 1, y
    yield x + 1, y
    yield x - 1, y + 1
    yield x, y + 1
    yield x + 1, y + 1


def readFile():
    with open('input.txt') as f:
        data = f.read().split('\n')
        data = [list(i) for i in data]
    return data


if __name__ == "__main__":
    dayEleven()
