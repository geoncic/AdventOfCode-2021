def daySeven():
    data = readFile()
    opt_loc, cost = partOne(data)
    max_loc = max(data)
    sum_list = summationMap(max_loc)
    opt_loc2, cost2 = partTwo(data, sum_list)
    print(f'Part One: The optimum location is {opt_loc} with a cost of {cost}')
    print(f'Part Two: The optimum location is {opt_loc2} with a cost of {cost2}')


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
def partTwo(data, sum_list):
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
            dist = abs(pos - i)
            cost += sum_list[dist]*count
        cost_list.append(cost)

    opt_loc = cost_list.index(min(cost_list))
    cost = cost_list[opt_loc]
    return opt_loc, cost


def summationMap(number):
    sum_map = []
    for i in range(number+1):
        if i == 0:
            sum_map.append(0)
        else:
            sum_map.append(i+sum_map[i-1])
    return sum_map


def readFile():
    with open('input.txt') as f:
        data = f.read()
        data = [int(i) for i in data.split(',')]
    return data


if __name__ == "__main__":
    daySeven()
