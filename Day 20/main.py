import argparse
import collections
import os.path
from typing import Generator


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test.txt')


def day_twenty(algo: str, image: list) -> ...:
    print(algo)
    print(image)
    coords = collections.defaultdict(lambda: x)
    for y, line in enumerate(image):
        for x, pixel in enumerate(line):
            coords[(x, y)]  = pixel

            # if pixel == '#':
            #     coords[(x, y)] = 1
            # else:
            #     coords[(x, y)] = 0
    print(coords)

    new_image = collections.defaultdict(lambda: x)

    for (x, y), n in coords.items():
        todo = []
        print(f'Evaluating Point ({x}, {y})')
        for pt in adjacent(x, y):
            todo.append(coords.get(pt, '.'))

        print(todo)


def adjacent(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    yield x - 1, y - 1
    yield x, y - 1
    yield x + 1, y - 1
    yield x - 1, y
    yield x + 1, y
    yield x - 1, y + 1
    yield x, y + 1
    yield x + 1, y + 1

def read_file():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        file = f.read().split("\n\n")
        algo = file[0]
        image = []
        for idx, line in enumerate(file[1].split("\n")):
            image.append([])
            for pixel in line:
                image[idx].append(pixel)

    return algo, image


def main():
    algo, image = read_file()
    day_twenty(algo, image)


if __name__ == "__main__":
    raise SystemExit(main())
