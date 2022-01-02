from collections import Counter
# from helper import bit_not, data_length, create_dictionary
from helper import *

def dayThree():
    data = readFile()
    print(f'Part One: Power Consumption is {partOne(data)}')
    print(f'Part Two: Life Support Rating is  {partTwo(data)}')

def partOne(data):
    num_bits = data_length(data)
    power_data = create_dictionary(data, num_bits)
    most_common = most_common_value(power_data)

    gamma_rate = ''.join(most_common)
    gamma_rate = bin(int(gamma_rate,2))
    epsilon_rate = bin(bit_not(int(gamma_rate,2), num_bits))
    power_consumption = int(gamma_rate,2)*int(epsilon_rate,2)

    return power_consumption

def partTwo(data):
    num_bits = data_length(data)

    OGR = filter_by_MCB(data, num_bits)
    C02SR = filter_by_LCB(data, num_bits)
    LSR = int(OGR[0],2)*int(C02SR[0],2)

    return LSR


def readFile():
    with open('input.txt') as f:
        data = []
        file = f.read().splitlines()

        for line in file:
            data.append(line)
        return data

if __name__ == "__main__":
    Day3 = dayThree()
