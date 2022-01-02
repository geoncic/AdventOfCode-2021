from collections import defaultdict
def daySix():
    data = readFile()
    data_one = data.copy()
    data_two = data.copy()

    print(f'Part One number of fishes is: {len(partOne(data_one, 80))}')
    print(f'Part Two number of fishes is: {partTwo(data_two, 256)}')

def partOne(data, n):
    for x in range(n):
        for i, n in enumerate(data):
            data[i] -= 1
            if n == 0:
                data[i] = 6
                data.append(9)
    return data

def partTwo(data, n):
    # Create map of fish
    fishMap = {}

    for fish in data:
        if fish not in fishMap:
            fishMap[fish] = 0
        fishMap[fish] += 1

    # Change fish states
    for day in range(n):
        updatedFishMap = defaultdict(int)

        # Change each fish state
        for fish, count in fishMap.items():
            if fish == 0:
                updatedFishMap[6] += count
                updatedFishMap[8] += count
            else:
                updatedFishMap[fish-1] += count

            fishMap = updatedFishMap

    return sum(fishMap.values())


def readFile():
    with open('input.txt') as f:
        data = f.read()
        data = [int(i) for i in data.split(',')]
    return data

if __name__ == "__main__":
    daySix()