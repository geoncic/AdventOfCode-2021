import argparse
import os.path
import numpy as np
from typing import Generator


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def part_one(a: str, img: list) -> int:
    steps = 2
    final_size = ((len(img)+2*steps), (len(img[0])+2*steps))
    pcount = 0

    for s in range(steps):
        img = day_twenty(a, img)

    while len(img) > final_size[0]:
        img = img[1:-1, 1:-1]
    for line in img:
        for p in line:
            if p == '#':
                pcount += 1

    return pcount


def day_twenty(algo: str, image: list) -> ...:
    image = expand_image(image)
    new_image = image.copy()

    for y, line in enumerate(image):
        for x, pixel in enumerate(line):
            pixel_sig = []
            for pt in adjacent(x, y):
                ix, iy = pt
                try:
                    pixel_sig.append(image[iy][ix])
                except IndexError:
                    pixel_sig.append('.')
            alg_index = pix_string_to_int(pixel_sig)
            new_image[y][x] = algo[alg_index]

    return new_image


def pix_string_to_int(plist: list) -> int:
    bin_str = ''
    for p in plist:
        if p == '.':
            bin_str += '0'
        else:
            bin_str += '1'
    return int(bin_str, 2)


def expand_image(image: list):
    return np.pad(image, pad_width=4, mode='constant', constant_values='.')


def adjacent(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    yield x - 1, y - 1
    yield x, y - 1
    yield x + 1, y - 1
    yield x - 1, y
    yield x, y
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
    print(f'Part One: {part_one(algo, image)}')


if __name__ == "__main__":
    raise SystemExit(main())
