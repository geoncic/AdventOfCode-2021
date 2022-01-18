from collections import defaultdict

def read_file():
    with open('input.txt') as f:
        file = f.read().split('\n')
    return file


def part_one():
    pass


def part_two():
    pass


if __name__ == "__main__":
    data = read_file()
    instructions = defaultdict()
    chain = data[0]
    for line in data:
        if '->' in line:
            pair, ins = line.split(' -> ')
            instructions[pair] = ins
    print(instructions)
    print(chain)