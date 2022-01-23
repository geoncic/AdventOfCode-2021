import ast
from collections.abc import Sequence
from itertools import chain, count
from collections import defaultdict


def calculate(snailfish: list[list], sig: str, type: str, operation: str) -> dict:
    ret = defaultdict(list)
    split_dict(snailfish, sig, 'list', operation, ret)
    return ret

def split_dict(seq: list, sig: str, type: str, operation: str, map: dict):
    operation = 'None'
    left = seq[0]
    left_sig = sig + '0'
    right = seq[1]
    right_sig = sig + '1'
    map[left_sig] = [left, type, operation]
    map[right_sig] = [right, type, operation]

    if len(left_sig) > 3 and isinstance(left, list):
        operation = 'Explode'
        map[left_sig][2] = operation
    if len(right_sig) > 3 and isinstance(right, list):
        operation = 'Explode'
        map[right_sig][2] = operation
    if isinstance(left, list):
        # check(left, left_sig, 'list', operation)
        split_dict(left, left_sig, 'list', operation, map)

    else:
        type = 'int'
        map[left_sig][1] = type
    if isinstance(right, list):
        # rightcheck = calculate(right, right_sig, 'list', operation)
        split_dict(right, right_sig, 'list', operation, map)
    else:
        type = 'int'
        map[right_sig][1] = type

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
        for i in range(len(key)):
            pre_key += key[i]
            list_copy = sf_dict[pre_key][0]
            sum_key = key[len(pre_key):]

            """Take advantage of the mutable property of lists, and only
            update one...is that what's actually going on here???? 
            """

            # if len(zero_key) == 3:
            #     print(f'Adding to {zero_key}')
            #     list_copy[int(zero_key[0])][int(zero_key[1])][int(zero_key[2])] += value
            # if len(zero_key) == 2:
            #     print(f'Adding to {zero_key}')
            #     list_copy[int(zero_key[0])][int(zero_key[1])] += value

            if len(sum_key) == 1:
                list_copy[int(sum_key[0])] += value

    def _find_right(key: str):
        test_key = ""
        print(f'Finding Right Key')
        right_key_flip = key.replace('1', '2').replace('0', '1').replace('2', '0')
        print(right_key_flip)
        for i in range(len(key)):
            test_key += right_key_flip[i]
            list_copy = sf_dict[test_key][0]
            if isinstance(list_copy, int):
                print(f'Found Int! {list_copy}')
                print(f'Key Signature is: {test_key}')
                return test_key

    def _find_left(key: str):
        pass




    # Getting so close, not doing correctly if adjacent number is inside a nested list

    for key, value in list(sf_dict.items()):
        print(f'Key is: {key}')
        if value[2] == "Explode":
            side = key[-1]
            sig_trim = key[:-1]
            if side == '1':
                print(f'Explode list is right side: {sf_dict[key]}')
                print(f'{side}')
                print(f'Finding Left Digit.....')


                left_check_sig_flip = key[-1].replace('1', '2').replace('0', '1').replace('2', '0')
                print(f'Right List: Left Check Sig Flip: {left_check_sig_flip}')
                left_check_sig = key[:-1] + left_check_sig_flip
                print(f'Right List: Left Check Sig: {left_check_sig}: {sf_dict[left_check_sig]}')



                right_check_sig_flip = sig_trim[-1].replace('1', '2').replace('0', '1').replace('2', '0')
                print(f'Right List: Left Check Sig Flip: {left_check_sig_flip}')
                right_check_sig = sig_trim[:-1] + right_check_sig_flip

                right_check_sig = _find_right(key)

                # print(f'Right List: Right Check Sig: {right_check_sig}: {sf_dict[right_check_sig]}')

            else:
                print(f'Explode list is left side')
                print(f'Sig trim: {sig_trim}')
                left_check_sig_flip = sig_trim[-1].replace('1', '2').replace('0', '1').replace('2', '0')
                print(f'Left Check Sig Flip: {left_check_sig_flip}')
                left_check_sig = sig_trim[:-1] + left_check_sig_flip
                print(f'Left Check Sig: {left_check_sig}')
                right_check_sig_flip = key[-1].replace('1', '2').replace('0', '1').replace('2', '0')
                print(f'Right Check Sig Flip: {right_check_sig_flip}')
                right_check_sig = key[:-1] + right_check_sig_flip
                print(f'Right Check Sig: {right_check_sig}')
                # left_key = find_sig_key(sf_dict, left_check_sig)
                # right_key = find_sig_key(sf_dict, right_check_sig)


            if max(key) != "0":
                print(f'Left Check Sig: {left_check_sig}')
                print(sf_dict[left_check_sig])
                if sf_dict[left_check_sig][1] == 'int':
                    _sum(left_check_sig, value[0][0])
            else:
                print(f'Value: {value[0]} with key {key} is left most {value[1]}')

            if min(key) != "1":
                print(f'Right Check Sig: {right_check_sig}')
                # print(sf_dict[right_check_sig])
                if sf_dict[right_check_sig][1] == 'int':
                    _sum(right_check_sig, value[0][1])
            else:
                print(f'Value: {value[0]} with key {key} is right most {value[1]}')

            sf_dict[key] = [0, 'int', 'None']
            sf_dict.pop(key + '0', None)
            sf_dict.pop(key + '1', None)

            _zero(key)
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
    # print(data[1])
    # fish_dict = defaultdict()
    # map = {}
    print(depth(data[0]))
    print(data[0])
    fish_dict = calculate(data[2], '', 'list', 'None')
    # print(fish_dict)
    reduce(fish_dict)
    # new_fish = add_fish(data[0], data[1])

