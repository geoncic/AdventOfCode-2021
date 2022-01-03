def dayEight():
    data = readFile()
    print(f'Part One: Number of instances is {partOne(data)}')
    print(f'Part Two: Sum of all output is {partTwo(data)}')

def partOne(data):
    data_output = []
    digit_counter = 0

    for line in data:
        line_output = []
        line_map = decodeLine(line[0])
        for d in line[1]:
            for x, y in line_map.items():
                if len(segDiff(d, y)) == 0:
                    line_output.append(x)
        data_output.append((line_output))

    for row in data_output:
        for d in row:
            if d == 1 or d == 4 or d == 7 or d == 8:
                digit_counter += 1
    return digit_counter

def partTwo(data):
    data_output = []
    sum_output = 0

    for line in data:
        line_output = []
        line_map = decodeLine(line[0])
        for d in line[1]:
            for x, y in line_map.items():
                if len(segDiff(d, y)) == 0:
                    line_output.append(x)
        data_output.append((line_output))

    for line in data_output:
        output = [str(x) for x in line]
        output = ''.join(output)
        sum_output += int(output)

    return sum_output

def decodeLine(digit_list):
    digitMap = {}

    # Solve for 1, 4, 7, and 8
    for i, d in enumerate(digit_list):
        if len(d) == 2:
            digitMap[1] = d
        elif len(d) == 4:
            digitMap[4] = d
        elif len(d) == 3:
            digitMap[7] = d
        elif len(d) == 7:
            digitMap[8] = d
        else:
            pass

    # solve for 0, 6, and 9
    for i, d in enumerate(digit_list):
        if len(d) == 6:
            diff = segDiff(d, digitMap[8])
            if diff not in digitMap[4]:
                digitMap[9] = d
            elif diff not in digitMap[1]:
                digitMap[0] = d
            else:
                digitMap[6] = d
        else:
            pass

    # solve for 2, 3, and 5
    for i, d in enumerate(digit_list):
        if len(d) == 5:
            diff = segDiff(d, digitMap[8])
            if (segCounter(diff, digitMap[9]) + segCounter(diff, digitMap[6])) == 0:
                digitMap[2] = d
            elif (segCounter(diff, digitMap[9]) + segCounter(diff, digitMap[6])) == 1:
                digitMap[3] = d
            else:
                digitMap[5] = d

    return digitMap

def segCounter(seg_diff, x):
    counter = 0
    for i in seg_diff:
        if i not in x:
            counter += 1
        else:
            pass
    return counter

def segDiff(a, b):
    set_diff = []
    for x in a:
        if x in b:
            pass
        else:
            set_diff.append(x)
    for x in b:
        if x in a:
            pass
        else:
            set_diff.append(x)

    set_diff = ''.join(set_diff)
    return set_diff


def readFile():
    with open('input.txt') as f:
        data = []

        for line in f:
            digit = []
            parsed_line = line.strip()
            parsed_line = parsed_line.split(' | ')
            for element in parsed_line:
                digit.append(element.split())
            data.append(digit)

    return data


if __name__ == "__main__":
    dayEight()
