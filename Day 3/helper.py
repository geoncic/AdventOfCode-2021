from collections import Counter

def bit_not(n, numbits=12):
    return (1 << numbits) - 1 - n

def data_length(data):
    num_digits = 0
    max_digits = len(max(data, key=len))
    min_digits = len(min(data, key=len))

    if max_digits != min_digits:
        print("Dataset is not valid")
    else:
        print("Dataset is valid, will continue to process:")
        print(f'Data length is {max_digits} bits...')
        num_digits = max_digits

    return num_digits

def create_dictionary(data, num_digits):
    bit_dict = {}

    for i in range(num_digits):
        bit_dict[str(i)] = []

        for line in data:
            bit_dict[str(i)].append(line[i])
    return bit_dict

def most_common_value(dict):
    mcv = []
    for values in dict.values():
        bit_count = Counter(values)
        if bit_count.most_common(1)[0][1] == int(len(values) / 2):
            mcv.append('1')
        else:
            mcv.append(bit_count.most_common(1)[0][0])
    return mcv

def least_common_value(dict):
    lcv = []
    for values in dict.values():
        bit_count = Counter(values)
        if bit_count.most_common(1)[0][1] == int(len(values) / 2):
            lcv.append('0')
        else:
            lcv.append(bit_count.most_common()[-1][0])
    return lcv

def filter_by_MCB(data, num_bits):
    power_data = create_dictionary(data, num_bits)
    power_data_copy = power_data.copy()
    data_copy = data.copy()

    for i in range(len(power_data)):
        most_common = most_common_value(power_data_copy)
        data_copy = list(filter(lambda x: (x[i] == most_common[i]), data_copy))
        power_data_copy = create_dictionary(data_copy, num_bits)
        if len(data_copy) == 1:
            return data_copy

def filter_by_LCB(data, num_bits):
    power_data = create_dictionary(data, num_bits)
    power_data_copy = power_data.copy()
    data_copy = data.copy()

    for i in range(len(power_data)):
        least_common = least_common_value(power_data_copy)
        data_copy = list(filter(lambda x: (x[i] == least_common[i]), data_copy))
        power_data_copy = create_dictionary(data_copy, num_bits)
        if len(data_copy) == 1:
            return data_copy
