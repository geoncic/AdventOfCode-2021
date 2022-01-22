import ast
from collections.abc import Sequence
from itertools import chain, count


def reduce(snailfish: list[list]) -> list:
    pass

def check(snailfish: list[list], sig: str) -> bool:
    # print(snailfish)
    # levels = depth(snailfish)
    # print(levels)
    split_dict(snailfish, sig)


def split_dict(seq: list, sig):
    left = seq[0]
    left_sig = sig + 'l'
    # print(f'Left Side: {left} with Sig: {left_sig}')
    right = seq[1]
    right_sig = sig + 'r'
    # print(f'Left Side: {right} with Sig: {right_sig}')
    # if levels == 0:
    #     print(f'Last level -> Left: {left}, Right -> {right}: Level: {levels}')
    if len(left_sig) > 3 and isinstance(left, list):
        print(f'Left Explodes! {left} {left_sig}')
    if len(right_sig) > 3 and isinstance(right, list):
        print(f'Right Explodes! {right} {right_sig}')
    if isinstance(left, list):
        leftcheck = check(left, left_sig)
    else:
        print(f'Dead End for Left: {left}, Level: {left_sig}')
    if isinstance(right, list):
        right = check(right, right_sig)
    else:
        print(f'Dead End for Right: {right}, Level: {right_sig}')
    # for i in range(levels):
    #     left = seq[0]
    #     right = seq [1]
    #     print(f'Left: {left}, and Right: {right} are Level: {i}')
    #     if isinstance(left, list):
    #         leftcheck = check(left)
    #     if isinstance(right, list):
    #         rightcheck = check(right)

def num_dict(seq: list) -> dict:
    pass

def depth(seq: list):
    seq = iter(seq)
    try:
        for level in count():
            seq = chain([next(seq)], seq)
            seq = chain.from_iterable(s for s in seq if isinstance(s, Sequence))
    except StopIteration:
        return level



def add_fish(a: list, b: list) -> list:
    comb_fish = []
    comb_fish.append(a)
    comb_fish.append(b)
    return comb_fish


def read_file():
    with open('input.txt') as f:
        file = f.read().split()
        output = []
        for i, line in enumerate(file):
            output.append(ast.literal_eval(line))
    return output


if __name__ == "__main__":
    data = read_file()
    # comb_fish = add_fish(data[0], data[1])
    # print(comb_fish)
    # check(comb_fish)
    print(data[0])
    check(data[0], '')
    # new_fish = add_fish(data[0], data[1])

