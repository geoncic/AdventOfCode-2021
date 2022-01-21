from typing import Generator
import heapq
# import collections


# Why is this more efficient than the commented out block of code?


def compute(graph: dict, s: tuple, d: tuple) -> int:
    todo = [(0, s)]
    best_at = {}

    while todo:
        c, last_coord = heapq.heappop(todo)
        if last_coord in best_at and c >= best_at[last_coord]:
            continue
        else:
            best_at[last_coord] = c
        if last_coord == d:
            return c
        for pt in adjacent(last_coord):
            if pt in graph:
                heapq.heappush(todo, (c + graph[pt], pt))
    return best_at[d]

# def compute(graph: dict, s: tuple, d: tuple) -> int:
#     visited = set()
#     cost = collections.defaultdict(int)
#     todo = [(0, s)]
#     heapq.heapify(todo)
#
#     while todo:
#         c, last_coord = heapq.heappop(todo)
#         if last_coord in visited:
#             continue
#         visited.add(last_coord)
#         cost[last_coord] = c
#         if last_coord == max(graph):
#             break
#         for pt in adjacent(last_coord):
#             if pt not in graph:
#                 continue
#             heapq.heappush(todo, (c + graph[pt], pt))
#     return cost[d]


def nine_wrap(n: int) -> int:
    while n > 9:
        n -= 9
    return n


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
    src = (0, 0)
    dst = max(coords_p2)
    cost = compute(coords_p2, src, dst)
    return cost


def read_file():
    data = {}
    with open('test.txt') as f:
        file = f.read()
        for y, line in enumerate(file.splitlines()):
            for x, c in enumerate(line):
                data[(x, y)] = int(c)
    return data


def read_file_p2():
    data = {}
    with open('input.txt') as f:
        file = f.read()
        lines = file.splitlines()
        height = len(lines)
        width = len(lines[0])
        for y, line in enumerate(file.splitlines()):
            for x, c in enumerate(line):
                for y_i in range(5):
                    for x_i in range(5):
                        data[(x + x_i * width), (y + y_i * height)] = (
                            nine_wrap(int(c) + x_i + y_i)
                        )
    return data


if __name__ == "__main__":
    coords = read_file()
    coords_p2 = read_file_p2()
    print(f'Part One: Path cost is {part_one()}')
    print(f'Part Two: Path cost is {part_two()}')
