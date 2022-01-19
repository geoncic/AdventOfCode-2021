def read_file():
    with open('input.txt') as f:
        file = f.read().split('\n')
    return file


def part_one(dots, folds, steps):
    for step in folds[0:steps]:
        direction, loc = step
        dots = fold_paper(dots, direction, loc)
        make_paper(dots)
    return len(dots)


def part_two(dots, folds):
    for step in folds:
        direction, loc = step
        dots = fold_paper(dots, direction, loc)
    finished = make_paper(dots)
    return len(dots), finished


def fold_paper(dots, direction, loc):
    paper_coords = set()
    for coord in dots:
        dot_x, dot_y = coord
        if direction == 'y':
            if dot_y < loc:
                paper_coords.add((dot_x, dot_y))
            else:
                d_y = abs(loc - dot_y)
                dot_y = loc - d_y
                paper_coords.add((dot_x, dot_y))
        elif direction == 'x':
            if dot_x < loc:
                paper_coords.add((dot_x, dot_y))
            else:
                d_x = abs(loc - dot_x)
                dot_x = loc - d_x
                paper_coords.add((dot_x, dot_y))
    return paper_coords


def paper_size(dots, folds):
    x_coords, y_coords = zip(*dots)
    x_fold = max(x_coords)
    y_fold = max(y_coords)
    for step in folds:
        direction, loc = step
        if direction == 'y':
            if loc < y_fold:
                y_fold = loc
        elif direction == 'x':
            if loc < x_fold:
                x_fold = loc
    return x_fold, y_fold


def make_paper(dots):
    x_coords, y_coords = zip(*dots)
    x_max = max(x_coords)
    y_max = max(y_coords)
    paper = [['.' for _ in range(x_max+1)] for _ in range(y_max+1)]

    for loc in dots:
        x_dot, y_dot = loc
        paper[y_dot][x_dot] = '#'
    return paper


if __name__ == "__main__":
    data = read_file()
    coords = []
    inst = []
    for line in data:
        if ',' in line:
            x, y = line.split(',')
            coords.append([int(x), int(y)])
        elif '=' in line:
            fold_dir, pos = line.split('=')
            fold_dir = fold_dir[-1]
            inst.append([fold_dir, int(pos)])

    solution, final_paper = part_two(coords, inst)
    for line in final_paper:
        print(line)
    print(f'Part Two: The number of dots are {solution}')
