
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
    # print(len(seq))
    left = seq[0]
    left_sig = sig + '0'
    # print(f'Left Side: {left} with Sig: {left_sig}')
    right = seq[1]
    right_sig = sig + '1'
    # print(f'Right Side: {right} with Sig: {right_sig}')
    # if levels == 0:
    #     print(f'Last level -> Left: {left}, Right -> {right}: Level: {levels}')
    # levels = depth(seq)

    # fish_dict[left_sig] = [str(left).replace(" ", ""), type, operation]
    # fish_dict[right_sig] = [str(right).replace(" ", ""), type, operation]

    fish_dict[left_sig] = [left, type, operation]
    fish_dict[right_sig] = [right, type, operation]


    # fish_dict[str(left).replace(" ", "")] = [left_sig, type, operation]
    # fish_dict[str(right).replace(" ", "")] = [right_sig, type, operation]

    if len(left_sig) > 3 and isinstance(left, list):
        # print(f'Left Explodes! {left} {left_sig} {type}')
        operation = 'Explode'

        fish_dict[left_sig][2] = 'Explode'
        # fish_dict[str(left).replace(" ", "")][2] = 'Explode'
        # print(fish_dict[str(left).replace(" ", "")])
    if len(right_sig) > 3 and isinstance(right, list):
        # print(f'Right Explodes! {right} {right_sig} {type}')
        operation = 'Explode'
        fish_dict[right_sig][2] = 'Explode'
        # fish_dict[str(left).replace(" ", "")][2] = 'Explode'
        # print(fish_dict[str(right).replace(" ", "")])
    if isinstance(left, list):
        # print(f'Checking Further: {left} {left_sig} {type}')
        leftcheck = check(left, left_sig, 'list', operation)
    else:
        type = 'int'
        fish_dict[left_sig][1] = type
        # fish_dict[str(left).replace(" ", "")][1] = type
        # print(f'Dead End for Left: {left}, Level: {left_sig}, Type: {type}')
    if isinstance(right, list):
        # print(f'Checking Further: {right} {right_sig} {type}')
        rightcheck = check(right, right_sig, 'list', operation)
    else:
        type = 'int'
        fish_dict[right_sig][1] = type
        # fish_dict[str(right).replace(" ", "")][1] = type
        # print(f'Dead End for Right: {right}, Level: {right_sig}, Type: {type}')

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
    def _zero(key):
        pre_key = ''
        for i in range(len(key)):
            pre_key += key[i]
            list_copy = sf_dict[pre_key][0]
            # print('\n')
            # print(f'Key: {key}')
            # print(f'Pre Key: {pre_key}')
            # print(f'Dict Value: {sf_dict[pre_key][0]}')
            # print(f'Copy: {list_copy}')

            zero_key = key[len(pre_key):]
            # print(f' Zero Key: {zero_key}')
            # if len(zero_key) == 3:
            #     list_copy[int(zero_key[0])][int(zero_key[1])][int(zero_key[2])] = 0
            # if len(zero_key) == 2:
            #     list_copy[int(zero_key[0])][int(zero_key[1])] = 0
            if len(zero_key) == 1:
                list_copy[int(zero_key[0])] = 0

    def _sum(key, value):
        pre_key = ''
        print(f'Sum key is {key}')
        print(f'Sum Value is {value}')
        for i in range(len(key)):
            print(f'i is {i}')

            pre_key += key[i]
            list_copy = sf_dict[pre_key][0]

            zero_key = key[len(pre_key):]
            print(f' Sum Key: {zero_key}')

            """Take advantage of the mutable property of lists, and only
            update one...is that what's actually going on here???? 
            """

            # if len(zero_key) == 3:
            #     print(f'Adding to {zero_key}')
            #     list_copy[int(zero_key[0])][int(zero_key[1])][int(zero_key[2])] += value
            # if len(zero_key) == 2:
            #     print(f'Adding to {zero_key}')
            #     list_copy[int(zero_key[0])][int(zero_key[1])] += value
            if len(zero_key) == 1:
                print(f'Adding to {zero_key}')
                list_copy[int(zero_key[0])] += value



    for key, value in list(sf_dict.items()):
        # if len(value[0]) > 3:
        #     print(key)
        #     print(value)
        if value[2] == "Explode":

            sig_trim = key[:-1]
            left_check_sig_flip = sig_trim[-1].replace('1', '2').replace('0', '1').replace('2', '0')
            left_check_sig = sig_trim[:-1] + left_check_sig_flip
            right_check_sig_flip = key[-1].replace('1', '2').replace('0', '1').replace('2', '0')


            right_check_sig = key[:-1] + right_check_sig_flip
            # left_key = find_sig_key(sf_dict, left_check_sig)
            # right_key = find_sig_key(sf_dict, right_check_sig)

            # print(key)
            # print(f'Max key {max(key)}')
            if max(key) != "0":
                # print(sf_dict[left_check_sig])
                if sf_dict[left_check_sig][1] == 'int':

                    # print(f'Value {value[0]}')
                    # print(f'Left {value[0][0]}')
                    # print(f'Modify {sf_dict[left_check_sig]}')
                    # sf_dict[left_check_sig][0] +=  value[0][0]
                    # print(f'Value added to Left: {sf_dict[left_check_sig]}')
                    _sum(left_check_sig, value[0][0])

            else:
                print(f'Value: {value[0]} with key {key} is left most {value[1]}')
            if min(key) != "1":
                # print(sf_dict[right_check_sig])
                if sf_dict[right_check_sig][1] == 'int':
                    # print(f'Value {value[0]}')
                    # print(f'Right {value[0][1]}')
                    # print(f'Modify {sf_dict[right_check_sig]}')
                    # sf_dict[right_check_sig][0] += value[0][1]
                    # print(f'Value added to Right: {sf_dict[right_check_sig]}')
                    _sum(right_check_sig, value[0][1])
            else:
                print(f'Value: {value[0]} with key {key} is right most {value[1]}')

            sf_dict[key] = [0, 'int', 'None']
            sf_dict.pop(key + '0', None)
            sf_dict.pop(key + '1', None)

            _zero(key)


            # pre_key = ''


            # for i in range(len(key)):
            #     # list_copy = []
            #
            #     pre_key += key[i]
            #
            #     list_copy = sf_dict[pre_key][0]
            #
            #     # try:
            #     #     list_copy = sf_dict[pre_key][0]
            #     # except AttributeError:
            #     #     print(f'Attribute Error with {sf_dict[pre_key][0]}')
            #     #     list_copy = [sf_dict[pre_key][0]]
            #     print('\n')
            #     print(f'Key: {key}')
            #     print(f'Pre Key: {pre_key}')
            #     print(f'Dict Value: {sf_dict[pre_key][0]}')
            #     print(f'Copy: {list_copy}')
            #
            #     zero_key = key[len(pre_key):]
            #
            #
            #     print(f' Zero Key: {zero_key}')
            #
            #     if len(zero_key) == 3:
            #         list_copy[int(zero_key[0])][int(zero_key[1])][int(zero_key[2])] = 0
            #     if len(zero_key) == 2:
            #         list_copy[int(zero_key[0])][int(zero_key[1])] = 0
            #     if len(zero_key) == 1:
            #         list_copy[int(zero_key[0])] = 0



                # try:
                #     print(f'Key 110: {list_copy[1][1][0]}')
                # except TypeError:
                #     print('Tis an Int')
                #     print(list_copy)
                # try:
                #     print(f'Key 10: {list_copy[1][0]}')
                # except TypeError:
                #     print('Tis an Int')
                #     print(list_copy)
                # try:
                #     print(f'Key 0: {list_copy[0]}')
                # except TypeError:
                #     print('Tis an Int')
                #     print(list_copy)

            # sig_trim = value[0][:-1]
            # left_check_sig_flip = sig_trim[-1].replace('1', '2').replace('0', '1').replace('2', '0')
            # left_check_sig = sig_trim[:-1] + left_check_sig_flip
            # right_check_sig_flip = value[0][-1].replace('1', '2').replace('0', '1').replace('2', '0')
            # right_check_sig = value[0][:-1] + right_check_sig_flip
            # left_key = find_sig_key(sf_dict, left_check_sig)
            # right_key = find_sig_key(sf_dict, right_check_sig)
            # print(key)
            # print(value[0])
            # print(left_key)
            # print(left_check_sig)
            # print(right_key)
            # print(right_check_sig)

            print(sf_dict)

            new_sfnumber = []
            new_sfnumber.append(sf_dict['0'][0])
            new_sfnumber.append(sf_dict['1'][0])

            print('\n')
            print(new_sfnumber)

def find_sig_key(input_dict: dict, value: str):
    return {k for k, v in input_dict.items() if k == value}


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
    # fish_dict = defaultdict()
    fish_dict = {}
    check(data[0], '', 'list', 'None')
    print(fish_dict)
    reduce(fish_dict)
    # new_fish = add_fish(data[0], data[1])

