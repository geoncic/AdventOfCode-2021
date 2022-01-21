def day_eight():
    data = read_file()
    print(f'Part One: Number of instances is {part_one(data)}')
    print(f'Part Two: Sum of all output is {part_two(data)}')


def part_one(data):
    data_output = []
    digit_counter = 0

    for line in data:
        line_output = []
        line_map = decode_line(line[0])
        for d in line[1]:
            for x, y in line_map.items():
                if len(s_diff(d, y)) == 0:
                    line_output.append(x)
        data_output.append(line_output)

    for row in data_output:
        for d in row:
            if d == 1 or d == 4 or d == 7 or d == 8:
                digit_counter += 1
    return digit_counter


def part_two(data):
    data_output = []
    sum_output = 0

    for line in data:
        line_output = []
        line_map = decode_line(line[0])
        for d in line[1]:
            for x, y in line_map.items():
                if len(s_diff(d, y)) == 0:
                    line_output.append(x)
        data_output.append(line_output)

    for line in data_output:
        output = [str(x) for x in line]
        output = ''.join(output)
        sum_output += int(output)

    return sum_output


def decode_line(digit_list):
    digit_map = {}

    # Solve for 1, 4, 7, and 8
    for i, d in enumerate(digit_list):
        if len(d) == 2:
            digit_map[1] = d
        elif len(d) == 4:
            digit_map[4] = d
        elif len(d) == 3:
            digit_map[7] = d
        elif len(d) == 7:
            digit_map[8] = d
        else:
            pass

    # solve for 0, 6, and 9
    for i, d in enumerate(digit_list):
        if len(d) == 6:
            diff = s_diff(d, digit_map[8])
            if diff not in digit_map[4]:
                digit_map[9] = d
            elif diff not in digit_map[1]:
                digit_map[0] = d
            else:
                digit_map[6] = d
        else:
            pass

    # solve for 2, 3, and 5
    for i, d in enumerate(digit_list):
        if len(d) == 5:
            diff = s_diff(d, digit_map[8])
            if (seg_counter(diff, digit_map[9]) + seg_counter(diff, digit_map[6])) == 0:
                digit_map[2] = d
            elif (seg_counter(diff, digit_map[9]) + seg_counter(diff, digit_map[6])) == 1:
                digit_map[3] = d
            else:
                digit_map[5] = d

    return digit_map


def seg_counter(seg_diff, x):
    counter = 0
    for i in seg_diff:
        if i not in x:
            counter += 1
        else:
            pass
    return counter


def s_diff(a, b):
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


def read_file():
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
    day_eight()
