def read_file():
    with open('input.txt') as f:
        data = f.read().split('\n')
    return data

def part_one(coords, inst, steps):
    # x_fold, y_fold = paper_size(coords, inst)
    # size = int(x_fold)*int(y_fold)
    # print(f'Paper size is {size}')
    for step, line in enumerate(inst[0:steps]):
        dir, loc = line
        coords = fold_paper(coords, dir, loc)
        print(step)
        print(coords)
        make_paper(coords)
    # num_dots = size - len(coords)
    print(f'length is {len(coords)}')
    return len(coords)


def fold_paper(coords, dir, loc):
    paper_coords = set()
    # print(coords)
    for coord in coords:
        x, y = coord
        if dir == 'y':
            if y < loc:
                paper_coords.add((x, y))
            else:
                print(f'Coord ({x}, {y}) below fold')
                d_y = abs(loc - y)
                y = loc - d_y
                print(f'Now in ({x}, {y}) position')
                paper_coords.add((x, y))
        elif dir == 'x':
            if x < loc:
                paper_coords.add((x, y))
            else:
                print(f'Coord ({x}, {y}) below fold')
                d_x = abs(loc - x)
                x = loc - d_x
                print(f'Now in ({x}, {y}) position')
                paper_coords.add((x, y))

    return paper_coords

def paper_size(coords, inst):
    x_coords, y_coords = zip(*coords)
    x_fold = max(x_coords)
    y_fold = max(y_coords)
    for step, line in enumerate(inst):
        dir, loc = line
        if dir == 'y':
            if loc < y_fold:
                y_fold = loc
        elif dir == 'x':
            if loc < x_fold:
                x_fold = loc
    return x_fold, y_fold

def make_paper(coords):
    x_coords, y_coords = zip(*coords)
    x_max = max(x_coords)
    y_max = max(y_coords)

    paper = [['.' for x in range(x_max+1)] for y in range(y_max+1)]
    for pos in coords:
        x, y = pos
        paper[y][x] = '#'
    for line in paper:
        print(line)
    return paper

if __name__ == "__main__":
    data = read_file()
    coords = []
    inst = []
    for line in data:
        if ',' in line:
            x, y = line.split(',')
            coords.append([int(x),int(y)])
        elif '=' in line:
            dir, pos = line.split('=')
            dir = dir[-1]
            inst.append([dir, int(pos)])



    solution = part_one(coords, inst, 1)
    print(solution)



