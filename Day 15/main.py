from typing import Generator
import heapq
import collections


def compute(graph: dict, s: tuple, d: tuple) -> int:
    visited = set()
    cost = collections.defaultdict(int)
    todo = [(0, s)]
    heapq.heapify(todo)

    while todo:
        print(todo)
        c, last_coord = heapq.heappop(todo)
        print(f'Checking the last_coord {last_coord}')
        if last_coord in visited:
            continue
        print(f'Adding last_coord cost: {c}: {last_coord} to visited')
        visited.add(last_coord)
        cost[last_coord] = c
        if last_coord == max(graph):
            print(f'Reached the end!')
            break
        for pt in adjacent(last_coord):
            if pt not in graph:
                continue
            heapq.heappush(todo, (c + graph[pt], pt))
    return cost[d]


def adjacent(pt: tuple) -> Generator[tuple[int, int], None, None]:
    x, y = pt
    yield x + 1, y
    yield x, y + 1
    yield x - 1, y
    yield x, y - 1


def part_one():
    src = (0, 0)
    dst = max(coords)
    cost = compute(coords, src, dst)
    return cost


def part_two():
    pass


def read_file():
    data = {}
    with open('test.txt') as f:
        file = f.read()
        for y, line in enumerate(file.splitlines()):
            for x, c in enumerate(line):
                data[(x, y)] = int(c)
    return data


if __name__ == "__main__":
    coords = read_file()
    print(f'Part One: Path cost is {part_one()}')
