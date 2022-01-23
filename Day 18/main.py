import ast
from collections.abc import Sequence
from collections import defaultdict
from itertools import chain, count


def reduce(snailfish: list[list]) -> list:
    pass

def check(snailfish: list[list], sig: str, type: str, operation: str) -> bool:
    # print(snailfish)
    # levels = depth(snailfish)
    # print(levels)
    split_dict(snailfish, sig, 'list', operation)


def split_dict(seq: list, sig: str, type: str, operation: str):
    operation = 'None'
    left = seq[0]
    left_sig = sig + 'l'
    print(f'Left Side: {left} with Sig: {left_sig}')
    right = seq[1]
    right_sig = sig + 'r'
    print(f'Right Side: {right} with Sig: {right_sig}')
    # if levels == 0:
    #     print(f'Last level -> Left: {left}, Right -> {right}: Level: {levels}')
    levels = depth(seq)
    fish_dict[str(left)] = [left_sig, type, operation]
    fish_dict[str(right)] = [right_sig, type, operation]

    if len(left_sig) > 3 and isinstance(left, list):
        print(f'Left Explodes! {left} {left_sig} {type}')
        operation = 'Explode'
        fish_dict[str(left)][2]= 'Explode'
        print(fish_dict[str(left)])
    if len(right_sig) > 3 and isinstance(right, list):
        print(f'Right Explodes! {right} {right_sig} {type}')
        operation = 'Explode'
        fish_dict[str(left)][2]= 'Explode'
        print(fish_dict[str(right)])
    if isinstance(left, list):
        print(f'Checking Further: {left} {left_sig} {type}')
        leftcheck = check(left, left_sig, 'list', operation)
    else:
        type = 'int'
        print(f'Dead End for Left: {left}, Level: {left_sig}, Type: {type}')
    if isinstance(right, list):
        print(f'Checking Further: {right} {right_sig} {type}')
        rightcheck = check(right, right_sig, 'list', operation)
    else:
        type = 'int'
        print(f'Dead End for Right: {right}, Level: {right_sig}, Type: {type}')

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

def reduce(sf_dict: dict) -> dict:
    for key, value in sf_dict.items():
        print(key)
        print(value)
        if value[2] == "Explode":
            print(f'Must explode {key}')
            print(f'Signature is {value[0]}')


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
    fish_dict = {}
    check(data[0], '', 'list', 'None')
    print(fish_dict)
    reduce(fish_dict)
    # new_fish = add_fish(data[0], data[1])

