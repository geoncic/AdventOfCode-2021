import ast
from math import floor, ceil
from collections.abc import Sequence
from itertools import chain, count
from collections import defaultdict

def part_one(input):
    global count
    sf_number = input[0]

    for i in range(1, len(input)):
        count = 0
        sf_number = [sf_number, input[i]]
        print(f'Reducing: {sf_number}')
        sf_number = compute_number(sf_number)
        print(sf_number)

    print(sf_number)


def compute_number(sf_number: list):
    global count
    count += 1
    fish_number = sf_number
    fish_dict = create_dict_from_str(sf_number, '', 'list', 'None')

    if any([True for k, v in fish_dict.items() if v[2] == 'Explode']):
        print(f"Yes, Value: '{'Explode'}' exists in dictionary")
        fish_dict = explode_dict(fish_dict)
        fish_number = [fish_dict['0'][0], fish_dict['1'][0]]
        compute_number(fish_number)
    elif any([True for k, v in fish_dict.items() if v[2] == 'Split']):
        print(f"Yes, Value: '{'Split'}' exists in dictionary")
        fish_dict = split_dict(fish_dict)
        fish_number = [fish_dict['0'][0], fish_dict['1'][0]]
        compute_number(fish_number)
    else:
        print(f"No, Value: '{'Explode'}' does not exists in dictionary")

    print(f'The Final Number Is!!! {fish_number}')
    print(f'Count: {count}')
    return fish_number

def create_dict_from_str(snailfish: list[list], sig: str, t: str, operation: str) -> dict:
    ret = defaultdict(list)
    create_dict(snailfish, sig, t, operation, ret)
    return ret

def create_str_from_dict(sf_dict: dict) -> str:
    return [sf_dict['0'][0], sf_dict['1'][0]]


def create_dict(seq: list, sig: str, t: str, operation: str, m: dict):
    operation = 'None'
    left = seq[0]
    left_sig = sig + '0'
    right = seq[1]
    right_sig = sig + '1'
    m[left_sig] = [left, t, operation]
    m[right_sig] = [right, t, operation]

    if len(left_sig) > 3 and isinstance(left, list):
        operation = 'Explode'
        m[left_sig][2] = operation
    if len(right_sig) > 3 and isinstance(right, list):
        operation = 'Explode'
        m[right_sig][2] = operation
    if isinstance(left, list):
        create_dict(left, left_sig, 'list', operation, m)

    else:
        t = 'int'
        m[left_sig][1] = t
        if m[left_sig][0] > 9:
            m[left_sig][2] = "Split"
    if isinstance(right, list):
        create_dict(right, right_sig, 'list', operation, m)
    else:
        t = 'int'
        m[right_sig][1] = t
        if m[right_sig][0] > 9:
            m[right_sig][2] = "Split"


def depth(seq: list):
    seq = iter(seq)
    level = 0
    try:
        for level in count():
            seq = chain([next(seq)], seq)
            seq = chain.from_iterable(s for s in seq if isinstance(s, Sequence))
    except StopIteration:
        return level


def explode_dict(sf_dict: dict) -> dict:

    def _zero(k):
        pre_key = ''
        for i in range(len(k)):
            pre_key += k[i]
            list_copy = sf_dict[pre_key][0]
            zero_key = k[len(pre_key):]
            if len(zero_key) == 1:
                list_copy[int(zero_key[0])] = 0

    def _sum(k, v):
        pre_key = ''
        for i in range(len(k)):
            pre_key += k[i]
            value_copy = sf_dict[pre_key][0]
            sum_key = k[len(pre_key):]

            # I only care about sf_dict[0] and sf_dict[1] being accurate

            if len(sum_key) == 1:
                value_copy[int(sum_key[0])] += v



    def _find_l_key(k: str):
        test_key = k + '0'
        while True:
            if sf_dict[test_key][1] == 'int':
                return test_key
            else:
                test_key += '1'

    def _find_r_key(k: str):
        test_key = k + '1'
        while True:
            if sf_dict[test_key][1] == 'int':
                return test_key
            else:
                test_key += '0'

    for key, value in list(sf_dict.items()):
        if value[2] == "Explode":
            side = key[-1]
            if side == '1':
                left_check_sig = _find_l_key(key[:-1])
                right_check_sig = _find_r_key(key.rstrip('1')[:-1])

            else:
                left_check_sig = _find_l_key(key.rstrip('0')[:-1])

                right_check_sig = _find_r_key(key[:-1])

            if max(key) != "0":
                if sf_dict[left_check_sig][1] == 'int':
                    _sum(left_check_sig, value[0][0])
            else:
                print(f'Value: {value[0]} with key {key} is left most {value[1]}')

            if min(key) != "1":
                if sf_dict[right_check_sig][1] == 'int':
                    _sum(right_check_sig, value[0][1])
            else:
                print(f'Value: {value[0]} with key {key} is right most {value[1]}')

            sf_dict[key] = [0, 'int', 'None']
            sf_dict.pop(key + '0')
            sf_dict.pop(key + '1')

            _zero(key)
            # print(sf_dict)

    new_sfnumber = [sf_dict['0'][0], sf_dict['1'][0]]

    # print('\n')
    # print(new_sfnumber)
    return sf_dict



def split_dict(sf_dict: dict) -> dict:
    def _clean_dict(k, sp_list):
        pre_key = ''
        for i in range(len(k)):
            pre_key += k[i]
            list_copy = sf_dict[pre_key][0]
            clean_key = k[len(pre_key):]

            # I only care about sf_dict[0] and sf_dict[1] being accurate
            if len(clean_key) == 1:
                list_copy[int(clean_key[0])] = sp_list




    for key, value in list(sf_dict.items()):
        if value[2] == "Split":
            split_list = [floor(value[0] / 2), ceil(value[0] / 2)]
            sf_dict[key] = [split_list, 'list', 'None']
            if split_list[0] > 9:
                sf_dict[key + '0'] = [split_list[0], 'int', 'Split']
            else:
                sf_dict[key + '0'] = [split_list[0], 'int', 'None']
            if split_list[1] > 9:
                sf_dict[key + '1'] = [split_list[1], 'int', 'Split']
            else:
                sf_dict[key + '1'] = [split_list[1], 'int', 'None']

            _clean_dict(key, split_list)

    return sf_dict




def find_sig_key(input_dict: dict, value: str):
    return {k for k, v in input_dict.items() if k == value}


def add_fish(a: list, b: list) -> list:
    comb_fish = [a, b]
    return comb_fish


def read_file():
    with open('test.txt') as f:
        file = f.read().split()
        output = []
        for i, line in enumerate(file):
            output.append(ast.literal_eval(line))
    return output


if __name__ == "__main__":
    data = read_file()
    # comb_fish = add_fish(data[0], data[1])
    # fish_dict = create_dict_from_str(data[4], '', 'list', 'None')
    # exploded_dict = explode_dict(fish_dict)
    # clean_list = create_str_from_dict(exploded_dict)
    # clean_dict = create_dict_from_str(clean_list, '', 'list', 'None')
    # print(f'Exploded List: {clean_list}')
    # print(clean_dict)
    # splited_dict = split_dict(clean_dict)
    # clean_list = create_str_from_dict(splited_dict)
    # print(f'Split List: {clean_list}')

    # print(f'Splited Dict: {splited_dict}')
    # count = 0
    # sf_number = compute_number(data[0])
    # print(f'Count is {count}')
    # print(f'Reduced number is: {sf_number}')
    part_one(data)