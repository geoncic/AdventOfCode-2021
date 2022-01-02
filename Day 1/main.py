def dayOne():
    depths = readFile()

    print(f'Part One: {partOne(depths)}')
    print(f'Part Two: {partTwo(depths)}')
    # partTwo(depths)

# This returns one less than the actual result. Not sure why
def partOne(depths):
    prev_depth = depths[0]
    count = 0

    for depth in depths[1:]:
        if depth > prev_depth:
            count += 1
        prev_depth = depth
    return count


def partTwo(depths):
    prev_depth_sum = depths[0]+depths[1]+depths[2]
    count = 0
    # return prev_depth_sum

    for i, current in enumerate(depths[3:]):
        depth_sum = depths[i+1] + depths[i+2] + current
        if depth_sum > prev_depth_sum:
            count += 1
        prev_depth_sum = depth_sum

    return count

def readFile():
    with open("input.txt") as file:
        depths = file.readlines()
        depths = [int(depth) for depth in depths]
        return depths

if __name__ == "__main__":
    Day1 = dayOne()
