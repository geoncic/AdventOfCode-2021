from collections import defaultdict, Counter
import pandas as pd


def read_file():
    with open('input.txt') as f:
        file = f.read().split('\n')
    return file


def part_one(polymer, inst, steps):
    for x in range(steps):
        polymer = polymer_insert(polymer, inst)
    poly_count = pd.Series(list(polymer)).value_counts()
    max_count = poly_count.max()
    min_count = poly_count.min()
    return max_count-min_count


def part_two(polymer, steps):
    cnt = polymer_counter(polymer)
    for x in range(steps):
        cnt, char_cnt = polymer_builder(cnt)
    return max(char_cnt.values()) - min(char_cnt.values())+1


def polymer_counter(polymer):
    poly_cnt = Counter()
    for i in range(0, len(polymer)-1):
        piece = polymer[i] + polymer[i + 1]
        poly_cnt[piece] += 1
    return poly_cnt


def polymer_builder(poly_count):
    new_cnt = Counter()
    char_counts = Counter()
    for i, v in poly_count.items():
        first = i[0] + instructions[i]
        second = instructions[i] + i[1]
        new_cnt[first] += v
        new_cnt[second] += v
        char_counts[i[0]] += v
        char_counts[instructions[i]] += v
    return new_cnt, char_counts


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

    part_one_sol = part_one(chain, instructions, 10)
    part_two_sol = part_two(chain, 40)

    print(f'Part One: Solution is {part_one_sol}')
    print(f'Part Two: Solution is {part_two_sol}')
