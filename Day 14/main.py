from collections import defaultdict
import pandas as pd


def read_file():
    with open('test.txt') as f:
        file = f.read().split('\n')
    return file


def part_one(polymer, inst, steps):
    for x in range(steps):
        print(x)
        polymer = polymer_insert(polymer, inst)
    poly_count = pd.Series(list(polymer)).value_counts()
    max_count = poly_count.max()
    min_count = poly_count.min()
    return max_count-min_count


def part_two():
    pass


def polymer_insert(polymer, inst):
    chain_build = [polymer[0]]
    for i in range(len(polymer) - 1):
        segment = polymer[i] + polymer[i + 1]
        if segment in inst:
            chain_build.append(inst[segment] + polymer[i + 1])
        else:
            print(f'Segment {segment} is not in instruction dictionary')
    new_polymer = ''.join(chain_build)
    return new_polymer


if __name__ == "__main__":
    data = read_file()
    instructions = defaultdict()
    chain = data[0]
    for line in data:
        if '->' in line:
            pair, ins = line.split(' -> ')
            instructions[pair] = ins

    part_one_sol = part_one(chain, instructions, 20)

    print(f'Part One: Solution is {part_one_sol}')
    