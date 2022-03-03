from __future__ import annotations

from typing import NamedTuple

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def day_twentythree(data):
    part_one(data)


def part_one(data):
    print(data)


def read_file():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        data = f.read().splitlines()

    return data


def main():
    data = read_file()
    day_twentythree(data)


if __name__ == "__main__":
    raise SystemExit(main())
