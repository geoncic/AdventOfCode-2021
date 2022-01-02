def dayTwo():
    path = readFile()
    print(f'Part One: {partOne(path)}')
    print(f'Part Two: {partTwo(path)}')
def partOne(path):
    horizontal = 0
    depth = 0
    for i, step in enumerate(path):
        dir = step[0]
        amp = int(step[1])

        if dir == 'forward':
            horizontal += amp
        elif dir == 'down':
            depth += amp
        elif dir == 'up':
            depth -= amp
        else:
            print('Direction Not Valid')
    return horizontal*depth

def partTwo(path):
    x = 0
    y = 0
    aim = 0

    for i, step in enumerate(path):
        dir = step[0]
        amp = int(step[1])

        if dir == 'forward':
            x += amp
            y += aim*amp
        elif dir == 'down':
            aim += amp
        elif dir == 'up':
            aim -= amp
        else:
            print('Direction Not Valid')
    return x*y

def readFile():
    with open('input.txt') as f:
        path = []
        data = f.read().splitlines()

        for instruction in data:
            path.append(tuple(instruction.strip().split()))

        return path

if __name__ == "__main__":
    Day2 = dayTwo()
