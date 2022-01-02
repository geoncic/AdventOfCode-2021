from collections import defaultdict

def daySeven():
    data = readFile()
    opt_loc, cost = partOne(data)
    opt_loc2, cost2 = partTwo(data)
    print(f'Part One: The optimum location is {opt_loc} with a cost of {cost}')
    print(f'Part Two: The optimum location is {opt_loc} with a cost of {cost}')

    partOne(data)

def partOne(data):
    # Create map of crab positions
    crabMap = {}
    max_pos = max(data)
    cost_list = []


    for crab in data:
        if crab not in crabMap:
            crabMap[crab] = 0
        crabMap[crab] += 1

    for i in range(max_pos):
        cost = 0
        for pos, count in crabMap.items():
            cost += abs(pos - i)*count
        cost_list.append(cost)
    opt_loc = cost_list.index(min(cost_list))
    cost = cost_list[opt_loc]
    return opt_loc, cost

# This is another scenario where the summation makes the time exponential
def partTwo(data):
    # Create map of crab positions
    crabMap = {}
    max_pos = max(data)
    cost_list = []


    for crab in data:
        if crab not in crabMap:
            crabMap[crab] = 0
        crabMap[crab] += 1

        print(crabMap)

    # for i in range(max_pos):
    #     dist = 0
    #     cost = 0
    #     for pos, count in crabMap.items():
    #         dist += abs(pos - i)*count
    #         cost = sum(range(1, dist + 1))
    #     cost_list.append(cost)
    # opt_loc = cost_list.index(min(cost_list))
    # cost = cost_list[opt_loc]
    # return opt_loc, cost


def readFile():
    with open('input.txt') as f:
        data = f.read()
        data = [int(i) for i in data.split(',')]
    return data

if __name__ == "__main__":
    daySeven()